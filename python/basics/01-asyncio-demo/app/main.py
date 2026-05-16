import asyncio
from time import perf_counter


async def fetch_value(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} finished in {delay:.1f}s"


async def run_sequential() -> tuple[list[str], float]:
    start = perf_counter()
    results = [
        await fetch_value("task-1", 0.2),
        await fetch_value("task-2", 0.2),
        await fetch_value("task-3", 0.2),
    ]
    duration = perf_counter() - start
    return results, duration


async def run_concurrent() -> tuple[list[str], float]:
    start = perf_counter()
    results = await asyncio.gather(
        fetch_value("task-1", 0.2),
        fetch_value("task-2", 0.2),
        fetch_value("task-3", 0.2),
    )
    duration = perf_counter() - start
    return list(results), duration


async def build_report() -> dict[str, object]:
    sequential_results, sequential_duration = await run_sequential()
    concurrent_results, concurrent_duration = await run_concurrent()
    return {
        "sequential_results": sequential_results,
        "sequential_duration": sequential_duration,
        "concurrent_results": concurrent_results,
        "concurrent_duration": concurrent_duration,
        "speedup": sequential_duration / concurrent_duration,
    }


async def main() -> None:
    report = await build_report()
    print("Sequential:")
    for item in report["sequential_results"]:
        print(f"  - {item}")
    print(f"  duration: {report['sequential_duration']:.3f}s")

    print("Concurrent:")
    for item in report["concurrent_results"]:
        print(f"  - {item}")
    print(f"  duration: {report['concurrent_duration']:.3f}s")
    print(f"  speedup: {report['speedup']:.2f}x")


if __name__ == "__main__":
    asyncio.run(main())
