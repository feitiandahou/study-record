from app.main import bellman_ford


def test_bellman_ford_basic_graph() -> None:
    nodes = ["A", "B", "C", "D"]
    edges = [
        ("A", "B", 4),
        ("A", "C", 5),
        ("B", "C", -2),
        ("C", "D", 3),
        ("B", "D", 6),
    ]

    result = bellman_ford(nodes, edges, source="A")
    assert result == {"A": 0, "B": 4, "C": 2, "D": 5}


def test_bellman_ford_unreachable_node_keeps_inf() -> None:
    nodes = ["A", "B", "C"]
    edges = [("A", "B", 2)]

    result = bellman_ford(nodes, edges, source="A")
    assert result is not None
    assert result["C"] == float("inf")


def test_bellman_ford_detects_negative_cycle() -> None:
    nodes = ["A", "B", "C"]
    edges = [
        ("A", "B", 1),
        ("B", "C", -2),
        ("C", "B", -2),
    ]

    assert bellman_ford(nodes, edges, source="A") is None


def test_bellman_ford_source_not_in_nodes_returns_none() -> None:
    nodes = ["A", "B"]
    edges = [("A", "B", 1)]

    assert bellman_ford(nodes, edges, source="Z") is None


def test_bellman_ford_empty_graph_and_source_missing() -> None:
    assert bellman_ford([], [], source="A") is None
