from fastapi.testclient import TestClient

from app.celery_app import celery_app
from app.main import app

client = TestClient(app)


def setup_module() -> None:
    celery_app.conf.task_always_eager = True
    celery_app.conf.task_store_eager_result = True
    celery_app.conf.broker_url = "memory://"
    celery_app.conf.result_backend = "cache+memory://"
    celery_app.loader.import_default_modules()


def teardown_module() -> None:
    celery_app.conf.task_always_eager = False


def test_queue_add_task_returns_task_id() -> None:
    response = client.post("/tasks/add", json={"a": 4, "b": 5, "delay_seconds": 0})

    assert response.status_code == 202
    payload = response.json()
    assert payload["task_id"]
    assert payload["state"] == "SUCCESS"


def test_get_task_status_returns_result() -> None:
    queued = client.post("/tasks/add", json={"a": 7, "b": 8, "delay_seconds": 0}).json()

    response = client.get(f"/tasks/{queued['task_id']}")
    assert response.status_code == 200

    payload = response.json()
    assert payload["ready"] is True
    assert payload["successful"] is True
    assert payload["state"] == "SUCCESS"
    assert payload["result"]["total"] == 15


def test_health_endpoint_reports_mode() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["always_eager"] is True
