from datetime import datetime

from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


root_agent = Agent(
    model='gemini-2.5-flash-preview-09-2025',
    name='tool_agent',
    description="tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - get_current_time
    """,
    # tools=[google_search],
    tools=[get_current_time]
)
