from app.main import floyd_warshall


def test_floyd_warshall_basic_graph() -> None:
    nodes = ["A", "B", "C", "D"]
    edges = [
        ("A", "B", 4),
        ("A", "C", 5),
        ("B", "C", -2),
        ("C", "D", 3),
        ("B", "D", 6),
    ]

    result = floyd_warshall(nodes, edges)
    assert result is not None
    assert result["A"]["A"] == 0
    assert result["A"]["B"] == 4
    assert result["A"]["C"] == 2
    assert result["A"]["D"] == 5
    assert result["B"]["C"] == -2
    assert result["B"]["D"] == 1


def test_floyd_warshall_unreachable_nodes() -> None:
    nodes = ["A", "B", "C"]
    edges = [("A", "B", 2)]

    result = floyd_warshall(nodes, edges)
    assert result is not None
    assert result["B"]["C"] == float("inf")
    assert result["C"]["A"] == float("inf")


def test_floyd_warshall_detects_negative_cycle() -> None:
    nodes = ["A", "B", "C"]
    edges = [
        ("A", "B", 1),
        ("B", "C", -2),
        ("C", "B", -2),
    ]

    assert floyd_warshall(nodes, edges) is None


def test_floyd_warshall_edge_references_unknown_node() -> None:
    nodes = ["A", "B"]
    edges = [("A", "Z", 1)]

    assert floyd_warshall(nodes, edges) is None


def test_floyd_warshall_single_node() -> None:
    nodes = ["A"]
    edges: list[tuple[str, str, int]] = []

    result = floyd_warshall(nodes, edges)
    assert result is not None
    assert result["A"]["A"] == 0


def test_floyd_warshall_duplicate_edges_uses_min() -> None:
    nodes = ["A", "B"]
    edges = [("A", "B", 5), ("A", "B", 3)]

    result = floyd_warshall(nodes, edges)
    assert result is not None
    assert result["A"]["B"] == 3


def test_floyd_warshall_negative_self_loop_detected() -> None:
    nodes = ["A", "B"]
    edges = [("A", "A", -1), ("A", "B", 1)]

    assert floyd_warshall(nodes, edges) is None
