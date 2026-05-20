# classmethod and staticmethod demo

This module demonstrates two method types:

- `@classmethod` works with the class itself
- `@staticmethod` is a utility function grouped inside the class
- both help model related behavior cleanly

## Run

```powershell
uv sync
uv run python -m app.main
```

The script prints temperature conversions.

## Test

```powershell
uv run pytest
```