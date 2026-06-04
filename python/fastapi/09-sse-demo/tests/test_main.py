from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_index_serves_eventsource_page() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "EventSource" in response.text
    assert "/events?count=5" in response.text


def test_events_stream_uses_sse_media_type() -> None:
    with client.stream("GET", "/events?count=2") as response:
        body = "".join(response.iter_text())

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/event-stream")
    assert ": connected" in body
    assert "event: tick" in body
    assert "'sequence': 1" in body
    assert "'sequence': 2" in body
    assert "event: complete" in body


def test_events_endpoint_validates_count() -> None:
    response = client.get("/events?count=0")

    assert response.status_code == 422


def test_health_reports_stream_defaults() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "default_event_count": 3,
        "max_event_count": 10,
    }