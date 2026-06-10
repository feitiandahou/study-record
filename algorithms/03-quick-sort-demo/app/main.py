def quick_sort(values: list[int]) -> list[int]:
    if len(values) <= 1:
        return values.copy()

    pivot = values[0]
    lower = [value for value in values[1:] if value <= pivot]
    higher = [value for value in values[1:] if value > pivot]
    return quick_sort(lower) + [pivot] + quick_sort(higher)


def main() -> None:
    numbers = [10, 7, 8, 9, 1, 5]
    sorted_numbers = quick_sort(numbers)
    print(f"numbers={numbers}")
    print(f"sorted={sorted_numbers}")


if __name__ == "__main__":
    main()