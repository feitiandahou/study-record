from heapq import heappop, heappush

Edge = tuple[str, str, int]
Graph = dict[str, list[tuple[str, int]]]


def prim_mst(graph: Graph, start: str | None = None) -> tuple[list[Edge], int] | None:
    if not graph:
        return [], 0

    if start is None:
        start = next(iter(graph))

    visited = {start}
    min_heap: list[tuple[int, str, str]] = []
    mst: list[Edge] = []
    total_weight = 0

    for neighbor, weight in graph[start]:
        heappush(min_heap, (weight, start, neighbor))

    while min_heap and len(visited) < len(graph):
        weight, u, v = heappop(min_heap)
        if v in visited:
            continue

        visited.add(v)
        mst.append((u, v, weight))
        total_weight += weight

        for next_node, next_weight in graph[v]:
            if next_node not in visited:
                heappush(min_heap, (next_weight, v, next_node))

    if len(visited) != len(graph):
        return None

    return mst, total_weight


def main() -> None:
    graph: Graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("C", 2), ("D", 5)],
        "C": [("A", 4), ("B", 2), ("D", 3)],
        "D": [("B", 5), ("C", 3)],
    }

    result = prim_mst(graph, start="A")
    print(f"graph={graph}")
    print(f"mst={result}")


if __name__ == "__main__":
    main()
