# Floyd-Warshall demo

This module demonstrates the Floyd-Warshall all-pairs shortest path algorithm:

- Works on directed weighted graphs, including negative edge weights.
- Finds shortest paths between all pairs of vertices using dynamic programming.
- Detects reachable negative cycles (returns `None`).
- Time complexity: O(V³), Space complexity: O(V²).

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```
