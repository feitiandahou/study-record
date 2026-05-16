import asyncio

from app.main import build_report, fetch_value


def test_fetch_value_returns_expected_text() -> None:
    result = asyncio.run(fetch_value("demo", 0.0))
    assert result == "demo finished in 0.0s"


def test_concurrent_execution_is_faster_than_sequential() -> None:
    report = asyncio.run(build_report())
    assert report["sequential_results"] == report["concurrent_results"]
    assert report["sequential_duration"] > report["concurrent_duration"]
    assert report["speedup"] > 2
