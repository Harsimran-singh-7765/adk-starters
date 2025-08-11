# content_generator/sub_agents/draft_refiner/agent.py
from google.adk.agents import Agent
from tools.tools import exit_loop

draft_refiner = Agent(
    name="draft_refiner",
    model="gemini-2.0-flash",
    description="Refines the caption according to freshness feedback or exits loop when PASS",
    instruction="""
    You receive:
      - The current caption in state['caption'] (or last produced text)
      - The freshness feedback in state['freshness_result']

    Task:
      - If freshness_result is exactly "PASS": call the 'exit_loop' tool and do NOT output any text.
      - Otherwise, freshness_result contains "FAIL" and a short explanation: improve the caption to address that feedback.
        Output only the improved caption text (no extra commentary).

    Do not output anything when calling the tool. When returning a revised caption, output only the caption text.
    """,
    tools=[exit_loop],
    # Write back the refined caption into the shared 'caption' state
    output_key="caption"
)
