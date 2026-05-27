# Background Tasks demo

Demonstrates FastAPI's built-in `BackgroundTasks` — work that runs **after** the response
is already sent to the client, without a separate message queue.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/send-email` | Queue a simulated email and return `202` immediately |
| `GET`  | `/tasks`       | List all queued / sent task records |
| `GET`  | `/health`      | Health check |

## Key concepts

- `BackgroundTasks.add_task(fn, *args)` — registers a callable to run after response.
- Sync functions run in a thread-pool; `async def` functions run on the event loop.
- Ideal for fire-and-forget work (email, audit logs, cache invalidation).
- For heavy / distributed work prefer Kafka (see `03-kafka-demo`) or Celery.

## Run

```powershell
uv sync
uv run uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to test interactively.

## Test

```powershell
uv run pytest
```
