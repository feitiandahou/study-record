# Topological Sort demo

This module demonstrates topological sort on a directed acyclic graph (DAG) using Kahn's algorithm:

- Compute the in-degree of every node.
- Enqueue all nodes with in-degree 0 (no dependencies).
- Repeatedly dequeue a node, emit it, and reduce the in-degree of its neighbours.
- If all nodes are emitted the graph is a DAG; otherwise it contains a cycle.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```
