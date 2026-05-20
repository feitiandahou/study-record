def build_demo_output(numbers: list[int] | None = None) -> dict[str, object]:
    source = numbers or [1, 2, 3, 4, 5]
    squares = [number * number for number in source]
    parity = {number: ("even" if number % 2 == 0 else "odd") for number in source}
    return {
        "squares": squares,
        "parity": parity,
    }


def main() -> None:
    demo_output = build_demo_output()
    print(f"squares: {demo_output['squares']}")
    print(f"parity: {demo_output['parity']}")


if __name__ == "__main__":
    main()