from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_login_and_read_profile() -> None:
    response = client.post(
        "/token",
        json={"username": "demo", "password": "demo123"},
    )
    assert response.status_code == 200

    token = response.json()["access_token"]
    profile_response = client.get(
        "/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert profile_response.status_code == 200
    assert profile_response.json()["username"] == "demo"


def test_login_rejects_invalid_password() -> None:
    response = client.post(
        "/token",
        json={"username": "demo", "password": "wrong-password"},
    )
    assert response.status_code == 401
