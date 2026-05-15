import datetime
from google.adk.agents import Agent

def get_datetime() -> dict:
    """
    Get the current Date and time in the format YYYY-MM-DD and HH:MM:SS.
    """
    return {
        "Current_datetime": datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S"),
    }
    
    
root_agent = Agent(
    name="tool_agent",
    model="gemini-3-flash-preview",
    description="Agent with tools to provide current date and time.",
    instruction="""
    You are a helpful AI agent with that use the following tool to fetch the current date and time:
    - get_datetime
    """,
    tools=[get_datetime]
)