import os
from google.adk.agents import Agent

BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "validator.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    instructions = f.read()

validator_agent = Agent(
    name="validator_agent",
    model="gemini-2.0-flash",
    description="Final validation agent ensuring consistency, completeness, and clarity of all outputs.",
    instruction=instructions,
)
