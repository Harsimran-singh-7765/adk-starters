import os
from google.adk.agents import Agent

BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "roadmap.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    instructions = f.read()


roadmap_agent = Agent(
    name="roadmap_agent",
    model="gemini-2.0-flash",
    description="Creates a step-by-step roadmap for building the selected hackathon project.",
    instruction=instructions,
)
