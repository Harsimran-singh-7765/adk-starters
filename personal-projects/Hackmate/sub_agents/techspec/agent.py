import os
from google.adk.agents import Agent

BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "techspec.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    instructions = f.read()

techspec_agent = Agent(
    name="techspec_agent",
    model="gemini-2.0-flash",
    description="Generates technical specifications including stack, APIs, and architecture.",
    instruction=instructions,
)
