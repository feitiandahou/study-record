# Observer demo

This module demonstrates a minimal Observer pattern in Python:

- `OrderTracker`: the subject that publishes order status changes.
- `EmailNotifier`: sends customer-facing updates.
- `WarehouseBoard`: updates an internal operations board.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```