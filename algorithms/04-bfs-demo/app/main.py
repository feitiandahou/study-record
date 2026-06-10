from collections import deque


def shortest_path(
    graph: dict[str, list[str]], start: str, target: str
) -> list[str]:
    if start == target:
        return [start]

    queue: deque[tuple[str, list[str]]] = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor in visited:
                continue

            next_path = path + [neighbor]
            if neighbor == target:
                return next_path

            visited.add(neighbor)
            queue.append((neighbor, next_path))

    return []


def main() -> None:
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["E"],
        "D": ["F"],
        "E": ["F"],
        "F": [],
    }
    path = shortest_path(graph, "A", "F")
    print(f"graph={graph}")
    print(f"path={path}")


if __name__ == "__main__":
    main()