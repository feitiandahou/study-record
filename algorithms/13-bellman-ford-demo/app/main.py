Edge = tuple[str, str, int]


def bellman_ford(
    nodes: list[str], edges: list[Edge], source: str
) -> dict[str, float] | None:
    distances: dict[str, float] = {node: float("inf") for node in nodes}

    if source not in distances:
        return None

    distances[source] = 0

    for _ in range(len(nodes) - 1):
        updated = False

        for u, v, w in edges:
            if distances[u] == float("inf"):
                continue

            candidate = distances[u] + w
            if candidate < distances[v]:
                distances[v] = candidate
                updated = True

        if not updated:
            break

    for u, v, w in edges:
        if distances[u] != float("inf") and distances[u] + w < distances[v]:
            return None

    return distances


def main() -> None:
    nodes = ["A", "B", "C", "D"]
    edges: list[Edge] = [
        ("A", "B", 4),
        ("A", "C", 5),
        ("B", "C", -2),
        ("C", "D", 3),
        ("B", "D", 6),
    ]

    distances = bellman_ford(nodes, edges, source="A")
    print(f"nodes={nodes}")
    print(f"edges={edges}")
    print(f"distances={distances}")


if __name__ == "__main__":
    main()
