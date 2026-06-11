import heapq


def shortest_path(
    graph: dict[str, dict[str, int]], start: str, target: str
) -> tuple[int | None, list[str]]:
    if start not in graph or target not in graph:
        return None, []

    distances = {node: float("inf") for node in graph}
    previous: dict[str, str | None] = {node: None for node in graph}
    distances[start] = 0
    heap: list[tuple[int, str]] = [(0, start)]

    while heap:
        current_distance, node = heapq.heappop(heap)
        if current_distance > distances[node]:
            continue

        if node == target:
            break

        for neighbor, weight in graph[node].items():
            next_distance = current_distance + weight
            if next_distance >= distances[neighbor]:
                continue

            distances[neighbor] = next_distance
            previous[neighbor] = node
            heapq.heappush(heap, (next_distance, neighbor))

    if distances[target] == float("inf"):
        return None, []

    path: list[str] = []
    cursor: str | None = target
    while cursor is not None:
        path.append(cursor)
        cursor = previous[cursor]

    path.reverse()
    return int(distances[target]), path


def main() -> None:
    graph = {
        "A": {"B": 4, "C": 1},
        "B": {"D": 1},
        "C": {"B": 2, "D": 5},
        "D": {},
    }
    distance, path = shortest_path(graph, "A", "D")
    print(f"graph={graph}")
    print(f"distance={distance}, path={path}")


if __name__ == "__main__":
    main()