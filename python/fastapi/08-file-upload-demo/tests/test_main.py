from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import create_app


@pytest.fixture
def client(tmp_path: Path) -> TestClient:
    app = create_app(upload_dir=tmp_path)
    with TestClient(app) as test_client:
        yield test_client


def test_upload_file_returns_metadata(client: TestClient) -> None:
    response = client.post(
        "/files",
        files={"file": ("hello.txt", b"hello world", "text/plain")},
        data={"note": "sample text file"},
    )

    assert response.status_code == 201
    payload = response.json()
    assert payload["filename"] == "hello.txt"
    assert payload["content_type"] == "text/plain"
    assert payload["size"] == 11
    assert payload["note"] == "sample text file"
    assert payload["id"]


def test_list_and_get_uploaded_file(client: TestClient) -> None:
    upload_response = client.post(
        "/files",
        files={"file": ("report.csv", b"a,b\n1,2\n", "text/csv")},
    )
    file_id = upload_response.json()["id"]

    list_response = client.get("/files")
    assert list_response.status_code == 200
    assert list_response.json()[0]["id"] == file_id

    detail_response = client.get(f"/files/{file_id}")
    assert detail_response.status_code == 200
    assert detail_response.json()["filename"] == "report.csv"


def test_download_uploaded_file(client: TestClient) -> None:
    upload_response = client.post(
        "/files",
        files={"file": ("notes.md", b"# title", "text/markdown")},
    )
    file_id = upload_response.json()["id"]

    download_response = client.get(f"/files/{file_id}/download")
    assert download_response.status_code == 200
    assert download_response.content == b"# title"
    assert 'filename="notes.md"' in download_response.headers["content-disposition"]


def test_delete_uploaded_file_removes_metadata(client: TestClient) -> None:
    upload_response = client.post(
        "/files",
        files={"file": ("image.png", b"pngdata", "image/png")},
    )
    file_id = upload_response.json()["id"]

    delete_response = client.delete(f"/files/{file_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"deleted": True}

    missing_response = client.get(f"/files/{file_id}")
    assert missing_response.status_code == 404


def test_health_reports_current_file_count(client: TestClient) -> None:
    client.post(
        "/files",
        files={"file": ("a.txt", b"1", "text/plain")},
    )
    client.post(
        "/files",
        files={"file": ("b.txt", b"22", "text/plain")},
    )

    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["file_count"] == 2


def test_unknown_file_returns_404(client: TestClient) -> None:
    response = client.get("/files/missing")
    assert response.status_code == 404
    assert response.json()["detail"] == "File not found"