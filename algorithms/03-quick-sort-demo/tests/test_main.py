from app.main import quick_sort


def test_quick_sort_returns_sorted_copy() -> None:
    assert quick_sort([10, 7, 8, 9, 1, 5]) == [1, 5, 7, 8, 9, 10]


def test_quick_sort_handles_duplicate_values() -> None:
    assert quick_sort([4, 2, 4, 1, 2]) == [1, 2, 2, 4, 4]