from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.celery_app import celery_app
from app.tasks import add_numbers

app = FastAPI(title="Celery Demo", version="0.1.0")


class AddTaskRequest(BaseModel):
    a: int = Field(description="First addend")
    b: int = Field(description="Second addend")
    delay_seconds: float = Field(default=0.0, ge=0.0, le=10.0)


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


@app.post("/tasks/add", response_model=TaskQueuedResponse, status_code=202)
def queue_add_task(request: AddTaskRequest) -> TaskQueuedResponse:
    task = add_numbers.delay(request.a, request.b, request.delay_seconds)
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


@app.get("/health")
def healthcheck() -> dict[str, str | bool]:
    return {
        "status": "ok",
        "broker": str(celery_app.conf.broker_url),
        "backend": str(celery_app.conf.result_backend),
        "always_eager": celery_app.conf.task_always_eager,
    }
