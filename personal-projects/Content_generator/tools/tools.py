# content_generator/tools/tools.py
from google.adk.tools.tool_context import ToolContext

def exit_loop(tool_context: ToolContext):
    """
    Tool to exit a LoopAgent early.
    Call this tool when a sub-agent determines the loop should stop.
    """
    print(f"[exit_loop] Triggered by {tool_context.agent_name}")
    # escalate tells the runner/loop agent to stop the loop early
    tool_context.actions.escalate = True
    return {}
