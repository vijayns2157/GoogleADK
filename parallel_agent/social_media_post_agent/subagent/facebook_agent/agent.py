from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import LlmAgent
import os
from .tool import generate_facebook_post

# model = LiteLlm(
#     model="groq/openai/gpt-oss-120b",
#     # model="llama-3.1-8b-instant",
#     # api_key=os.getenv("OPENROUTER_API_KEY"),
#         api_key=os.getenv("GROQ_API_KEY"),
# )

GEMINI_MODEL = "gemini-2.5-flash-lite"

facebook_agent = LlmAgent(
    name="facebook_agent",
    model=GEMINI_MODEL,
    description="""
    Specialized Facebook content generation agent.
    """,
    instruction="""
    You are a Facebook marketing expert.

    Responsibilities:
    - Generate engaging Facebook posts
    - Create long-form social media content
    - Optimize engagement and readability
    - Include CTAs when relevant
    - Maintain brand tone consistency

    Focus Areas:
    - Marketing campaigns
    - Product promotions
    - Community engagement
    - Educational posts
    """,
    tools=[generate_facebook_post],
    output_key="facebook_post",  
)

