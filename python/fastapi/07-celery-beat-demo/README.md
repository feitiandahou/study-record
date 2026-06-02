# Celery + Redis beat demo

Demonstrates a minimal **FastAPI + Celery + Redis + beat** workflow:

- `POST /tasks/multiply`: enqueue a worker task.
- `GET /tasks/{task_id}`: inspect task state and result.
- `GET /heartbeats`: read periodic heartbeat records written by Celery beat.
- `DELETE /heartbeats`: clear stored heartbeat records for the next demo run.
- `GET /health`: inspect broker, backend, and beat configuration.

## Key concepts

- Redis acts as both the Celery broker and result backend.
- Celery worker executes ad-hoc tasks from API requests.
- Celery beat publishes scheduled tasks on a fixed interval.
- A shared store lets the API observe data produced by the worker.
- Tests switch to eager mode and an in-memory store so they stay self-contained.

## Run with Redis

Start Redis locally first, then open three terminals in this folder.

Terminal 1, worker:

```powershell
uv sync
uv run celery -A app.celery_app:celery_app worker --loglevel=info --pool=solo
```

Terminal 2, beat scheduler:

```powershell
uv run celery -A app.celery_app:celery_app beat --loglevel=info
```

Terminal 3, FastAPI:

```powershell
uv run uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs`, call `DELETE /heartbeats`, wait about 10 seconds, then call `GET /heartbeats` to confirm that beat is publishing the periodic job.

## Environment variables

```powershell
$env:CELERY_BROKER_URL = "redis://localhost:6379/0"
$env:CELERY_RESULT_BACKEND = "redis://localhost:6379/1"
$env:APP_STATE_REDIS_URL = "redis://localhost:6379/2"
$env:CELERY_HEARTBEAT_SECONDS = "10"
```

The defaults already point at these Redis databases, so you only need the variables when you want different endpoints.

## Test

```powershell
uv sync
uv run pytest
```
