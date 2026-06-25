from app.main import kruskal_mst


def test_kruskal_mst_returns_expected_weight_and_edge_count() -> None:
    nodes = ["A", "B", "C", "D"]
    edges = [
        ("A", "B", 1),
        ("B", "C", 2),
        ("A", "C", 3),
        ("C", "D", 4),
        ("B", "D", 5),
    ]

    result = kruskal_mst(nodes, edges)
    assert result is not None

    mst_edges, total_weight = result
    assert len(mst_edges) == len(nodes) - 1
    assert total_weight == 7


def test_kruskal_mst_with_equal_weights() -> None:
    nodes = ["A", "B", "C"]
    edges = [
        ("A", "B", 1),
        ("B", "C", 1),
        ("A", "C", 1),
    ]

    result = kruskal_mst(nodes, edges)
    assert result is not None

    mst_edges, total_weight = result
    assert len(mst_edges) == 2
    assert total_weight == 2


def test_kruskal_mst_detects_disconnected_graph() -> None:
    nodes = ["A", "B", "C", "D"]
    edges = [
        ("A", "B", 1),
        ("C", "D", 2),
    ]

    assert kruskal_mst(nodes, edges) is None


def test_kruskal_mst_single_node() -> None:
    assert kruskal_mst(["A"], []) == ([], 0)


def test_kruskal_mst_empty_graph() -> None:
    assert kruskal_mst([], []) == ([], 0)
