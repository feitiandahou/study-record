from app.main import AuditDecorator, EmailNotifier, SmsDecorator


def test_email_notifier_keeps_base_behavior() -> None:
    notifier = EmailNotifier()

    result = notifier.send("alice@example.com", "Invoice ready")

    assert result == ["email: alice@example.com <- Invoice ready"]


def test_decorators_layer_extra_delivery_steps() -> None:
    notifier = AuditDecorator(SmsDecorator(EmailNotifier()))

    result = notifier.send("alice@example.com", "Invoice ready")

    assert result == [
        "email: alice@example.com <- Invoice ready",
        "sms: alice@example.com <- Invoice ready",
        "audit: queued notification for alice@example.com",
    ]
    assert notifier.entries == ["audit: queued notification for alice@example.com"]