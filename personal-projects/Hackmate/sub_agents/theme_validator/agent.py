import os
from google.adk.agents import Agent

BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "theme_validator.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    instructions = f.read()

theme_validator = Agent(
    name="theme_validator",
    model="gemini-2.0-flash",
    description="Validates the hackathon theme to ensure it is actionable and hackathon-friendly.",
    instruction=instructions,
)
