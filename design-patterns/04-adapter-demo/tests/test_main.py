from app.main import IncidentNotifier, LegacySmsGateway, SlackSender, SmsSenderAdapter


def test_incident_notifier_works_with_native_sender() -> None:
    notifier = IncidentNotifier(sender=SlackSender())

    message = notifier.notify("ops-team", "INC-204", "critical")

    assert message == "slack: @ops-team <- incident INC-204 is critical"


def test_sms_sender_adapter_converts_to_legacy_gateway_contract() -> None:
    notifier = IncidentNotifier(sender=SmsSenderAdapter(LegacySmsGateway()))

    message = notifier.notify("+1 555 0100", "INC-204", "critical")

    assert message == "sms: +15550100 <- incident INC-204 is critical"
