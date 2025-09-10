import os
from google.adk.agents import Agent

BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "pitch.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    instructions = f.read()

pitch_agent = Agent(
    name="pitch_agent",
    model="gemini-2.0-flash",
    description="Prepares the pitch script and content for presenting the hackathon project.",
    instruction=instructions,
)
