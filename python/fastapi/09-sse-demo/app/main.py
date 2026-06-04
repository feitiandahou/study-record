from datetime import UTC, datetime
from typing import Iterator

from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI(title="SSE Demo", version="0.1.0")

DEFAULT_EVENT_COUNT = 3


def _format_sse(event: str, data: str) -> str:
    return f"event: {event}\ndata: {data}\n\n"


def generate_events(count: int) -> Iterator[str]:
    yield ": connected\n\n"
    for sequence in range(1, count + 1):
        payload = {
            "sequence": sequence,
            "recorded_at": datetime.now(UTC).isoformat(),
        }
        yield _format_sse("tick", str(payload))
    yield _format_sse("complete", "stream finished")


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>FastAPI SSE Demo</title>
    <style>
      body {
        font-family: Consolas, monospace;
        max-width: 760px;
        margin: 40px auto;
        padding: 0 16px;
        line-height: 1.5;
      }
      pre {
        min-height: 220px;
        padding: 16px;
        background: #111827;
        color: #f9fafb;
        border-radius: 12px;
        overflow: auto;
      }
    </style>
  </head>
  <body>
    <h1>Server-Sent Events Demo</h1>
    <p>This page listens to <code>/events</code> using <code>EventSource</code>.</p>
    <pre id="log"></pre>
    <script>
      const log = document.getElementById("log");
      const source = new EventSource("/events?count=5");

      source.onmessage = (event) => {
        log.textContent += `message: ${event.data}\n`;
      };

      source.addEventListener("tick", (event) => {
        log.textContent += `tick: ${event.data}\n`;
      });

      source.addEventListener("complete", (event) => {
        log.textContent += `complete: ${event.data}\n`;
        source.close();
      });

      source.onerror = () => {
        log.textContent += "connection closed\n";
        source.close();
      };
    </script>
  </body>
</html>
"""


@app.get("/events")
def stream_events(count: int = Query(default=DEFAULT_EVENT_COUNT, ge=1, le=10)) -> StreamingResponse:
    return StreamingResponse(generate_events(count), media_type="text/event-stream")


@app.get("/health")
def healthcheck() -> dict[str, int | str]:
    return {
        "status": "ok",
        "default_event_count": DEFAULT_EVENT_COUNT,
        "max_event_count": 10,
    }