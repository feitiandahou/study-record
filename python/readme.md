# Python demos

This directory contains independent Python study modules.

## Modules

- `basics/01-asyncio-demo`: compare sequential and concurrent coroutine execution.
- `basics/02-decorator-demo`: demonstrate how decorators wrap and extend functions.
- `basics/03-dataclass-demo`: use `dataclass` to model simple structured data.
- `basics/04-generator-demo`: generate values lazily with `yield`.
- `basics/05-contextmanager-demo`: handle setup and cleanup with `with`.
- `basics/06-pathlib-demo`: compose and inspect filesystem paths with `pathlib`.
- `basics/07-classmethod-staticmethod-demo`: compare class-level and utility methods.
- `basics/08-exception-demo`: demonstrate `try`, `except`, and `finally`.
- `basics/09-iterator-demo`: build a custom iterator with `__next__`.
- `basics/10-comprehension-demo`: transform collections with comprehensions.
- `fastapi/01-jwt-demo`: minimal JWT login and bearer token flow.
- `fastapi/02-websocket-demo`: minimal WebSocket connect and echo flow.
- `fastapi/03-kafka-demo`: minimal Kafka producer and consumer integration flow.
- `fastapi/04-background-tasks-demo`: compare in-process background jobs with simple task tracking.
- `fastapi/05-sqlmodel-crud-demo`: build a typed CRUD API with FastAPI and SQLModel.
- `fastapi/06-celery-demo`: enqueue and inspect distributed background jobs with Celery.

## With uv

Each demo is an independent `uv` project.

```powershell
cd python/basics/01-asyncio-demo
uv sync
uv run python -m app.main
```

Use the same pattern in any other module directory.

