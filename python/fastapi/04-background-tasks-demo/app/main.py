import time
from datetime import UTC, datetime

from fastapi import BackgroundTasks, FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Background Tasks Demo", version="0.1.0")

# In-memory store – good enough for a demo; not thread-safe at scale.
_task_log: list[dict] = []


# ---------------------------------------------------------------------------
# Schemas
# ---------------------------------------------------------------------------


class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str


class TaskRecord(BaseModel):
    id: int
    to: str
    subject: str
    queued_at: str
    completed_at: str | None
    status: str  # "queued" | "sent"


# ---------------------------------------------------------------------------
# Background worker
# ---------------------------------------------------------------------------


def _send_email(task_id: int, to: str, subject: str, body: str) -> None:
    """Simulate sending an email (sync I/O placeholder).

    FastAPI runs sync background functions in a thread-pool executor so the
    event loop is never blocked.
    """
    time.sleep(0.05)  # simulate SMTP latency

    for record in _task_log:
        if record["id"] == task_id:
            record["status"] = "sent"
            record["completed_at"] = datetime.now(UTC).isoformat()
            break


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.post("/send-email", status_code=202)
def send_email(request: EmailRequest, background_tasks: BackgroundTasks) -> dict:
    """Accept an email request, queue it, and return 202 immediately."""
    task_id = len(_task_log) + 1
    record: dict = {
        "id": task_id,
        "to": request.to,
        "subject": request.subject,
        "queued_at": datetime.now(UTC).isoformat(),
        "completed_at": None,
        "status": "queued",
    }
    _task_log.append(record)
    background_tasks.add_task(_send_email, task_id, request.to, request.subject, request.body)
    return {"task_id": task_id, "status": "queued"}


@app.get("/tasks", response_model=list[TaskRecord])
def list_tasks() -> list[dict]:
    """Return all task records."""
    return _task_log


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
