import os
from google.adk.agents import Agent

BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "theme_refiner.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    instructions = f.read()

theme_refiner = Agent(
    name="theme_refiner",
    model="gemini-2.0-flash",
    description="Refines the hackathon theme into a clearer, more structured form for better understanding.",
    instruction=instructions,
)


if __name__ == "__main__":
    user_input = "Make a theme about sustainability and AI"
    response = theme_refiner.run(user_input, instructions=instructions)
    print(response)