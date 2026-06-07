# Command demo

This module demonstrates a minimal Command pattern in Python:

- `TextEditor`: the receiver that performs document changes.
- `AppendTextCommand` and `ReplaceTextCommand`: encapsulate editor operations.
- `EditorInvoker`: triggers commands and supports undo for the last action.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```
