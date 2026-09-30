"""Cedar Valley Intake - MCP server (STARTER).

This is the reusable tool layer: it holds
the data and state, and exposes tools for the agent to call.

PROVIDED FOR YOU (below, already written - read it, but you don't need to change it):
  - imports and the count-window constants
  - the taxonomy lookup layer: normalize(), load_taxonomy(), and resolve()

YOU WILL ADD, as you work through the project:
  - Step 2: the Observation model
  - Step 3: the Roster class
  - Step 4: the validate() helper
  - Steps 5-7: the FastMCP server and its four tools

Run everything from the project folder so the "data/..." paths resolve.
"""
import json
import re

from pydantic import BaseModel, Field, ValidationError
from fastmcp import FastMCP

COUNT_WINDOW_START = "2026-05-01"   # the count runs through May 2026
COUNT_WINDOW_END = "2026-05-31"
SITES = ["Cedar Ridge", "Marsh", "North Marsh"]


# ==========================================================================
# PROVIDED: the taxonomy lookup layer.
# This is typical Python code - loading JSON and
# building a dictionary. Read it so you know what resolve() returns, then
# move on. You will not change anything in this section.
# ==========================================================================
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


# ==========================================================================
# STEP 2 - YOUR CODE: the Observation model
# A Pydantic model that describes one clean record and validates its shape.
# ==========================================================================



# ==========================================================================
# STEP 3 - YOUR CODE: the Roster class
# The accumulating run state: the clean roster and the review queue.
# ==========================================================================



# ==========================================================================
# STEP 4 - YOUR CODE: the validate() helper
# Returns {"valid": bool, "errors": [...]} for a candidate record.
# ==========================================================================



# ==========================================================================
# STEPS 5-7 - YOUR CODE: the FastMCP server and its four tools
# Create the server and the module-scope ROSTER, then add:
#   resolve_species, validate_observation, commit_observation, flag_for_review
# ==========================================================================
