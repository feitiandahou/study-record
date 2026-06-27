from app.main import Graph, prim_mst


def test_prim_mst_returns_expected_weight_and_edge_count() -> None:
    graph: Graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("C", 2), ("D", 5)],
        "C": [("A", 4), ("B", 2), ("D", 3)],
        "D": [("B", 5), ("C", 3)],
    }

    result = prim_mst(graph, start="A")
    assert result is not None

    mst_edges, total_weight = result
    assert len(mst_edges) == len(graph) - 1
    assert total_weight == 6


def test_prim_mst_disconnected_graph_returns_none() -> None:
    graph: Graph = {
        "A": [("B", 1)],
        "B": [("A", 1)],
        "C": [("D", 2)],
        "D": [("C", 2)],
    }

    assert prim_mst(graph, start="A") is None


def test_prim_mst_single_node() -> None:
    assert prim_mst({"A": []}, start="A") == ([], 0)


def test_prim_mst_empty_graph() -> None:
    assert prim_mst({}) == ([], 0)


def test_prim_mst_start_none_works() -> None:
    graph: Graph = {
        "X": [("Y", 7)],
        "Y": [("X", 7)],
    }

    result = prim_mst(graph)
    assert result is not None

    mst_edges, total_weight = result
    assert len(mst_edges) == 1
    assert total_weight == 7
