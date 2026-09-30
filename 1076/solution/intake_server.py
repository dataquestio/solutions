"""Cedar Valley Intake - MCP server (the reusable tool layer, like 1045's product_server).

Holds the data and state, and exposes four tools. The tools are module-level functions so
FastMCP can read their type hints and docstrings to build the tool schemas.
Run from the project folder so the "data/..." paths resolve.
"""
import json
import re

from pydantic import BaseModel, Field, ValidationError
from fastmcp import FastMCP

COUNT_WINDOW_START = "2026-05-01"   # the count runs through May 2026
COUNT_WINDOW_END = "2026-05-31"
SITES = ["Cedar Ridge", "Marsh", "North Marsh"]


# --- The record model: structured output + validation ---
class Observation(BaseModel):
    species_code: str
    common_name: str
    scientific_name: str
    count: int = Field(gt=0)
    date: str          # ISO YYYY-MM-DD
    location: str = Field(min_length=1)   # a blank location is incomplete, not a valid record
    source: str


# --- Taxonomy lookup (backs resolve_species) ---
def normalize(text):
    return text.strip().lower()


def load_taxonomy():
    """Build one lookup: every canonical name, scientific name, and alias -> its record."""
    with open("data/taxonomy_subset.json") as f:
        species = json.load(f)["species"]

    by_code = {}
    lookup = {}
    for s in species:
        by_code[s["speciesCode"]] = s
        lookup[normalize(s["comName"])] = s
        lookup[normalize(s["sciName"])] = s
        if s["category"] != "species":            # index the group stem: "gull sp." -> "gull"
            lookup[normalize(s["comName"].replace(" sp.", ""))] = s

    with open("data/aliases.json") as f:
        aliases = json.load(f)["aliases"]
    for alias in aliases:
        lookup[normalize(alias)] = by_code[aliases[alias]]

    return by_code, lookup


BY_CODE, LOOKUP = load_taxonomy()


def resolve(text):
    """Return the matching taxon record, or None. Exact dict lookup only (no fuzzy matching):
    the caller passes the species name; we match it against canonical names, scientific names,
    and the alias table. Pulling the species out of surrounding words is the agent's job."""
    query = normalize(text)
    if query in LOOKUP:
        return LOOKUP[query]
    return None


def validate(record):
    """Return {"valid": bool, "errors": [...]}: correct shape (the model), a date in the
    count window, and a species_code that is a real 'species' (not a 'spuh' group)."""
    errors = []
    try:
        Observation(**record)
    except ValidationError as e:
        errors.append(str(e))

    date = record.get("date", "")
    if not re.search(r"^\d{4}-\d{2}-\d{2}$", date):
        errors.append("date must look like YYYY-MM-DD")
    elif not (COUNT_WINDOW_START <= date <= COUNT_WINDOW_END):
        errors.append("date is outside the count window")

    species = BY_CODE.get(record.get("species_code"))
    if species is not None and species["category"] != "species":
        errors.append(f"{species['comName']} is a group, not a single species")

    return {"valid": len(errors) == 0, "errors": errors}


# --- Roster: the accumulating run state (the one class) ---
class Roster:
    def __init__(self):
        self.clean = []
        self.review = []

    def duplicate_of(self, record):
        """Return the record_id this duplicates (checking the roster so far), or None."""
        for r in self.clean:
            same_species = r["species_code"] == record["species_code"]
            same_date = r["date"] == record["date"]
            same_place = r["location"].strip().lower() == record["location"].strip().lower()
            if same_species and same_date and same_place:
                return r["record_id"]
        return None

    def add(self, record):
        record = record.copy()
        record["record_id"] = f"obs-{len(self.clean) + 1}"
        self.clean.append(record)
        return record["record_id"]

    def flag(self, raw_input, source, reason, existing_record_id=None):
        item = {
            "raw_input": raw_input,
            "source": source,
            "reason": reason,
            "existing_record_id": existing_record_id,
        }
        if item not in self.review:      # don't queue the same thing twice
            self.review.append(item)


# --- MCP server: four tools over the data and state above ---
mcp = FastMCP("Cedar Valley Intake")
ROSTER = Roster()


@mcp.tool()
def resolve_species(text: str):
    """Resolve a messy species name, nickname, or typo to a canonical eBird taxon. Do NOT
    guess the species yourself. If the returned category is not "species" (e.g. a "spuh"
    group like "gull sp.") or match is "no_match", flag the record instead of committing.

    Args:
        text: the singular species name from the note, with surrounding words removed.
            Drop counts and filler and make it singular: 'pair of mallards' -> 'mallard',
            'half a dozen cedar waxwings' -> 'cedar waxwing', 'some kind of gull' -> 'gull',
            'a couple hawks' -> 'hawk'. Keep the observer's own spelling; do NOT fix typos
            ('Canda Goose' stays 'Canda Goose'). This tool only does an exact lookup.
    """
    match = resolve(text)
    if match is None:
        return {"match": "no_match"}
    return {
        "match": "ok",
        "species_code": match["speciesCode"],
        "common_name": match["comName"],
        "scientific_name": match["sciName"],
        "category": match["category"],
    }


@mcp.tool()
def validate_observation(record: dict):
    """Check a candidate record before committing: shape, a date in the count window, and a
    real 'species' code.

    Args:
        record: dict with species_code, common_name, scientific_name, count, date, location, source
    """
    return validate(record)


@mcp.tool()
def commit_observation(record: dict, raw_input: str = ""):
    """Authoritative gate: re-validates AND checks for duplicates, so nothing bad gets in. A
    duplicate is not committed; this tool records it as 'possible_duplicate' itself, so you do
    not need to flag duplicates separately.

    Args:
        record: the observation dict
        raw_input: the original note verbatim (kept on the review item if it's a duplicate)
    """
    check = validate(record)
    if not check["valid"]:
        return {"committed": False, "errors": check["errors"]}
    existing = ROSTER.duplicate_of(record)
    if existing is not None:
        ROSTER.flag(raw_input or record["common_name"], record["source"], "possible_duplicate", existing)
        return {"committed": False, "duplicate": True, "existing_record_id": existing}
    return {"committed": True, "record_id": ROSTER.add(record)}


@mcp.tool()
def flag_for_review(raw_input: str, source: str, reason: str):
    """Record a human-review item instead of guessing.

    Args:
        raw_input: the note verbatim
        source: which source it came from
        reason: ambiguous_species | ambiguous_count | missing_date | out_of_taxonomy | incomplete_record
    """
    ROSTER.flag(raw_input, source, reason)
    return {"queued": True}
