from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import LlmAgent
import os
from .tool import generate_instagram_post

# model = LiteLlm(
#     model="groq/openai/gpt-oss-120b",
#     # model="llama-3.1-8b-instant",
#     # api_key=os.getenv("OPENROUTER_API_KEY"),
#         api_key=os.getenv("GROQ_API_KEY"),
# )

GEMINI_MODEL = "gemini-2.5-flash-lite"

instagram_agent = LlmAgent(
    name="instagram_agent",
    model=GEMINI_MODEL,
    description="""
    Specialized Instagram content generation agent.
    """,
    instruction="""
    You are an Instagram growth expert.

    Responsibilities:
    - Generate viral captions
    - Create hashtag strategies
    - Optimize engagement
    - Create trendy content
    - Improve discoverability

    Focus Areas:
    - Reels
    - Stories
    - Carousel posts
    - Influencer-style captions
    - Trend-based engagement
    """,
    tools=[generate_instagram_post],
    output_key="instagram_caption", 
)