from app.main import best_knapsack_value


def test_best_knapsack_value_picks_optimal_combination() -> None:
    items = [(2, 6), (2, 10), (3, 12)]

    assert best_knapsack_value(5, items) == 22


def test_best_knapsack_value_returns_zero_when_capacity_is_zero() -> None:
    assert best_knapsack_value(0, [(1, 10), (2, 20)]) == 0