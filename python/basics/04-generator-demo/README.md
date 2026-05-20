# generator demo

This module demonstrates generators:

- values are produced one by one with `yield`
- generators avoid building the full result list up front
- they can be consumed like any iterable

## Run

```powershell
uv sync
uv run python -m app.main
```

The script prints generated even numbers and their sum.

## Test

```powershell
uv run pytest
```