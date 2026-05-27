# SQLModel CRUD demo

Demonstrates a fully typed FastAPI CRUD API backed by **SQLite** via
[SQLModel](https://sqlmodel.tiangolo.com/) — the library that unifies
SQLAlchemy ORM models and Pydantic schemas into a single class.

## Endpoints

| Method   | Path              | Description              |
|----------|-------------------|--------------------------|
| `POST`   | `/notes`          | Create a note (201)      |
| `GET`    | `/notes`          | List all notes           |
| `GET`    | `/notes/{id}`     | Get a single note        |
| `PATCH`  | `/notes/{id}`     | Partial update           |
| `DELETE` | `/notes/{id}`     | Delete a note (204)      |
| `GET`    | `/health`         | Health check             |

## Key concepts

- `SQLModel` — single class acts as both ORM table and Pydantic schema.
- `table=True` marks a class as a DB table; plain classes are pure schemas.
- `Session` dependency injected via `Annotated` + `Depends`.
- `lifespan` context manager used for startup table creation (replaces deprecated `@app.on_event`).
- Partial updates via `model_dump(exclude_unset=True)` + `sqlmodel_update`.
- Tests override the `get_session` dependency with an in-memory SQLite engine.

## Run

```powershell
uv sync
uv run uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to test interactively.

## Test

```powershell
uv run pytest
```
