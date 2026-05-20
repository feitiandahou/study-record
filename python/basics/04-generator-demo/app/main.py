def generate_even_numbers(limit: int):
    for number in range(limit + 1):
        if number % 2 == 0:
            yield number


def build_demo_output(limit: int = 10) -> dict[str, object]:
    numbers = list(generate_even_numbers(limit))
    return {
        "numbers": numbers,
        "sum": sum(numbers),
    }


def main() -> None:
    demo_output = build_demo_output()
    print(f"even numbers: {demo_output['numbers']}")
    print(f"sum: {demo_output['sum']}")


if __name__ == "__main__":
    main()