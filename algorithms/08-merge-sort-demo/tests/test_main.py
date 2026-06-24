from app.main import merge_sort


def test_merge_sort_sorts_unsorted_list() -> None:
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]


def test_merge_sort_handles_already_sorted_list() -> None:
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_merge_sort_handles_reverse_sorted_list() -> None:
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_merge_sort_handles_single_element() -> None:
    assert merge_sort([42]) == [42]


def test_merge_sort_handles_empty_list() -> None:
    assert merge_sort([]) == []


def test_merge_sort_handles_duplicates() -> None:
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]
