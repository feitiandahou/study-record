from app.main import Temperature, build_demo_output


def test_classmethod_builds_instance_from_fahrenheit() -> None:
    temperature = Temperature.from_fahrenheit(50)

    assert round(temperature.celsius, 1) == 10.0


def test_staticmethod_converts_celsius_to_fahrenheit() -> None:
    demo_output = build_demo_output()

    assert demo_output == {"celsius": 20.0, "fahrenheit": 68.0}