from src.agent.logic import build_response


def test_build_response_returns_dict() -> None:
    result = build_response("Tell me about Mars")
    assert isinstance(result, dict)
    assert result["prompt"] == "Tell me about Mars"
    assert "response" in result
