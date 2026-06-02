from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.celery_app import celery_app
from app.store import clear_heartbeats


@pytest.fixture(autouse=True)
def configure_demo(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_STATE_USE_MEMORY", "true")
    celery_app.conf.task_always_eager = True
    celery_app.conf.task_store_eager_result = True
    celery_app.conf.broker_url = "memory://"
    celery_app.conf.result_backend = "cache+memory://"
    clear_heartbeats()
    yield
    clear_heartbeats()
