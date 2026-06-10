from app.main import shortest_path


def test_shortest_path_returns_minimum_hops() -> None:
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["E"],
        "D": ["F"],
        "E": ["F"],
        "F": [],
    }

    assert shortest_path(graph, "A", "F") == ["A", "B", "D", "F"]


def test_shortest_path_returns_empty_list_when_missing() -> None:
    graph = {
        "A": ["B"],
        "B": [],
        "C": [],
    }

    assert shortest_path(graph, "A", "C") == []