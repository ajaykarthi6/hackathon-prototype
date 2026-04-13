from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_query_endpoint_returns_expected_structure() -> None:
    response = client.post("/query", json={"prompt": "Tell me about Mars"})
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "success"
    data = payload["data"]
    assert data["planet"] == "Mars"
    assert data["summary"].startswith("Mars, often called")
    assert data["metrics"]["diameter_km"] == 6779
