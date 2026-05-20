# exception handling demo

This module demonstrates `try`, `except`, and `finally`:

- normal results can be returned from `try`
- expected errors can be converted into safe messages
- cleanup logic belongs in `finally`

## Run

```powershell
uv sync
uv run python -m app.main
```

The script prints a successful division and an error case.

## Test

```powershell
uv run pytest
```