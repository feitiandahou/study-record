# Kruskal demo

This module demonstrates Kruskal's algorithm for minimum spanning tree (MST):

- Sort edges by weight in ascending order.
- Greedily add an edge only if it does not form a cycle.
- Use Union-Find to detect cycles efficiently.
- If all nodes can be connected, the result is an MST with `|V|-1` edges.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```
