from pathlib import Path

from app.main import build_demo_output, summarize_path


def test_summarize_path_extracts_parts() -> None:
    summary = summarize_path(Path("base"))

    assert summary["name"] == "demo.txt"
    assert summary["stem"] == "demo"
    assert summary["suffix"] == ".txt"
    assert summary["parts"][-2:] == ("notes", "demo.txt")


def test_build_demo_output_uses_study_record_base() -> None:
    demo_output = build_demo_output()

    assert str(demo_output["target"]).endswith("study-record/notes/demo.txt") or str(
        demo_output["target"]
    ).endswith("study-record\\notes\\demo.txt")