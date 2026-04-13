from typing import Any

from src.agent.prompts import DEFAULT_PROMPT

# Planetary data for dynamic responses
PLANET_DATA = {
    "mars": {
        "planet": "Mars",
        "summary": "Mars, often called the 'Red Planet', is the fourth planet from the Sun...",
        "metrics": {
            "diameter_km": 6779,
            "surface_gravity": "1/3 of Earth",
            "temperature_range_celsius": {"min": -153, "max": 20},
        },
        "features": ["Olympus Mons", "Valles Marineris"],
        "moons": ["Phobos", "Deimos"],
    },
    "venus": {
        "planet": "Venus",
        "summary": "Venus is the second planet from the Sun and is Earth's closest planetary neighbor...",
        "metrics": {
            "diameter_km": 12104,
            "surface_gravity": "0.9 of Earth",
            "temperature_range_celsius": {"min": 450, "max": 470},
        },
        "features": ["Volcanic plains", "Thick atmosphere"],
        "moons": [],
    },
    "jupiter": {
        "planet": "Jupiter",
        "summary": "Jupiter is the largest planet in our solar system...",
        "metrics": {
            "diameter_km": 142984,
            "surface_gravity": "2.4 of Earth",
            "temperature_range_celsius": {"min": -145, "max": -108},
        },
        "features": ["Great Red Spot", "Gas giant"],
        "moons": ["Io", "Europa", "Ganymede", "Callisto"],
    },
}


def build_response(prompt: str) -> dict[str, Any]:
    """Build a response for the interstellar agent."""
    lower_prompt = prompt.lower()
    for planet_key, data in PLANET_DATA.items():
        if planet_key in lower_prompt:
            return {
                **data,
                "prompt": prompt,
                "prompt_template": DEFAULT_PROMPT,
            }

    return {
        "prompt": prompt,
        "prompt_template": DEFAULT_PROMPT,
        "response": "I'm an interstellar agent specializing in planetary education. Ask me about Mars, Venus, or Jupiter!",
    }

