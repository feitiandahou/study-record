from dataclasses import dataclass, field
from typing import Protocol


class Notifier(Protocol):
    def send(self, recipient: str, message: str) -> list[str]:
        ...


@dataclass(slots=True)
class EmailNotifier:
    def send(self, recipient: str, message: str) -> list[str]:
        return [f"email: {recipient} <- {message}"]


@dataclass(slots=True)
class NotifierDecorator:
    wrapped: Notifier

    def send(self, recipient: str, message: str) -> list[str]:
        return self.wrapped.send(recipient, message)


@dataclass(slots=True)
class SmsDecorator(NotifierDecorator):
    def send(self, recipient: str, message: str) -> list[str]:
        deliveries = self.wrapped.send(recipient, message)
        return [*deliveries, f"sms: {recipient} <- {message}"]


@dataclass(slots=True)
class AuditDecorator(NotifierDecorator):
    entries: list[str] = field(default_factory=list)

    def send(self, recipient: str, message: str) -> list[str]:
        deliveries = self.wrapped.send(recipient, message)
        self.entries.append(f"audit: queued notification for {recipient}")
        return [*deliveries, self.entries[-1]]


def main() -> None:
    notifier = AuditDecorator(SmsDecorator(EmailNotifier()))
    for delivery in notifier.send("alice@example.com", "Your invoice is ready"):
        print(delivery)


if __name__ == "__main__":
    main()