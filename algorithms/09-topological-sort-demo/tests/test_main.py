from app.main import topological_sort


def test_topological_sort_returns_valid_order() -> None:
    graph = {
        "A": ["C"],
        "B": ["C"],
        "C": ["D", "E"],
        "D": [],
        "E": [],
    }
    order = topological_sort(graph)
    assert order is not None
    assert set(order) == {"A", "B", "C", "D", "E"}
    # A and B must both come before C
    assert order.index("A") < order.index("C")
    assert order.index("B") < order.index("C")
    # C must come before D and E
    assert order.index("C") < order.index("D")
    assert order.index("C") < order.index("E")


def test_topological_sort_linear_chain() -> None:
    graph = {"A": ["B"], "B": ["C"], "C": []}
    assert topological_sort(graph) == ["A", "B", "C"]


def test_topological_sort_detects_cycle() -> None:
    graph = {"A": ["B"], "B": ["C"], "C": ["A"]}
    assert topological_sort(graph) is None


def test_topological_sort_single_node() -> None:
    assert topological_sort({"A": []}) == ["A"]


def test_topological_sort_disconnected_graph() -> None:
    graph = {"A": [], "B": [], "C": []}
    order = topological_sort(graph)
    assert order is not None
    assert set(order) == {"A", "B", "C"}
