def binary_search(values: list[int], target: int) -> int:
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2
        guess = values[middle]

        if guess == target:
            return middle
        if guess < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def main() -> None:
    numbers = [2, 4, 8, 16, 32, 64]
    target = 16
    index = binary_search(numbers, target)
    print(f"numbers={numbers}")
    print(f"target={target}, index={index}")


if __name__ == "__main__":
    main()