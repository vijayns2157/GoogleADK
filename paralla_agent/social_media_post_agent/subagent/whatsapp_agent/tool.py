import time
from typing import Dict, Any

def generate_whatsapp_campaign_message(
    topic: str,
    tone: str = "friendly",
    include_emoji: bool = True,
    ) -> Dict[str, Any]:
    """
    Generate a WhatsApp campaign or promotional message.

    ```
    This tool creates:
    - Short conversational messages
    - Promotional campaigns
    - Broadcast messages
    - Lead nurturing content

    Args:
        topic (str):
            Campaign topic or offer.

        tone (str):
            Desired communication style.

        include_emoji (bool):
            Whether to include emojis.

    Returns:
        Dict[str, Any]:
            Structured ADK-compatible response.
    """



    try:
        emoji = "🚀" if include_emoji else ""

        message = (
            f"{emoji} Exciting update about {topic}!\n\n"
            f"Discover smarter automation solutions today."
        )

        return {
            "result": {
                "platform": "whatsapp",
                "message": message,
                "message_type": "campaign",
            },
            "stats": {
                "success": True,
                "message_length": len(message),
            },
            "additional_info": {
                "tone": tone,
                "generated_at": time.time(),
                "tool_name": "generate_whatsapp_campaign_message",
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