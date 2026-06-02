import os

from celery import Celery


def _env_flag(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


heartbeat_seconds = float(os.getenv("CELERY_HEARTBEAT_SECONDS", "10"))

celery_app = Celery(
    "study_record_celery_beat_demo",
    broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/1"),
)

celery_app.conf.update(
    accept_content=["json"],
    beat_schedule={
        "record-demo-heartbeat": {
            "task": "app.tasks.record_heartbeat",
            "schedule": heartbeat_seconds,
            "args": ("beat",),
        }
    },
    enable_utc=True,
    imports=("app.tasks",),
    result_serializer="json",
    task_always_eager=_env_flag("CELERY_TASK_ALWAYS_EAGER"),
    task_store_eager_result=True,
    task_serializer="json",
    timezone="UTC",
)
