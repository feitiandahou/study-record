# context manager demo

This module demonstrates context managers:

- setup code runs before `yield`
- cleanup code runs after the `with` block
- resource handling becomes predictable and readable

## Run

```powershell
uv sync
uv run python -m app.main
```

The script prints the order of setup, work, and cleanup events.

## Test

```powershell
uv run pytest
```