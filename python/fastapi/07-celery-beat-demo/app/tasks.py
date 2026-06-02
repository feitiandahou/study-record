from app.celery_app import celery_app
from app.store import append_heartbeat


@celery_app.task(name="app.tasks.multiply_numbers")
def multiply_numbers(a: int, b: int) -> dict[str, int]:
    return {
        "a": a,
        "b": b,
        "product": a * b,
    }


@celery_app.task(name="app.tasks.record_heartbeat")
def record_heartbeat(source: str = "beat") -> dict[str, str]:
    return append_heartbeat(source)
