# iterator demo

This module demonstrates custom iterators:

- the iterator keeps internal state
- `__iter__` returns the iterator object
- `__next__` produces values until `StopIteration`

## Run

```powershell
uv sync
uv run python -m app.main
```

The script prints a countdown sequence.

## Test

```powershell
uv run pytest
```