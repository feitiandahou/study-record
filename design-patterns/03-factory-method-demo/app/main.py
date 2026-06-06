from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol


class ReportSerializer(Protocol):
    extension: str

    def serialize(self, title: str, rows: list[tuple[str, int]]) -> str:
        ...


class CsvSerializer:
    extension = "csv"

    def serialize(self, title: str, rows: list[tuple[str, int]]) -> str:
        lines = ["name,value"]
        lines.extend(f"{name},{value}" for name, value in rows)
        return "\n".join(lines)


class MarkdownSerializer:
    extension = "md"

    def serialize(self, title: str, rows: list[tuple[str, int]]) -> str:
        lines = [f"# {title}", "", "| Name | Value |", "| --- | ---: |"]
        lines.extend(f"| {name} | {value} |" for name, value in rows)
        return "\n".join(lines)


@dataclass(slots=True)
class Report:
    filename: str
    content: str


class ReportGenerator(ABC):
    def export(self, title: str, rows: list[tuple[str, int]]) -> Report:
        serializer = self.create_serializer()
        filename = f"{title.lower().replace(' ', '_')}.{serializer.extension}"
        return Report(filename=filename, content=serializer.serialize(title, rows))

    @abstractmethod
    def create_serializer(self) -> ReportSerializer:
        raise NotImplementedError


class CsvReportGenerator(ReportGenerator):
    def create_serializer(self) -> ReportSerializer:
        return CsvSerializer()


class MarkdownReportGenerator(ReportGenerator):
    def create_serializer(self) -> ReportSerializer:
        return MarkdownSerializer()


def describe_report(generator: ReportGenerator, title: str, rows: list[tuple[str, int]]) -> str:
    report = generator.export(title, rows)
    return f"{report.filename}\n{report.content}"


def main() -> None:
    rows = [("orders", 24), ("returns", 3)]

    print(describe_report(CsvReportGenerator(), "Daily Summary", rows))
    print()
    print(describe_report(MarkdownReportGenerator(), "Daily Summary", rows))


if __name__ == "__main__":
    main()