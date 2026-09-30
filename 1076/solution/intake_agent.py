"""Cedar Valley Intake - agent / host (consumes the MCP server).

Bridge helpers + the agentic loop + a main() that runs the sources in order.
Uses OpenAI (gpt-4o-mini). Needs OPENAI_API_KEY. Run from the project folder:
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


# --- MCP <-> OpenAI bridge ---
def load_mcp_tools(mcp_server):
    """Load the server's tools once: a list of OpenAI tool definitions and a name->function map.
    get_tools() is async and returns a dict of tools, each with .name, .description, .parameters,
    and .fn. It's the only async call, so we run it once with asyncio.run()."""
    tools_by_name = asyncio.run(mcp_server.get_tools())
    openai_tools = []
    tool_functions = {}
    for name in tools_by_name:
        tool = tools_by_name[name]
        openai_tools.append({
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.parameters,
            },
        })
        tool_functions[name] = tool.fn
    return openai_tools, tool_functions


def execute_tool(function_name, arguments, tool_functions):
    """Safely run a requested tool and return a JSON string (result or error)."""
    if function_name not in tool_functions:
        return json.dumps({"error": f"Unknown function: {function_name}"})
    try:
        result = tool_functions[function_name](**arguments)
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": f"Tool failed: {e}"})


# --- Agent ---
class IntakeAgent:
    def __init__(self, client, mcp_server):
        self.client = client
        self.tools, self.tool_functions = load_mcp_tools(mcp_server)

    def run_source(self, source_name, content, reference_date):
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Source: {source_name}\nReference date: {reference_date}\n\n{content}"},
        ]
        for step in range(MAX_ITERATIONS):
            response = self.client.chat.completions.create(
                model=MODEL,
                messages=messages,
                tools=self.tools,
                tool_choice="auto",
                temperature=0.2,
            )
            message = response.choices[0].message
            if not message.tool_calls:
                return message.content
            messages.append(message)
            for call in message.tool_calls:
                arguments = json.loads(call.function.arguments)
                print(f"  {call.function.name}({arguments})")
                result = execute_tool(call.function.name, arguments, self.tool_functions)
                messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
        return "Max iterations reached"


def main():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    agent = IntakeAgent(client, mcp)

    with open("data/source1_logbook.txt") as f:
        logbook = f.read()
    with open("data/source2_email.txt") as f:
        email = f.read()
    with open("data/source3_spreadsheet.json") as f:
        spreadsheet = f.read()

    # Order matters: "first committed wins" dedup depends on the logbook running first.
    sources = [
        ("logbook", logbook, "2026-05-09"),
        ("email", email, "2026-05-16"),
        ("spreadsheet", spreadsheet, "year 2026"),
    ]
    for source_name, content, reference_date in sources:
        print(f"\n=== {source_name} ===")
        print(agent.run_source(source_name, content, reference_date))

    with open("clean_roster.json", "w") as f:
        json.dump(ROSTER.clean, f, indent=2)
    with open("review_queue.json", "w") as f:
        json.dump(ROSTER.review, f, indent=2)
    print(f"\nDone. Committed {len(ROSTER.clean)}, flagged {len(ROSTER.review)}.")


if __name__ == "__main__":
    main()
