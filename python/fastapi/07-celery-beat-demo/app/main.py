from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.celery_app import celery_app, heartbeat_seconds
from app.store import clear_heartbeats, list_heartbeats, state_backend_name
from app.tasks import multiply_numbers, record_heartbeat

app = FastAPI(title="Celery Beat Demo", version="0.1.0")


class MultiplyTaskRequest(BaseModel):
    a: int = Field(description="First factor")
    b: int = Field(description="Second factor")


class TaskQueuedResponse(BaseModel):
    task_id: str
    state: str


class TaskStatusResponse(BaseModel):
    task_id: str
    state: str
    ready: bool
    successful: bool
    result: dict[str, Any] | None = None
    error: str | None = None


class HeartbeatRecord(BaseModel):
    source: str
    recorded_at: str


class HeartbeatListResponse(BaseModel):
    count: int
    items: list[HeartbeatRecord]


@app.post("/tasks/multiply", response_model=TaskQueuedResponse, status_code=202)
def queue_multiply_task(request: MultiplyTaskRequest) -> TaskQueuedResponse:
    task = multiply_numbers.delay(request.a, request.b)
    return TaskQueuedResponse(task_id=task.id, state=task.state)


@app.post("/tasks/heartbeat", response_model=TaskQueuedResponse, status_code=202)
def queue_manual_heartbeat() -> TaskQueuedResponse:
    task = record_heartbeat.delay("manual")
    return TaskQueuedResponse(task_id=task.id, state=task.state)


@app.get("/tasks/{task_id}", response_model=TaskStatusResponse)
def get_task_status(task_id: str) -> TaskStatusResponse:
    task_result = celery_app.AsyncResult(task_id)
    error = None
    result_payload = None

    if task_result.successful():
        raw_result = task_result.result
        result_payload = raw_result if isinstance(raw_result, dict) else {"value": raw_result}
    elif task_result.failed():
        error = str(task_result.result)

    return TaskStatusResponse(
        task_id=task_id,
        state=task_result.state,
        ready=task_result.ready(),
        successful=task_result.successful(),
        result=result_payload,
        error=error,
    )


@app.get("/heartbeats", response_model=HeartbeatListResponse)
def get_heartbeats() -> HeartbeatListResponse:
    items = [HeartbeatRecord(**entry) for entry in list_heartbeats()]
    return HeartbeatListResponse(count=len(items), items=items)


@app.delete("/heartbeats")
def delete_heartbeats() -> dict[str, int]:
    return {"cleared": clear_heartbeats()}


@app.get("/health")
def healthcheck() -> dict[str, str | bool | float]:
    return {
        "status": "ok",
        "broker": str(celery_app.conf.broker_url),
        "backend": str(celery_app.conf.result_backend),
        "state_backend": state_backend_name(),
        "always_eager": celery_app.conf.task_always_eager,
        "heartbeat_seconds": heartbeat_seconds,
    }
