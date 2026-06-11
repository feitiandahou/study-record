def depth_first_traversal(
    graph: dict[str, list[str]], start: str
) -> list[str]:
    if start not in graph:
        return []

    visited: set[str] = set()
    order: list[str] = []

    def visit(node: str) -> None:
        if node in visited:
            return

        visited.add(node)
        order.append(node)

        for neighbor in graph.get(node, []):
            visit(neighbor)

    visit(start)
    return order


def main() -> None:
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": [],
    }
    order = depth_first_traversal(graph, "A")
    print(f"graph={graph}")
    print(f"dfs_order={order}")


if __name__ == "__main__":
    main()