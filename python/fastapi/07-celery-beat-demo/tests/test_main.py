from fastapi.testclient import TestClient

from app.main import app
from app.tasks import record_heartbeat

client = TestClient(app)


def test_queue_multiply_task_returns_success_result_in_eager_mode() -> None:
    response = client.post("/tasks/multiply", json={"a": 6, "b": 7})

    assert response.status_code == 202
    payload = response.json()
    assert payload["task_id"]
    assert payload["state"] == "SUCCESS"

    task_response = client.get(f"/tasks/{payload['task_id']}")
    assert task_response.status_code == 200
    assert task_response.json()["result"]["product"] == 42


def test_manual_and_periodic_heartbeat_share_same_store_shape() -> None:
    client.post("/tasks/heartbeat")
    record_heartbeat.delay("beat")

    response = client.get("/heartbeats")
    assert response.status_code == 200
    payload = response.json()
    assert payload["count"] == 2
    assert [item["source"] for item in payload["items"]] == ["manual", "beat"]


def test_delete_heartbeats_clears_records() -> None:
    client.post("/tasks/heartbeat")

    delete_response = client.delete("/heartbeats")
    assert delete_response.status_code == 200
    assert delete_response.json()["cleared"] == 1

    list_response = client.get("/heartbeats")
    assert list_response.json()["count"] == 0


def test_health_reports_beat_configuration() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["always_eager"] is True
    assert payload["heartbeat_seconds"] == 10.0
    assert payload["state_backend"] == "memory"
