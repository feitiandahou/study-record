def merge_sort(items: list[int]) -> list[int]:
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    result: list[int] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def main() -> None:
    items = [38, 27, 43, 3, 9, 82, 10]
    print(f"before: {items}")
    sorted_items = merge_sort(items)
    print(f"after:  {sorted_items}")


if __name__ == "__main__":
    main()
