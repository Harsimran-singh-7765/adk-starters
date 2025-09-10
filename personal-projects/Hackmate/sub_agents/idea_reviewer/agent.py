import os
from google.adk.agents import Agent

BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "idea_reviewer.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    instructions = f.read()


idea_reviewer = Agent(
    name="idea_reviewer",
    model="gemini-2.0-flash",
    description="Evaluates suggested ideas, ranking them based on feasibility, impact, and creativity.",
    instruction=instructions,
)
