from app.main import shortest_path


def test_shortest_path_returns_lowest_cost_route() -> None:
    graph = {
        "A": {"B": 4, "C": 1},
        "B": {"D": 1},
        "C": {"B": 2, "D": 5},
        "D": {},
    }

    assert shortest_path(graph, "A", "D") == (4, ["A", "C", "B", "D"])


def test_shortest_path_returns_none_and_empty_path_when_unreachable() -> None:
    graph = {
        "A": {"B": 3},
        "B": {},
        "C": {},
    }

    assert shortest_path(graph, "A", "C") == (None, [])