# content_generator/sub_agents/humanization_refiner/agent.py
from google.adk.agents import Agent
from tools.tools import exit_loop

humanization_refiner = Agent(
    name="humanization_refiner",
    model="gemini-2.0-flash",
    description="Polishes caption based on humanization feedback or exits loop when PASS",
    instruction="""
    You receive:
      - caption text in state['caption']
      - humanization feedback in state['humanization_result']

    Task:
      - If humanization_result is exactly "PASS": call the 'exit_loop' tool (do not output).
      - Otherwise, apply the reviewer feedback to produce a more natural, on-brand caption.
        Output only the revised caption text.

    Do not output anything when calling the tool. Otherwise output only the caption text.
    """,
    tools=[exit_loop],
    output_key="caption"   # overwrite caption with refined version
)
