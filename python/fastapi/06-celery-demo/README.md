# Celery demo

Demonstrates a minimal **FastAPI + Celery** workflow:

- `POST /tasks/add`: enqueue a background addition job.
- `GET /tasks/{task_id}`: query the task state and result.
- `GET /health`: inspect app health and current Celery mode.

## Key concepts

- Celery worker runs outside the FastAPI process, unlike `BackgroundTasks`.
- Broker moves messages from API to worker; result backend stores task output.
- `task_always_eager=true` is useful for tests and single-process demos.
- Query task status via `AsyncResult(task_id)`.

## Run with Redis

Start Redis locally first, then open two terminals in this folder.

Terminal 1:

```powershell
uv sync
uv run celery -A app.celery_app:celery_app worker --loglevel=info --pool=solo
```

Terminal 2:

```powershell
uv run uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` and submit `POST /tasks/add`.

## Run without Redis for a quick preview

This mode executes tasks eagerly inside the API process.

```powershell
$env:CELERY_BROKER_URL = "memory://"
$env:CELERY_RESULT_BACKEND = "cache+memory://"
$env:CELERY_TASK_ALWAYS_EAGER = "true"
uv sync
uv run uvicorn app.main:app --reload
```

## Test

```powershell
uv sync
uv run pytest
```
