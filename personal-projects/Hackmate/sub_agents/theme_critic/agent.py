import os
from google.adk.agents import Agent

BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "theme_critic.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    instructions = f.read()

theme_critic = Agent(
    name="theme_critic",
    model="gemini-2.0-flash",
    description="Critically analyzes the refined theme, pointing out weaknesses or ambiguities.",
    instruction=instructions,
)
