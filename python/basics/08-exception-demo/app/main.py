def safe_divide(left: float, right: float) -> dict[str, object]:
    cleaned_up = False
    try:
        return {
            "result": left / right,
            "error": None,
            "cleaned_up": cleaned_up,
        }
    except ZeroDivisionError:
        return {
            "result": None,
            "error": "cannot divide by zero",
            "cleaned_up": cleaned_up,
        }
    finally:
        cleaned_up = True


def build_demo_output() -> dict[str, dict[str, object]]:
    return {
        "success": safe_divide(10, 2),
        "failure": safe_divide(10, 0),
    }


def main() -> None:
    demo_output = build_demo_output()
    print(demo_output)


if __name__ == "__main__":
    main()