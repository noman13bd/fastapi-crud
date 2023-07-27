from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health(test_app):
    response = test_app.get("/health")
    assert response.status_code == 204
