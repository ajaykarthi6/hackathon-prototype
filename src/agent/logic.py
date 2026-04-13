from typing import Any

from src.agent.prompts import DEFAULT_PROMPT


def build_response(prompt: str) -> dict[str, Any]:
    """Build a placeholder response for the interstellar agent."""
    return {
        "prompt": prompt,
        "prompt_template": DEFAULT_PROMPT,
        "response": "This is a placeholder response from the interstellar agent.",
    }
