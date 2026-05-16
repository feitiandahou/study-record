from app.main import build_demo_output, greet


def test_greet_returns_wrapped_result(capsys) -> None:
    result = greet("demo")
    output = capsys.readouterr().out

    assert result == "hello, demo"
    assert "before calling greet" in output
    assert "after calling greet" in output


def test_wraps_preserves_function_name() -> None:
    demo_output = build_demo_output()
    assert demo_output["function_name"] == "greet"