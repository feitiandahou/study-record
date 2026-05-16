# JWT demo

This module demonstrates a minimal FastAPI JWT flow:

- `POST /token`: verify username and password, then issue a JWT.
- `GET /me`: read the bearer token and return the current user.

## Run

```powershell
uv sync
uv run uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to test the endpoints.

## Demo account

- Username: `demo`
- Password: `demo123`

## Test

```powershell
uv run pytest
```
