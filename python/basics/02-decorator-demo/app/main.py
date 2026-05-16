from collections.abc import Callable
from functools import wraps
from typing import Any


def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"after calling {func.__name__}")
        return result

    return wrapper


@log_calls
def greet(name: str) -> str:
    return f"hello, {name}"


def build_demo_output() -> dict[str, str]:
    return {
        "function_name": greet.__name__,
        "greeting": greet("study-record"),
    }


def main() -> None:
    demo_output = build_demo_output()
    print(f"wrapped function name: {demo_output['function_name']}")
    print(f"result: {demo_output['greeting']}")


if __name__ == "__main__":
    main()
