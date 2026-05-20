from app.main import build_demo_output, safe_divide


def test_safe_divide_returns_result_for_valid_input() -> None:
    assert safe_divide(9, 3)["result"] == 3


def test_safe_divide_returns_error_for_zero_division() -> None:
    demo_output = build_demo_output()

    assert demo_output["failure"]["result"] is None
    assert demo_output["failure"]["error"] == "cannot divide by zero"