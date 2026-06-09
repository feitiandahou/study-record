from app.main import Ticket, build_support_chain


def test_chain_stops_when_billing_handler_can_resolve() -> None:
    handler = build_support_chain()

    result = handler.handle(Ticket("billing", "normal", "refund request"))

    assert result == "billing resolved: refund request"


def test_chain_falls_through_to_manager_for_critical_ticket() -> None:
    handler = build_support_chain()

    result = handler.handle(Ticket("technical", "critical", "checkout is down"))

    assert result == "manager escalated: checkout is down"