# Kafka demo

This module demonstrates a minimal FastAPI and Kafka integration flow:

- `POST /events`: publish a JSON message.
- `GET /events`: inspect the most recent consumed messages.
- `GET /config`: inspect the active backend and topic settings.

The demo supports two modes:

- `memory` mode: default, no external Kafka required, useful for local study and tests.
- `kafka` mode: uses `aiokafka` producer and consumer against a real Kafka broker.

## Run

Default local mode:

```powershell
uv sync
uv run uvicorn app.main:app --reload
```

Real Kafka mode:

```powershell
$env:KAFKA_BACKEND = "kafka"
$env:KAFKA_BOOTSTRAP_SERVERS = "127.0.0.1:9092"
$env:KAFKA_TOPIC = "study-record.demo"
uv sync
uv run uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to publish messages and inspect the latest consumed records.

## What To Observe

- In `memory` mode, published messages are appended directly to the in-process history.
- In `kafka` mode, `POST /events` sends to Kafka and a background consumer appends consumed records to the same history buffer.

## Test

```powershell
uv run pytest
```