import pytest
from fastapi.testclient import TestClient

from app.main import _task_log, app

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_task_log() -> None:
    """Reset shared state between tests."""
    _task_log.clear()


def test_send_email_returns_202() -> None:
    response = client.post(
        "/send-email",
        json={"to": "user@example.com", "subject": "Hello", "body": "World"},
    )
    assert response.status_code == 202
    data = response.json()
    assert data["status"] == "queued"
    assert "task_id" in data


def test_background_task_completes() -> None:
    # TestClient executes background tasks synchronously before returning,
    # so the status should already be "sent" by the time we call GET /tasks.
    client.post(
        "/send-email",
        json={"to": "a@b.com", "subject": "Subject", "body": "Body"},
    )
    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["status"] == "sent"
    assert tasks[0]["completed_at"] is not None


def test_multiple_tasks_are_tracked() -> None:
    for i in range(3):
        client.post(
            "/send-email",
            json={"to": f"user{i}@example.com", "subject": f"Msg {i}", "body": "..."},
        )
    response = client.get("/tasks")
    assert len(response.json()) == 3


def test_health() -> None:
    assert client.get("/health").status_code == 200
