from contextlib import asynccontextmanager
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

from fastapi import FastAPI, File, Form, HTTPException, Request, UploadFile, status
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field


class FileRecord(BaseModel):
    id: str
    filename: str
    content_type: str
    size: int = Field(description="Stored file size in bytes")
    note: str | None = None
    stored_at: str


def _build_storage_path(upload_dir: Path, file_id: str, filename: str) -> Path:
    suffix = Path(filename).suffix
    return upload_dir / f"{file_id}{suffix}"


def _public_record(record: dict[str, Any]) -> FileRecord:
    return FileRecord(
        id=record["id"],
        filename=record["filename"],
        content_type=record["content_type"],
        size=record["size"],
        note=record["note"],
        stored_at=record["stored_at"],
    )


def create_app(upload_dir: Path | None = None) -> FastAPI:
    resolved_upload_dir = upload_dir or Path(__file__).resolve().parent.parent / ".uploads"

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        resolved_upload_dir.mkdir(parents=True, exist_ok=True)
        app.state.upload_dir = resolved_upload_dir
        app.state.file_index = {}
        yield

    app = FastAPI(title="File Upload Demo", version="0.1.0", lifespan=lifespan)

    @app.post("/files", response_model=FileRecord, status_code=status.HTTP_201_CREATED)
    async def upload_file(
        request: Request,
        file: UploadFile = File(...),
        note: str | None = Form(default=None),
    ) -> FileRecord:
        filename = file.filename or "upload.bin"
        file_id = uuid4().hex
        storage_path = _build_storage_path(request.app.state.upload_dir, file_id, filename)
        content = await file.read()
        storage_path.write_bytes(content)

        record = {
            "id": file_id,
            "filename": filename,
            "content_type": file.content_type or "application/octet-stream",
            "size": len(content),
            "note": note,
            "stored_at": datetime.now(UTC).isoformat(),
            "path": storage_path,
        }
        request.app.state.file_index[file_id] = record
        return _public_record(record)

    @app.get("/files", response_model=list[FileRecord])
    def list_files(request: Request) -> list[FileRecord]:
        return [_public_record(record) for record in request.app.state.file_index.values()]

    @app.get("/files/{file_id}", response_model=FileRecord)
    def get_file_metadata(request: Request, file_id: str) -> FileRecord:
        record = request.app.state.file_index.get(file_id)
        if record is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")
        return _public_record(record)

    @app.get("/files/{file_id}/download")
    def download_file(request: Request, file_id: str) -> FileResponse:
        record = request.app.state.file_index.get(file_id)
        if record is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")

        file_path = Path(record["path"])
        if not file_path.exists():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Stored file is missing")

        return FileResponse(
            path=file_path,
            media_type=record["content_type"],
            filename=record["filename"],
        )

    @app.delete("/files/{file_id}")
    def delete_file(request: Request, file_id: str) -> dict[str, bool]:
        record = request.app.state.file_index.pop(file_id, None)
        if record is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")

        file_path = Path(record["path"])
        if file_path.exists():
            file_path.unlink()

        return {"deleted": True}

    @app.get("/health")
    def healthcheck(request: Request) -> dict[str, str | int]:
        return {
            "status": "ok",
            "upload_dir": str(request.app.state.upload_dir),
            "file_count": len(request.app.state.file_index),
        }

    return app


app = create_app()