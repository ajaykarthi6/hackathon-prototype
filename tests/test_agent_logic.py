from src.agent.logic import build_response


def test_build_response_returns_dict() -> None:
    result = build_response("Tell me about Mars")
    assert isinstance(result, dict)
    assert result["prompt"] == "Tell me about Mars"
    assert result["planet"] == "Mars"
    assert result["metrics"]["diameter_km"] == 6779


def test_build_response_venus() -> None:
    result = build_response("What about Venus?")
    assert result["planet"] == "Venus"
    assert "Volcanic plains" in result["features"]


def test_build_response_jupiter() -> None:
    result = build_response("Tell me about Jupiter")
    assert result["planet"] == "Jupiter"
    assert "Great Red Spot" in result["features"]


def test_build_response_unknown() -> None:
    result = build_response("Tell me about Pluto")
    assert "response" in result
    assert "planetary education" in result["response"]
