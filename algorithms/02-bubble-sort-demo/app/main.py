def bubble_sort(values: list[int]) -> list[int]:
    items = values.copy()

    for pass_index in range(len(items)):
        swapped = False

        for current_index in range(0, len(items) - 1 - pass_index):
            if items[current_index] > items[current_index + 1]:
                items[current_index], items[current_index + 1] = (
                    items[current_index + 1],
                    items[current_index],
                )
                swapped = True

        if not swapped:
            break

    return items


def main() -> None:
    numbers = [5, 1, 4, 2, 8]
    sorted_numbers = bubble_sort(numbers)
    print(f"numbers={numbers}")
    print(f"sorted={sorted_numbers}")


if __name__ == "__main__":
    main()