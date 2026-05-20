from collections.abc import Iterator
from contextlib import contextmanager


@contextmanager
def managed_events() -> Iterator[list[str]]:
    events = ["setup"]
    try:
        yield events
    finally:
        events.append("cleanup")


def build_demo_output() -> list[str]:
    with managed_events() as events:
        events.append("work")
    return events


def main() -> None:
    print(build_demo_output())


if __name__ == "__main__":
    main()