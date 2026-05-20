from app.main import build_demo_output


def test_build_demo_output_creates_square_list() -> None:
    demo_output = build_demo_output([2, 3])

    assert demo_output["squares"] == [4, 9]


def test_build_demo_output_creates_parity_mapping() -> None:
    demo_output = build_demo_output([1, 2, 3])

    assert demo_output["parity"] == {1: "odd", 2: "even", 3: "odd"}