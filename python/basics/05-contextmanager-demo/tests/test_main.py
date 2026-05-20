from app.main import build_demo_output, managed_events


def test_context_manager_runs_cleanup_after_block() -> None:
    assert build_demo_output() == ["setup", "work", "cleanup"]


def test_context_manager_exposes_mutable_value_inside_block() -> None:
    with managed_events() as events:
        events.append("inside")

    assert events == ["setup", "inside", "cleanup"]