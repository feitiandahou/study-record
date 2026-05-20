from app.main import Student, build_demo_output


def test_student_uses_default_factory_for_skills() -> None:
    first = Student(name="A", age=18)
    second = Student(name="B", age=19)

    first.skills.append("python")

    assert first.skills == ["python"]
    assert second.skills == []


def test_build_demo_output_returns_summary() -> None:
    demo_output = build_demo_output()

    assert demo_output["summary"] == "Alice (20) -> python, sql"