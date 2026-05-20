from app.main import build_demo_output, generate_even_numbers


def test_generate_even_numbers_yields_expected_values() -> None:
    assert list(generate_even_numbers(6)) == [0, 2, 4, 6]


def test_build_demo_output_returns_sum() -> None:
    demo_output = build_demo_output(8)

    assert demo_output["numbers"] == [0, 2, 4, 6, 8]
    assert demo_output["sum"] == 20