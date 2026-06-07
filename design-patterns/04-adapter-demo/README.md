# Adapter demo

This module demonstrates a minimal Adapter pattern in Python:

- `AlertSender`: the target interface used by the incident workflow.
- `SlackSender`: a native implementation that already matches the interface.
- `SmsSenderAdapter`: wraps a legacy SMS gateway with a different method name.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```
