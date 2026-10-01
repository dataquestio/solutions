"""Verify your Cedar Valley intake solution. Run this after you finish the project:

    python validate_core.py

By default it runs the offline checks of the deterministic core (resolve, validate, Roster).
These need no API key and cost nothing. To ALSO test the full agent end to end, set
RUN_LLM_TEST = True below (that part needs OPENAI_API_KEY and makes real API calls).

Run from the project folder, with deps installed (pip install -r requirements.txt).
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Flip this to True to also run the agent on the three sources and check its output.
# It needs OPENAI_API_KEY set and will make real (small) API calls.
RUN_LLM_TEST = False

from intake_server import resolve, validate, Roster

passed = 0
failed = 0


def check(label, actual, expected):
    global passed, failed
    if actual == expected:
        passed = passed + 1
        print(f"[PASS] {label}")
    else:
        failed = failed + 1
        print(f"[FAIL] {label}\n    actual={actual!r} expected={expected!r}")


def code_of(text):
    match = resolve(text)
    if match is None:
        return "no_match"
    return match["speciesCode"]


def category_of(text):
    match = resolve(text)
    if match is None:
        return "no_match"
    return match["category"]


def run_core_tests():
    """The offline half: the deterministic machinery, no LLM and no network."""
    # resolve(): turn a messy species name into the right eBird code, or no_match.
    print("--- resolve ---")
    # typos and misnames of "Canada Goose" all resolve to its code
    check("'Canda Goose' -> cangoo", code_of("Canda Goose"), "cangoo")
    check("'Canadian Goose' -> cangoo", code_of("Canadian Goose"), "cangoo")
    # birder nickname and shortened forms, handled by the alias table
    check("'Canadas' -> cangoo", code_of("Canadas"), "cangoo")
    check("'Canada' -> cangoo", code_of("Canada"), "cangoo")
    # a scientific name resolves just like a common name
    check("'Quiscalus mexicanus' -> grtgra", code_of("Quiscalus mexicanus"), "grtgra")
    # more aliases and exact common names
    check("'annas hummingbird' -> annhum", code_of("annas hummingbird"), "annhum")
    check("'red-tail' -> rethaw", code_of("red-tail"), "rethaw")
    check("'mallard' -> mallar3", code_of("mallard"), "mallar3")
    check("'American Robbin' -> amerob", code_of("American Robbin"), "amerob")
    # a name that isn't in the taxonomy at all comes back as no_match
    check("'Jackalope Warbler' -> no_match", code_of("Jackalope Warbler"), "no_match")
    # group terms resolve to the "spuh" category, not a single species
    check("'gull' -> spuh", category_of("gull"), "spuh")
    check("'hawk' -> spuh", category_of("hawk"), "spuh")
    # resolve() does an exact lookup only; pulling the species name out of a
    # phrase is the agent's job, so a whole phrase must NOT resolve.
    check("'some kind of gull' -> no_match (agent must strip it)", code_of("some kind of gull"), "no_match")

    # validate(): a record passes only if its shape, date, and species all check out.
    # Start from one clean record, then break a single field at a time.
    print("\n--- validate ---")
    good_record = {"species_code": "grtgra", "common_name": "Great-tailed Grackle",
            "scientific_name": "Quiscalus mexicanus", "count": 4, "date": "2026-05-10",
            "location": "Cedar Ridge", "source": "spreadsheet"}
    check("clean record valid", validate(good_record)["valid"], True)
    # a "spuh" group code is not a single species, so it's rejected
    bad_spuh = good_record.copy()
    bad_spuh["species_code"] = "gullsp"
    check("spuh code rejected", validate(bad_spuh)["valid"], False)
    # count must be greater than 0
    bad_count = good_record.copy()
    bad_count["count"] = 0
    check("zero count rejected", validate(bad_count)["valid"], False)
    # location cannot be blank
    no_loc = good_record.copy()
    no_loc["location"] = ""
    check("blank location rejected", validate(no_loc)["valid"], False)
    # the date must fall inside the count window (May 2026)
    bad_date = good_record.copy()
    bad_date["date"] = "2026-07-01"
    check("date outside window rejected", validate(bad_date)["valid"], False)

    # Roster: catch duplicates, and never queue the same review item twice.
    print("\n--- roster: dedup + no double flag ---")
    roster = Roster()
    first = good_record.copy()
    first["species_code"] = "cangoo"
    first["date"] = "2026-05-09"
    first["location"] = "Cedar Ridge"
    roster.add(first)
    # the same sighting with a different-case location still counts as a duplicate
    again = first.copy()
    again["location"] = "cedar ridge"
    check("duplicate across case", roster.duplicate_of(again), "obs-1")
    # flagging the identical item twice should leave just one entry in review
    roster.flag("American Robbin", "spreadsheet", "incomplete_record")
    roster.flag("American Robbin", "spreadsheet", "incomplete_record")
    check("flag not double-queued", len(roster.review), 1)


def flagged(review, reason, needle):
    """True if some review item with this reason mentions needle in its raw_input."""
    for item in review:
        if item["reason"] == reason and needle.lower() in item["raw_input"].lower():
            return True
    return False


def run_llm_test():
    """The optional half: run the whole agent and check PROPERTIES of its output. An agent is
    not deterministic, so we check tolerant properties (a count range, invariants the tools
    enforce, a few stable flags), never an exact roster."""
    if not os.environ.get("OPENAI_API_KEY"):
        print("\n[SKIP] RUN_LLM_TEST is on but OPENAI_API_KEY is not set, so the agent test")
        print("       cannot run. Set your key, or set RUN_LLM_TEST back to False.")
        return

    # Only needed for this part, so import here (the offline checks above need none of it).
    from openai import OpenAI
    from intake_server import mcp, ROSTER
    from intake_agent import IntakeAgent

    print("\n--- llm: full agent run, checking properties (not exact output) ---")
    agent = IntakeAgent(OpenAI(api_key=os.environ.get("OPENAI_API_KEY")), mcp)
    with open("data/source1_logbook.txt") as f:
        logbook = f.read()
    with open("data/source2_email.txt") as f:
        email = f.read()
    with open("data/source3_spreadsheet.json") as f:
        spreadsheet = f.read()
    sources = [
        ("logbook", logbook, "2026-05-09"),
        ("email", email, "2026-05-16"),
        ("spreadsheet", spreadsheet, "year 2026"),
    ]
    for name, content, reference_date in sources:
        agent.run_source(name, content, reference_date)

    clean = ROSTER.clean
    review = ROSTER.review
    print(f"(agent committed {len(clean)}, flagged {len(review)})")

    # Invariants the tools ENFORCE, regardless of how the model words things:
    check("committed count is about 11", len(clean) >= 10 and len(clean) <= 12, True)
    blank_locations = [r for r in clean if r.get("location", "").strip() == ""]
    check("no committed record has a blank location", len(blank_locations), 0)

    seen = []
    duplicate_found = False
    for r in clean:
        key = (r["species_code"], r["date"], r["location"].strip().lower())
        if key in seen:
            duplicate_found = True
        seen.append(key)
    check("no duplicate sightings in the clean roster", duplicate_found, False)

    # Stable flags (the taxonomy is deterministic, so these land the same way every run):
    check("Jackalope flagged out_of_taxonomy", flagged(review, "out_of_taxonomy", "Jackalope"), True)
    check("'some kind of gull' flagged ambiguous_species", flagged(review, "ambiguous_species", "gull"), True)
    check("'a couple hawks' flagged ambiguous_species", flagged(review, "ambiguous_species", "hawks"), True)


run_core_tests()
if RUN_LLM_TEST:
    run_llm_test()

print(f"\n{passed} passed, {failed} failed")
if failed == 0:
    print("All checks passed.")
else:
    print("Some checks FAILED - see the [FAIL] lines above.")
