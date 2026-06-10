def best_knapsack_value(
    capacity: int, items: list[tuple[int, int]]
) -> int:
    dp = [0] * (capacity + 1)

    for weight, value in items:
        for current_capacity in range(capacity, weight - 1, -1):
            dp[current_capacity] = max(
                dp[current_capacity],
                dp[current_capacity - weight] + value,
            )

    return dp[capacity]


def main() -> None:
    capacity = 5
    items = [(2, 6), (2, 10), (3, 12)]
    best_value = best_knapsack_value(capacity, items)
    print(f"capacity={capacity}, items={items}")
    print(f"best_value={best_value}")


if __name__ == "__main__":
    main()