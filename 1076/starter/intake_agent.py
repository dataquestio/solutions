"""Cedar Valley Intake - agent / host (STARTER).

This file consumes the MCP server you built in intake_server.py. It holds the bridge helpers, the agentic loop,
and a main() that runs the three sources in order.

PROVIDED FOR YOU (below): the imports, the model constants, and the complete SYSTEM_PROMPT.
Use the SYSTEM_PROMPT exactly as written - it encodes the intake rules the agent must follow,
and keeping it identical is what makes everyone's results comparable.

YOU WILL ADD, as you work through the project:
  - Step 8:  load_mcp_tools() and execute_tool()  (the MCP <-> OpenAI bridge)
  - Step 9:  the IntakeAgent class                 (the agentic loop)
  - Step 10: main()                                (run the three sources, write the output)

Uses OpenAI (gpt-4o-mini). Needs OPENAI_API_KEY, set in a .env file. Run from the project folder:
    python intake_agent.py
"""
import asyncio
import json
import os

from openai import OpenAI
from dotenv import load_dotenv

from intake_server import mcp, ROSTER, SITES

load_dotenv()   # read OPENAI_API_KEY from a .env file in the project folder

MODEL = "gpt-4o-mini"
MAX_ITERATIONS = 30

# ---------------------------------------------------------------------------
# PROVIDED: the system prompt. Do not rewrite it - use it as-is.
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = f"""You are the intake agent for the Cedar Valley spring bird count. Turn
messy observation notes into clean records using ONLY the provided tools.

For each observation:
  1. resolve_species on the species text. Never identify a bird yourself - trust the tool. If it
     returns no_match, flag out_of_taxonomy and move on: do NOT build or commit a record for that
     note, and never put a species_code the tool did not return.
  2. Decide the count and date (see rules below).
  3. Build the record and call commit_observation, passing the original note as raw_input.
     commit_observation is authoritative: if it returns duplicate=true the record is a
     duplicate and has ALREADY been queued for review - do not flag it again. If it returns
     errors, fix them if you can; if you cannot fix them, you MUST flag the note (a blank or
     missing required field is incomplete_record). Never leave a note neither committed nor flagged.

Counts: "a"/"one"/singular=1, "pair"=2, "half a dozen"=6. An estimate like "12 (est)" is
usable (use 12). Only a count with no number ("handful", "a flock", "didn't count") is vague.
Dates: resolve "yesterday"/"Sat" against the reference date given. Known sites: {", ".join(SITES)}.
Never invent a missing field - if a note has no location or no species, do not fill it in and
do not commit it; flag it as incomplete_record.

Flag with flag_for_review using the FIRST reason that applies:
  1. resolve_species is "no_match"                         -> out_of_taxonomy
  2. species missing, or a required field can't be recovered -> incomplete_record
  3. resolve_species category is not "species" (a spuh)    -> ambiguous_species
  4. the date can't be pinned to a day                      -> missing_date
  5. the count is vague                                     -> ambiguous_count

Process EVERY observation. When done, reply with a one-line summary."""


# ==========================================================================
# STEP 8 - YOUR CODE: the MCP <-> OpenAI bridge
# load_mcp_tools(mcp_server) -> (openai_tools, tool_functions)
# execute_tool(function_name, arguments, tool_functions) -> JSON string
# ==========================================================================



# ==========================================================================
# STEP 9 - YOUR CODE: the agent
# class IntakeAgent with __init__(self, client, mcp_server) and
# run_source(self, source_name, content, reference_date)
# ==========================================================================



# ==========================================================================
# STEP 10 - YOUR CODE: main()
# Run the three sources in order, then write clean_roster.json + review_queue.json.
# ==========================================================================



if __name__ == "__main__":
    main()
