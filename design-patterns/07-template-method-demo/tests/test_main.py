from app.main import EmailDeploymentSummary, SlackDeploymentSummary


def test_email_summary_uses_fixed_steps_with_email_format() -> None:
    summary = EmailDeploymentSummary()

    result = summary.build("billing-api", "v1.4.2")

    assert result == (
        "Subject: billing-api v1.4.2 deployed\n"
        "- prepare billing-api v1.4.2\n"
        "- verify health checks for billing-api\n"
        "- release billing-api v1.4.2\n"
        "- announce billing-api v1.4.2"
    )


def test_slack_summary_reuses_same_algorithm_with_different_format() -> None:
    summary = SlackDeploymentSummary()

    result = summary.build("billing-api", "v1.4.2")

    assert result == (
        "slack: [billing-api@v1.4.2] "
        "prepare billing-api v1.4.2 | "
        "verify health checks for billing-api | "
        "release billing-api v1.4.2 | "
        "announce billing-api v1.4.2"
    )