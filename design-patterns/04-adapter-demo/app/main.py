from dataclasses import dataclass
from typing import Protocol


class AlertSender(Protocol):
    def send(self, recipient: str, message: str) -> str:
        ...


class SlackSender:
    def send(self, recipient: str, message: str) -> str:
        return f"slack: @{recipient} <- {message}"


class LegacySmsGateway:
    def deliver(self, phone_number: str, content: str) -> str:
        return f"sms: {phone_number} <- {content}"


@dataclass(slots=True)
class SmsSenderAdapter:
    gateway: LegacySmsGateway

    def send(self, recipient: str, message: str) -> str:
        normalized_number = recipient.replace(" ", "")
        return self.gateway.deliver(normalized_number, message)


@dataclass(slots=True)
class IncidentNotifier:
    sender: AlertSender

    def notify(self, recipient: str, incident_id: str, severity: str) -> str:
        message = f"incident {incident_id} is {severity}"
        return self.sender.send(recipient, message)


def main() -> None:
    notifier = IncidentNotifier(sender=SlackSender())
    print(notifier.notify("ops-team", "INC-204", "critical"))

    sms_notifier = IncidentNotifier(sender=SmsSenderAdapter(LegacySmsGateway()))
    print(sms_notifier.notify("+1 555 0100", "INC-204", "critical"))


if __name__ == "__main__":
    main()
