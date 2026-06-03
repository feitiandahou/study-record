# File upload demo

Demonstrates a minimal **FastAPI file upload** workflow with multipart form data:

- `POST /files`: upload a file with an optional note.
- `GET /files`: list uploaded file metadata.
- `GET /files/{file_id}`: inspect a single uploaded file.
- `GET /files/{file_id}/download`: download the stored file.
- `DELETE /files/{file_id}`: remove both metadata and file content.
- `GET /health`: inspect storage directory and current file count.

## Key concepts

- `UploadFile` streams multipart uploads efficiently instead of loading everything through JSON.
- `File(...)` and `Form(...)` let one endpoint accept both binary content and normal fields.
- `FileResponse` returns a saved file with download headers.
- `lifespan` initializes per-app storage state, which also makes tests easy to isolate.
- Tests use a temporary directory so they do not leave local artifacts behind.

## Run

```powershell
uv sync
uv run uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs`, call `POST /files`, then use the returned `file_id` for the other endpoints.

By default, uploaded files are stored under `.uploads/` in this demo directory.

## Test

```powershell
uv sync
uv run pytest
```