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

    def connected(self, a: str, b: str) -> bool:
        return self.find(a) == self.find(b)


def main() -> None:
    users = ["A", "B", "C", "D", "E"]
    dsu = UnionFind(users)

    dsu.union("A", "B")
    dsu.union("C", "D")
    dsu.union("B", "C")

    print("A connected to D:", dsu.connected("A", "D"))
    print("A connected to E:", dsu.connected("A", "E"))


if __name__ == "__main__":
    main()
