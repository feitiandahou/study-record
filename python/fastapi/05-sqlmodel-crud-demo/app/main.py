from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from sqlmodel import Field, Session, SQLModel, create_engine, select

# ---------------------------------------------------------------------------
# Database setup
# ---------------------------------------------------------------------------

DATABASE_URL = "sqlite:///./notes.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: ANN001
    create_db_and_tables()
    yield


# ---------------------------------------------------------------------------
# Models & Schemas
# ---------------------------------------------------------------------------


class NoteBase(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = Field(default="")


class Note(NoteBase, table=True):
    """ORM table model — also acts as the read/response schema."""

    id: int | None = Field(default=None, primary_key=True)


class NoteCreate(NoteBase):
    """Write schema (no id field)."""


class NoteUpdate(SQLModel):
    """Partial-update schema — all fields optional."""

    title: str | None = Field(default=None, min_length=1, max_length=200)
    content: str | None = None


# ---------------------------------------------------------------------------
# App & dependency
# ---------------------------------------------------------------------------

app = FastAPI(title="SQLModel CRUD Demo", version="0.1.0", lifespan=lifespan)


def get_session():  # noqa: ANN201
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.post("/notes", response_model=Note, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate, session: SessionDep) -> Note:
    db_note = Note.model_validate(note)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note


@app.get("/notes", response_model=list[Note])
def list_notes(session: SessionDep) -> list[Note]:
    return list(session.exec(select(Note)).all())


@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int, session: SessionDep) -> Note:
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note


@app.patch("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, update: NoteUpdate, session: SessionDep) -> Note:
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    note.sqlmodel_update(update.model_dump(exclude_unset=True))
    session.add(note)
    session.commit()
    session.refresh(note)
    return note


@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, session: SessionDep) -> None:
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    session.delete(note)
    session.commit()


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
