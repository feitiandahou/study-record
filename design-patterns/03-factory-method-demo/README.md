# Factory Method demo

This module demonstrates a minimal Factory Method pattern in Python:

- `ReportGenerator`: defines the export workflow.
- `CsvReportGenerator`: chooses a CSV serializer.
- `MarkdownReportGenerator`: chooses a Markdown serializer.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```