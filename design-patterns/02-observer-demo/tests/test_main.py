from app.main import EmailNotifier, OrderTracker, WarehouseBoard


def test_order_tracker_notifies_all_subscribers() -> None:
    tracker = OrderTracker()
    tracker.subscribe(EmailNotifier())
    tracker.subscribe(WarehouseBoard())

    messages = tracker.set_status("A1001", "packed")

    assert messages == [
        "email: order A1001 is now packed",
        "warehouse-board: order A1001 moved to packed",
    ]
    assert tracker.history == ("A1001:packed",)


def test_order_tracker_stops_notifying_unsubscribed_observer() -> None:
    tracker = OrderTracker()
    email_notifier = EmailNotifier()

    tracker.subscribe(email_notifier)
    tracker.unsubscribe(email_notifier)

    assert tracker.set_status("A1002", "shipped") == []