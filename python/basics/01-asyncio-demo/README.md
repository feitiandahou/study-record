# asyncio demo

This module demonstrates the core idea of `asyncio`:

- awaiting tasks one by one runs them sequentially
- `asyncio.gather()` can run independent coroutines concurrently

## Run

```powershell
uv sync
uv run python -m app.main
```

The script prints the sequential and concurrent results and durations.

## Test

```powershell
uv run pytest
```
