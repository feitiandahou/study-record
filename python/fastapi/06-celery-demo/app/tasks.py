import time

from app.celery_app import celery_app


@celery_app.task(name="app.tasks.add_numbers")
def add_numbers(a: int, b: int, delay_seconds: float = 0.0) -> dict[str, int | float]:
    if delay_seconds > 0:
        time.sleep(delay_seconds)
    return {
        "a": a,
        "b": b,
        "total": a + b,
        "delay_seconds": delay_seconds,
    }
