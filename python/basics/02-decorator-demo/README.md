# decorator demo

This module demonstrates what a decorator does:

- it receives a function
- returns a new wrapped function
- adds behavior before and after the original function call

## Run

```powershell
uv sync
uv run python -m app.main
```

The script shows call logging and preserves the wrapped function name.

## Test

```powershell
uv run pytest
```
