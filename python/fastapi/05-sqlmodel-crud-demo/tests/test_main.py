import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from app.main import app, get_session


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(name="client")
def client_fixture():
    """Provide a TestClient backed by a fresh in-memory SQLite database."""
    test_engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(test_engine)

    def get_session_override():
        with Session(test_engine) as session:
            yield session

    app.dependency_overrides[get_session] = get_session_override
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_create_note(client: TestClient) -> None:
    response = client.post("/notes", json={"title": "Hello", "content": "World"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Hello"
    assert data["content"] == "World"
    assert isinstance(data["id"], int)


def test_list_notes(client: TestClient) -> None:
    client.post("/notes", json={"title": "A", "content": "1"})
    client.post("/notes", json={"title": "B", "content": "2"})
    response = client.get("/notes")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_note(client: TestClient) -> None:
    note_id = client.post("/notes", json={"title": "Read me", "content": "ok"}).json()["id"]
    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Read me"


def test_partial_update_note(client: TestClient) -> None:
    note_id = client.post("/notes", json={"title": "Old", "content": "Keep"}).json()["id"]
    response = client.patch(f"/notes/{note_id}", json={"title": "New"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New"
    assert data["content"] == "Keep"  # untouched field preserved


def test_delete_note(client: TestClient) -> None:
    note_id = client.post("/notes", json={"title": "Bye", "content": ""}).json()["id"]
    assert client.delete(f"/notes/{note_id}").status_code == 204
    assert client.get(f"/notes/{note_id}").status_code == 404


def test_get_nonexistent_note(client: TestClient) -> None:
    assert client.get("/notes/99999").status_code == 404


def test_update_nonexistent_note(client: TestClient) -> None:
    assert client.patch("/notes/99999", json={"title": "Ghost"}).status_code == 404


def test_health(client: TestClient) -> None:
    assert client.get("/health").status_code == 200
