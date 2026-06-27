# Bellman-Ford demo

This module demonstrates Bellman-Ford shortest path algorithm:

- Works on directed weighted graphs, including negative edge weights.
- Repeatedly relax all edges up to `|V|-1` times.
- Detects reachable negative cycles.
- Returns `None` when a negative cycle makes shortest paths undefined.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```
