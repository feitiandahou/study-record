"""Floyd-Warshall algorithm for all-pairs shortest paths."""

Edge = tuple[str, str, int]


def floyd_warshall(
    nodes: list[str], edges: list[Edge]
) -> dict[str, dict[str, float]] | None:
    """
    Compute shortest paths between all pairs of vertices.

    Args:
        nodes: List of vertex labels.
        edges: List of (source, dest, weight) tuples.

    Returns:
        Distance matrix as nested dicts, or None if a negative cycle is detected.
    """
    # Initialize distance matrix
    dist: dict[str, dict[str, float]] = {}
    for u in nodes:
        dist[u] = {}
        for v in nodes:
            if u == v:
                dist[u][v] = 0
            else:
                dist[u][v] = float("inf")

    # Fill in known edges
    for u, v, w in edges:
        if u not in dist or v not in dist:
            return None  # Edge references unknown node
        dist[u][v] = min(dist[u][v], w)  # Handle duplicate edges

    # Floyd-Warshall DP: relax via intermediate vertex k
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Check for negative cycles
    for u in nodes:
        if dist[u][u] < 0:
            return None

    return dist


def main() -> None:
    """Demonstrate Floyd-Warshall algorithm."""
    nodes = ["A", "B", "C", "D"]
    edges: list[Edge] = [
        ("A", "B", 4),
        ("A", "C", 5),
        ("B", "C", -2),
        ("C", "D", 3),
        ("B", "D", 6),
    ]

    dist = floyd_warshall(nodes, edges)
    print(f"nodes={nodes}")
    print(f"edges={edges}")
    print(f"distances={dist}")

    if dist:
        print("\nPairwise distances:")
        for u in nodes:
            for v in nodes:
                d = dist[u][v]
                print(f"  {u}->{v}: {d if d != float('inf') else 'inf'}")


if __name__ == "__main__":
    main()
