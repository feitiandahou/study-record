class Countdown:
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self) -> "Countdown":
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value


def build_demo_output(start: int = 3) -> list[int]:
    return list(Countdown(start))


def main() -> None:
    print(build_demo_output())


if __name__ == "__main__":
    main()