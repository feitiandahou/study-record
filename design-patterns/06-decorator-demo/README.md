# Decorator demo

This module demonstrates a minimal Decorator pattern in Python:

- `Notifier`: the component interface used by the reminder workflow.
- `EmailNotifier`: the concrete component with the base delivery behavior.
- `SmsDecorator` and `AuditDecorator`: wrap another notifier to add extra behavior.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```