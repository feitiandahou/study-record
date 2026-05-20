from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    age: int
    skills: list[str] = field(default_factory=list)

    def summary(self) -> str:
        joined_skills = ", ".join(self.skills) if self.skills else "no skills yet"
        return f"{self.name} ({self.age}) -> {joined_skills}"


def build_demo_output() -> dict[str, object]:
    student = Student(name="Alice", age=20, skills=["python", "sql"])
    return {
        "student": student,
        "summary": student.summary(),
    }


def main() -> None:
    demo_output = build_demo_output()
    print(demo_output["summary"])


if __name__ == "__main__":
    main()