from app.main import UnionFind


def test_union_find_initially_disconnected() -> None:
    dsu = UnionFind(["A", "B", "C"])
    assert dsu.connected("A", "A")
    assert not dsu.connected("A", "B")
    assert not dsu.connected("B", "C")


def test_union_find_union_connects_components() -> None:
    dsu = UnionFind(["A", "B", "C", "D"])
    assert dsu.union("A", "B")
    assert dsu.union("C", "D")
    assert dsu.union("B", "C")

    assert dsu.connected("A", "D")
    assert dsu.connected("A", "C")


def test_union_find_union_same_component_returns_false() -> None:
    dsu = UnionFind(["A", "B"])
    assert dsu.union("A", "B")
    assert not dsu.union("A", "B")


def test_union_find_path_compression_effect() -> None:
    dsu = UnionFind(["A", "B", "C", "D"])
    dsu.union("A", "B")
    dsu.union("B", "C")
    dsu.union("C", "D")

    root = dsu.find("D")
    assert root == dsu.find("A")
    # After find with path compression, D points directly to root.
    assert dsu.parent["D"] == root
