from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="google_search_agent",
    model="gemini-3-flash-preview",
    description="Search Agent with Goodgle Search tool.",
    instruction="""
    You are a helpful AI agent, who provide a search result using following search tool:
    - google_search
    """,
    tools=[google_search]
       
)