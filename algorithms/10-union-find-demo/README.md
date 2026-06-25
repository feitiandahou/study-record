# Union-Find demo

This module demonstrates a minimal Union-Find (Disjoint Set Union, DSU) implementation in Python:

- `find(x)` returns the representative (root) of the set containing `x`.
- `union(a, b)` merges two sets efficiently.
- Path compression and union by rank keep operations nearly constant in practice.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```
