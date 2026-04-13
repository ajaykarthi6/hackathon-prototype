from typing import Any

from src.agent.prompts import DEFAULT_PROMPT


def build_response(prompt: str) -> dict[str, Any]:
    """Build a response for the interstellar agent."""
    lower_prompt = prompt.lower()
    if "mars" in lower_prompt:
        return {
            "planet": "Mars",
            "summary": "Mars, often called the 'Red Planet', is the fourth planet from the Sun...",
            "metrics": {
                "diameter_km": 6779,
                "surface_gravity": "1/3 of Earth",
                "temperature_range_celsius": {"min": -153, "max": 20},
            },
            "features": ["Olympus Mons", "Valles Marineris"],
            "moons": ["Phobos", "Deimos"],
            "prompt": prompt,
            "prompt_template": DEFAULT_PROMPT,
        }

    return {
        "prompt": prompt,
        "prompt_template": DEFAULT_PROMPT,
        "response": "This is a placeholder response from the interstellar agent.",
    }
