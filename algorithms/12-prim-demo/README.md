# Prim demo

This module demonstrates Prim's algorithm for minimum spanning tree (MST):

- Start from any node and expand the tree one edge at a time.
- Always choose the lowest-weight edge that connects the current tree to an unvisited node.
- Use a min-heap to efficiently pick the next best edge.
- If the graph is disconnected, a single MST does not exist.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```
