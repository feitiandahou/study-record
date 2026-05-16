# WebSocket demo

This module demonstrates a minimal FastAPI WebSocket flow:

- `GET /`: a tiny browser client.
- `WS /ws`: connect, receive a welcome message, and echo text messages.

## Run

```powershell
uv sync
uv run uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000` in a browser, type a message, and watch the echo flow.

## Test

```powershell
uv run pytest
```
