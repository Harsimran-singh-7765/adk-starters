import os
from google.adk.agents import Agent

BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "ppt.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    instructions = f.read()


ppt_agent = Agent(
    name="ppt_agent",
    model="gemini-2.0-flash",
    description="Generates PPT slide content for the hackathon pitch deck.",
    instruction=instructions,
)
