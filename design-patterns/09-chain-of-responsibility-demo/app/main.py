from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Ticket:
    topic: str
    priority: str
    summary: str


class SupportHandler:
    def __init__(self, next_handler: SupportHandler | None = None) -> None:
        self._next_handler = next_handler

    def handle(self, ticket: Ticket) -> str:
        if self.can_handle(ticket):
            return self.resolve(ticket)
        if self._next_handler is not None:
            return self._next_handler.handle(ticket)
        return f"unhandled ticket: {ticket.summary}"

    def can_handle(self, ticket: Ticket) -> bool:
        raise NotImplementedError

    def resolve(self, ticket: Ticket) -> str:
        raise NotImplementedError


class BillingHandler(SupportHandler):
    def can_handle(self, ticket: Ticket) -> bool:
        return ticket.topic == "billing"

    def resolve(self, ticket: Ticket) -> str:
        return f"billing resolved: {ticket.summary}"


class TechnicalHandler(SupportHandler):
    def can_handle(self, ticket: Ticket) -> bool:
        return ticket.topic == "technical" and ticket.priority != "critical"

    def resolve(self, ticket: Ticket) -> str:
        return f"technical resolved: {ticket.summary}"


class DutyManagerHandler(SupportHandler):
    def can_handle(self, ticket: Ticket) -> bool:
        return ticket.priority == "critical"

    def resolve(self, ticket: Ticket) -> str:
        return f"manager escalated: {ticket.summary}"


def build_support_chain() -> SupportHandler:
    return BillingHandler(TechnicalHandler(DutyManagerHandler()))


def main() -> None:
    handler = build_support_chain()

    print(handler.handle(Ticket("billing", "normal", "refund request")))
    print(handler.handle(Ticket("technical", "normal", "cache miss spike")))
    print(handler.handle(Ticket("technical", "critical", "checkout is down")))


if __name__ == "__main__":
    main()