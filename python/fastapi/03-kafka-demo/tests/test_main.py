from fastapi.testclient import TestClient

from app.main import app


def test_health_reports_memory_backend() -> None:
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok", "backend": "memory"}


def test_publish_event_is_recorded_in_history() -> None:
    with TestClient(app) as client:
        publish_response = client.post(
            "/events",
            json={
                "key": "order-1",
                "payload": {"event": "order.created", "amount": 99},
            },
        )
        assert publish_response.status_code == 200
        assert publish_response.json()["backend"] == "memory"

        events_response = client.get("/events")
        assert events_response.status_code == 200
        assert events_response.json() == [
            {
                "topic": "study-record.demo",
                "key": "order-1",
                "payload": {"event": "order.created", "amount": 99},
                "source": "memory",
                "offset": 1,
            }
        ]


def test_runtime_config_exposes_topic_settings() -> None:
    with TestClient(app) as client:
        response = client.get("/config")
        assert response.status_code == 200
        assert response.json()["topic"] == "study-record.demo"
        assert response.json()["history_limit"] == 20