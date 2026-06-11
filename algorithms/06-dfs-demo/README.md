# Depth-first search demo

This module demonstrates a minimal depth-first traversal in Python:

- Visit nodes by exploring each branch as deep as possible first.
- Preserve neighbor order for deterministic traversal results.
- Return the reachable nodes from a given start node.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```