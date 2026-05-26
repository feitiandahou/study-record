import asyncio
import importlib
import json
import os
from contextlib import asynccontextmanager
from dataclasses import dataclass
from json import JSONDecodeError
from typing import Any, Literal, cast

from fastapi import FastAPI
from pydantic import BaseModel, Field


@dataclass(slots=True)
class AppSettings:
    backend: Literal["memory", "kafka"]
    bootstrap_servers: str
    topic: str
    group_id: str
    client_id: str
    history_limit: int


class EventPublishRequest(BaseModel):
    key: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)


class EventRecord(BaseModel):
    topic: str
    key: str | None
    payload: dict[str, Any]
    source: Literal["memory", "kafka"]
    offset: int


class PublishResult(BaseModel):
    status: Literal["queued"] = "queued"
    backend: Literal["memory", "kafka"]
    topic: str
    offset: int


class RuntimeConfig(BaseModel):
    backend: Literal["memory", "kafka"]
    bootstrap_servers: str
    topic: str
    group_id: str
    history_limit: int


def load_settings() -> AppSettings:
    backend_value = os.getenv("KAFKA_BACKEND", "memory").strip().lower() or "memory"
    if backend_value not in {"memory", "kafka"}:
        backend_value = "memory"
    backend = cast(Literal["memory", "kafka"], backend_value)

    return AppSettings(
        backend=backend,
        bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "127.0.0.1:9092"),
        topic=os.getenv("KAFKA_TOPIC", "study-record.demo"),
        group_id=os.getenv("KAFKA_GROUP_ID", "study-record-fastapi-demo"),
        client_id=os.getenv("KAFKA_CLIENT_ID", "study-record-fastapi-app"),
        history_limit=int(os.getenv("KAFKA_HISTORY_LIMIT", "20")),
    )


def decode_payload(raw_value: bytes) -> dict[str, Any]:
    text = raw_value.decode("utf-8")
    try:
        data = json.loads(text)
    except JSONDecodeError:
        return {"raw": text}

    if isinstance(data, dict):
        return data
    return {"value": data}


class InMemoryEventBus:
    def __init__(self, settings: AppSettings):
        self.settings = settings
        self._records: list[EventRecord] = []
        self._next_offset = 0

    async def start(self) -> None:
        return None

    async def stop(self) -> None:
        return None

    async def publish(self, event: EventPublishRequest) -> int:
        self._next_offset += 1
        self._remember(
            EventRecord(
                topic=self.settings.topic,
                key=event.key,
                payload=event.payload,
                source="memory",
                offset=self._next_offset,
            )
        )
        return self._next_offset

    def list_records(self) -> list[EventRecord]:
        return list(self._records)

    def _remember(self, record: EventRecord) -> None:
        self._records.append(record)
        if len(self._records) > self.settings.history_limit:
            self._records = self._records[-self.settings.history_limit :]


class KafkaEventBus:
    def __init__(self, settings: AppSettings):
        self.settings = settings
        self._records: list[EventRecord] = []
        self._producer: Any = None
        self._consumer: Any = None
        self._consumer_task: asyncio.Task[None] | None = None

    async def start(self) -> None:
        try:
            aiokafka_module = importlib.import_module("aiokafka")
        except ImportError as exc:
            raise RuntimeError("aiokafka is not installed. Run 'uv sync' before using kafka mode.")

        producer = aiokafka_module.AIOKafkaProducer(
            bootstrap_servers=self.settings.bootstrap_servers,
            client_id=self.settings.client_id,
        )
        consumer = aiokafka_module.AIOKafkaConsumer(
            self.settings.topic,
            bootstrap_servers=self.settings.bootstrap_servers,
            group_id=self.settings.group_id,
            auto_offset_reset="earliest",
        )

        await producer.start()
        await consumer.start()
        self._producer = producer
        self._consumer = consumer
        self._consumer_task = asyncio.create_task(self._consume_loop())

    async def stop(self) -> None:
        if self._consumer_task is not None:
            self._consumer_task.cancel()
            try:
                await self._consumer_task
            except asyncio.CancelledError:
                pass

        if self._consumer is not None:
            await self._consumer.stop()

        if self._producer is not None:
            await self._producer.stop()

    async def publish(self, event: EventPublishRequest) -> int:
        if self._producer is None:
            raise RuntimeError("Kafka producer is not started")

        metadata = await self._producer.send_and_wait(
            self.settings.topic,
            json.dumps(event.payload).encode("utf-8"),
            key=event.key.encode("utf-8") if event.key else None,
        )
        return metadata.offset

    def list_records(self) -> list[EventRecord]:
        return list(self._records)

    async def _consume_loop(self) -> None:
        if self._consumer is None:
            return

        async for message in self._consumer:
            key = message.key.decode("utf-8") if message.key else None
            record = EventRecord(
                topic=message.topic,
                key=key,
                payload=decode_payload(message.value),
                source="kafka",
                offset=message.offset,
            )
            self._records.append(record)
            if len(self._records) > self.settings.history_limit:
                self._records = self._records[-self.settings.history_limit :]


def build_event_bus(settings: AppSettings) -> InMemoryEventBus | KafkaEventBus:
    if settings.backend == "kafka":
        return KafkaEventBus(settings)
    return InMemoryEventBus(settings)


settings = load_settings()


@asynccontextmanager
async def lifespan(application: FastAPI):
    event_bus = build_event_bus(settings)
    application.state.settings = settings
    application.state.event_bus = event_bus
    await event_bus.start()
    try:
        yield
    finally:
        await event_bus.stop()


app = FastAPI(title="Kafka Demo", version="0.1.0", lifespan=lifespan)


@app.get("/health")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok", "backend": settings.backend}


@app.get("/config", response_model=RuntimeConfig)
async def get_config() -> RuntimeConfig:
    return RuntimeConfig(
        backend=settings.backend,
        bootstrap_servers=settings.bootstrap_servers,
        topic=settings.topic,
        group_id=settings.group_id,
        history_limit=settings.history_limit,
    )


@app.post("/events", response_model=PublishResult)
async def publish_event(event: EventPublishRequest) -> PublishResult:
    offset = await app.state.event_bus.publish(event)
    return PublishResult(
        backend=settings.backend,
        topic=settings.topic,
        offset=offset,
    )


@app.get("/events", response_model=list[EventRecord])
async def list_events() -> list[EventRecord]:
    return app.state.event_bus.list_records()