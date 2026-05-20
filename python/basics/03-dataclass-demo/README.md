# dataclass demo

This module demonstrates why `dataclass` is useful:

- it reduces boilerplate for data containers
- supports default values and default factories
- makes object creation and debugging straightforward

## Run

```powershell
uv sync
uv run python -m app.main
```

The script prints a simple user profile summary.

## Test

```powershell
uv run pytest
```