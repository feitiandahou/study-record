from app.main import depth_first_traversal


def test_depth_first_traversal_visits_nodes_depth_first() -> None:
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": [],
    }

    assert depth_first_traversal(graph, "A") == ["A", "B", "D", "E", "C", "F"]


def test_depth_first_traversal_returns_empty_list_for_unknown_start() -> None:
    assert depth_first_traversal({"A": ["B"], "B": []}, "Z") == []