# Hackmate/manager/agent.py
import os
from google.adk.agents import SequentialAgent, LoopAgent,Agent

# === Import sub-agents ===
from sub_agents.theme_refiner.agent import theme_refiner
from sub_agents.theme_critic.agent import theme_critic
from sub_agents.theme_validator.agent import theme_validator
from sub_agents.idea_suggester.agent import idea_suggester
from sub_agents.idea_reviewer.agent import idea_reviewer
from sub_agents.roadmap.agent import roadmap_agent
from sub_agents.techspec.agent import techspec_agent
from sub_agents.pitch.agent import pitch_agent
from sub_agents.ppt.agent import ppt_agent
from sub_agents.validator.agent import validator_agent

# === Load manager instructions (optional) ===
BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "manager.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    manager_instructions = f.read()

## inshort file handle  
theme_collector = Agent(
    name="theme_collector",
    model="gemini-2.0-flash",
    description="Collects the initial hackathon theme from the user.",
    instruction="Ask the user for the hackathon theme and pass it to the next agents."
)
# === Root workflow ===
root_agent = SequentialAgent(
    name="Hack_Mate",
    description=manager_instructions,
    sub_agents=[
         theme_collector,
        # Step 1: Theme loop (refine → critic → validator, until validator says PASS)
        LoopAgent(
            name="ThemeLoop",
            description="Loop to refine, critique, and validate the hackathon theme.",
            sub_agents=[theme_refiner, theme_critic, theme_validator],
            max_iterations=1,
        ),

        # Step 2: Idea suggestion + review (straight sequence)
        SequentialAgent(
            name="IdeaStage",
            description="Suggest and evaluate project ideas.",
            sub_agents=[idea_suggester, idea_reviewer],
        ),

        # Step 3: Execution pipeline (roadmap → techspec → pitch → ppt → validator)
        SequentialAgent(
            name="ExecutionPipeline",
            description="Turns the chosen idea into a concrete hackathon project plan and pitch deck.",
            sub_agents=[
                roadmap_agent,
                techspec_agent,
                pitch_agent,
                ppt_agent,
                validator_agent,
            ],
        ),
    ],
)
