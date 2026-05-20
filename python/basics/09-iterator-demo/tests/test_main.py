from app.main import Countdown, build_demo_output


def test_countdown_iterates_until_zero() -> None:
    assert list(Countdown(2)) == [2, 1, 0]


def test_build_demo_output_collects_iterator_values() -> None:
    assert build_demo_output(4) == [4, 3, 2, 1, 0]