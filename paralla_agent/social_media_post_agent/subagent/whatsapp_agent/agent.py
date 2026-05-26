from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import LlmAgent
import os
from .tool import generate_whatsapp_campaign_message

# model = LiteLlm(
#     model="groq/openai/gpt-oss-120b",
#     # model="llama-3.1-8b-instant",
#     # api_key=os.getenv("OPENROUTER_API_KEY"),
#         api_key=os.getenv("GROQ_API_KEY"),
# )

GEMINI_MODEL = "gemini-2.5-flash-lite"

whatsapp_agent = LlmAgent(
    name="whatsapp_agent",
    model=GEMINI_MODEL,
    description="""
    Specialized WhatsApp communication agent.
    """,
    instruction="""
    You are a WhatsApp business communication expert.

    Responsibilities:
    - Generate conversational messages
    - Create broadcast campaigns
    - Improve customer engagement
    - Maintain concise communication
    - Create personalized messaging

    Focus Areas:
    - Promotions
    - Notifications
    - Customer support
    - Business onboarding
    - Campaign broadcasts
    """,
    tools=[generate_whatsapp_campaign_message],
    output_key="whatsapp_message", 
)