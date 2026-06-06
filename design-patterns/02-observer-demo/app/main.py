from dataclasses import dataclass, field
from typing import Protocol


class OrderObserver(Protocol):
    def update(self, order_id: str, status: str) -> str:
        ...


class EmailNotifier:
    def update(self, order_id: str, status: str) -> str:
        return f"email: order {order_id} is now {status}"


class WarehouseBoard:
    def update(self, order_id: str, status: str) -> str:
        return f"warehouse-board: order {order_id} moved to {status}"


@dataclass(slots=True)
class OrderTracker:
    _observers: list[OrderObserver] = field(default_factory=list)
    _history: list[str] = field(default_factory=list)

    def subscribe(self, observer: OrderObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: OrderObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def set_status(self, order_id: str, status: str) -> list[str]:
        event = f"{order_id}:{status}"
        self._history.append(event)
        return [observer.update(order_id, status) for observer in self._observers]

    @property
    def history(self) -> tuple[str, ...]:
        return tuple(self._history)


def main() -> None:
    tracker = OrderTracker()
    tracker.subscribe(EmailNotifier())
    tracker.subscribe(WarehouseBoard())

    for message in tracker.set_status("A1001", "packed"):
        print(message)


if __name__ == "__main__":
    main()