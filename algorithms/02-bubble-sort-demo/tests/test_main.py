from app.main import bubble_sort


def test_bubble_sort_returns_sorted_copy() -> None:
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]


def test_bubble_sort_keeps_input_unchanged() -> None:
    numbers = [3, 2, 1]

    assert bubble_sort(numbers) == [1, 2, 3]
    assert numbers == [3, 2, 1]