# Algorithms

This directory contains small, focused algorithm examples.

## Modules

- `01-binary-search-demo`: search a sorted list with binary search.
- `02-bubble-sort-demo`: sort a list with bubble sort.
- `03-quick-sort-demo`: sort a list with recursive quick sort.
- `04-bfs-demo`: find the shortest path in an unweighted graph with BFS.
- `05-knapsack-demo`: compute the best 0/1 knapsack value with dynamic programming.
- `06-dfs-demo`: traverse a graph in depth-first order.
- `07-dijkstra-demo`: find the lowest-cost path in a weighted graph.
- `08-merge-sort-demo`: sort a list with divide-and-conquer merge sort.
- `09-topological-sort-demo`: produce a topological order of a DAG with Kahn's algorithm.

## With uv

```powershell
cd algorithms/01-binary-search-demo
uv sync
uv run python -m app.main
```

Repeat the same workflow inside any module directory.