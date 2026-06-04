# SSE demo

Demonstrates a minimal **FastAPI Server-Sent Events** workflow:

- `GET /`: tiny browser client that subscribes with `EventSource`.
- `GET /events`: stream a short sequence of SSE messages.
- `GET /health`: inspect app health and default stream settings.

## Key concepts

- SSE uses plain HTTP with `text/event-stream`, unlike a WebSocket upgrade.
- `StreamingResponse` can emit protocol-formatted event chunks from a generator.
- Browser `EventSource` is ideal for one-way server-to-client updates.
- Tests can read only the first few chunks to validate the stream shape.

## Run

```powershell
uv sync
uv run uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`, then watch incoming events in the page.

## Test

```powershell
uv run pytest
```