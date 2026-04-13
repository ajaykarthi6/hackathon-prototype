from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_query_endpoint_returns_expected_structure() -> None:
    response = client.post("/query", json={"prompt": "Tell me about Mars"})
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["prompt"] == "Tell me about Mars"
    assert "response" in data
