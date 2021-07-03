from fastapi.testclient import TestClient


def test_healthz(test_client: TestClient):
    response = test_client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == "healthy"
