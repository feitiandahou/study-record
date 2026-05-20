class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> "Temperature":
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return celsius * 9 / 5 + 32


def build_demo_output() -> dict[str, float]:
    temperature = Temperature.from_fahrenheit(68)
    return {
        "celsius": round(temperature.celsius, 1),
        "fahrenheit": Temperature.celsius_to_fahrenheit(20),
    }


def main() -> None:
    demo_output = build_demo_output()
    print(f"68F -> {demo_output['celsius']}C")
    print(f"20C -> {demo_output['fahrenheit']}F")


if __name__ == "__main__":
    main()