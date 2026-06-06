from app.main import CsvReportGenerator, MarkdownReportGenerator


def test_csv_report_generator_uses_csv_serializer() -> None:
    report = CsvReportGenerator().export("Daily Summary", [("orders", 24), ("returns", 3)])

    assert report.filename == "daily_summary.csv"
    assert report.content == "name,value\norders,24\nreturns,3"


def test_markdown_report_generator_uses_markdown_serializer() -> None:
    report = MarkdownReportGenerator().export("Daily Summary", [("orders", 24)])

    assert report.filename == "daily_summary.md"
    assert report.content == "# Daily Summary\n\n| Name | Value |\n| --- | ---: |\n| orders | 24 |"