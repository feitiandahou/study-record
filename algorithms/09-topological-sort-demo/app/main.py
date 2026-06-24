from collections import deque


def topological_sort(graph: dict[str, list[str]]) -> list[str] | None:
    """Return a topological order of *graph*, or None if a cycle is detected.

    *graph* is an adjacency list mapping each node to its direct successors.
    Every node that appears as a successor must also be a key in the dict.
    """
    in_degree: dict[str, int] = {node: 0 for node in graph}
    for neighbours in graph.values():
        for neighbour in neighbours:
            in_degree[neighbour] += 1

    queue: deque[str] = deque(node for node, deg in in_degree.items() if deg == 0)
    order: list[str] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph[node]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    if len(order) != len(graph):
        return None  # cycle detected

    return order


def main() -> None:
    # Task dependency graph: A and B must precede C; C must precede D and E.
    graph = {
        "A": ["C"],
        "B": ["C"],
        "C": ["D", "E"],
        "D": [],
        "E": [],
    }
    result = topological_sort(graph)
    print(f"graph={graph}")
    print(f"topological order={result}")


if __name__ == "__main__":
    main()
