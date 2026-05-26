import time
from typing import Dict, Any


def generate_instagram_post(
    topic: str,
    tone: str = "engaging",
    include_hashtags: bool = True,
    ) -> Dict[str, Any]:
    """
    Generate an Instagram-ready social media post.

    ```
    This tool creates:
    - Instagram captions
    - Engagement hooks
    - Emoji-enhanced formatting
    - Relevant hashtags

    Args:
        topic (str):
            Main topic or product description.

        tone (str):
            Writing tone.

            Examples:
            - engaging
            - professional
            - funny
            - luxury
            - casual

        include_hashtags (bool):
            Whether to include hashtags.

    Returns:
        Dict[str, Any]:
            Structured ADK-compatible response.

            Example:
            {
                "result": {
                    "caption": "...",
                    "hashtags": [...]
                },
                "stats": {...},
                "additional_info": {...}
            }
    """

    try:
        caption = (
            f"✨ {topic} ✨\n\n"
            f"Transform your workflow today 🚀\n"
            f"Experience innovation like never before."
        )

        hashtags = [
            "#AI",
            "#Automation",
            "#Innovation",
            "#Tech",
            "#Future",
        ] if include_hashtags else []

        return {
            "result": {
                "platform": "instagram",
                "caption": caption,
                "hashtags": hashtags,
                "post_type": "feed_post",
            },
            "stats": {
                "success": True,
                "caption_length": len(caption),
                "hashtag_count": len(hashtags),
            },
            "additional_info": {
                "tone": tone,
                "generated_at": time.time(),
                "tool_name": "generate_instagram_post",
            },
        }

    except Exception as e:
        return {
            "result": {
                "error": str(e)
            },
            "stats": {
                "success": False
            },
            "additional_info": {
                "error_type": type(e).__name__
            },
        }
