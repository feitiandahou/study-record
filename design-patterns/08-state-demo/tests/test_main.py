from app.main import PublishingWorkflow


def test_workflow_moves_from_draft_to_published_via_states() -> None:
    workflow = PublishingWorkflow("Release notes")

    first_transition = workflow.request_review()
    second_transition = workflow.approve()

    assert first_transition == "moved to review"
    assert second_transition == "published"
    assert workflow.status() == "Published: Release notes is live"


def test_invalid_action_is_resolved_by_current_state() -> None:
    workflow = PublishingWorkflow("Release notes")

    result = workflow.approve()

    assert result == "cannot approve while draft"
    assert workflow.status() == "Draft: Release notes is being edited"