Edge = tuple[str, str, int]


class UnionFind:
    def __init__(self, elements: list[str]) -> None:
        self.parent: dict[str, str] = {element: element for element in elements}
        self.rank: dict[str, int] = {element: 0 for element in elements}

    def find(self, element: str) -> str:
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, a: str, b: str) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        return True


def kruskal_mst(nodes: list[str], edges: list[Edge]) -> tuple[list[Edge], int] | None:
    if not nodes:
        return [], 0

    dsu = UnionFind(nodes)
    mst: list[Edge] = []
    total_weight = 0

    for u, v, w in sorted(edges, key=lambda edge: edge[2]):
        if dsu.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == len(nodes) - 1:
                break

    if len(mst) != len(nodes) - 1:
        return None

    return mst, total_weight


def main() -> None:
    nodes = ["A", "B", "C", "D", "E"]
    edges: list[Edge] = [
        ("A", "B", 1),
        ("A", "C", 3),
        ("B", "C", 2),
        ("B", "D", 4),
        ("C", "D", 5),
        ("C", "E", 6),
        ("D", "E", 7),
    ]

    result = kruskal_mst(nodes, edges)
    print(f"nodes={nodes}")
    print(f"edges={edges}")
    print(f"mst={result}")


if __name__ == "__main__":
    main()
