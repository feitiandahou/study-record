# State demo

This module demonstrates a minimal State pattern in Python:

- `PublishingWorkflow`: the context that delegates behavior to the current state.
- `DraftState`, `ReviewState`, and `PublishedState`: encapsulate transition rules.
- Each state decides what the next valid action is without long conditional chains in the context.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```