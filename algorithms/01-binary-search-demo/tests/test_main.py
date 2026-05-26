from app.main import binary_search


def test_binary_search_returns_matching_index() -> None:
    assert binary_search([1, 3, 5, 7, 9], 7) == 3


def test_binary_search_returns_minus_one_when_missing() -> None:
    assert binary_search([1, 3, 5, 7, 9], 2) == -1