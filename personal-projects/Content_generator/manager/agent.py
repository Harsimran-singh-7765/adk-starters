# content_generator/manager/agent.py
from google.adk.agents import SequentialAgent, LoopAgent
from sub_agents.draft_writer.agent import draft_writer
from sub_agents.freshness_checker.agent import freshness_checker
from sub_agents.draft_refiner.agent import draft_refiner
from sub_agents.emotional_polisher.agent import emotional_polisher
from sub_agents.humanization_reviewer.agent import humanization_reviewer
from sub_agents.humanization_refiner.agent import humanization_refiner

# Root Sequential workflow: DraftLoop -> Emotional Polisher -> HumanizationLoop
# Note: SequentialAgent and LoopAgent should NOT include `instruction` (ADK schema).
root_agent = SequentialAgent(
    name="content_manager",
    description="Manager agent for Instagram content creation with loops for quality control",

    sub_agents=[
        # Draft loop: writer -> freshness check -> refiner (refiner calls exit_loop on PASS)
        LoopAgent(
            name="DraftLoop",
            description="Loop between draft_writer, freshness_checker and draft_refiner until PASS or max iterations.",
            sub_agents=[draft_writer, freshness_checker, draft_refiner],
            max_iterations=10
        ),
        # Emotional polish runs once on the accepted draft (or on the last refined caption)
        emotional_polisher,
        # Humanization loop: reviewer -> refiner (refiner calls exit_loop on PASS)
        LoopAgent(
            name="HumanizationLoop",
            description="Loop between humanization_reviewer and humanization_refiner until PASS or max iterations.",
            sub_agents=[humanization_reviewer, humanization_refiner],
            max_iterations=10
        )
    ],
)