from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse


app = FastAPI(title="WebSocket Demo", version="0.1.0")
app.state.active_connections = 0


HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>WebSocket Demo</title>
    <style>
        body { font-family: sans-serif; margin: 2rem; background: #f7f7f0; color: #1f2937; }
        .panel { max-width: 720px; padding: 1.5rem; background: white; border-radius: 16px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08); }
        h1 { margin-top: 0; }
        #messages { min-height: 220px; padding: 1rem; border-radius: 12px; background: #111827; color: #f9fafb; overflow: auto; }
        form { display: flex; gap: 0.75rem; margin-top: 1rem; }
        input { flex: 1; padding: 0.8rem 1rem; border: 1px solid #d1d5db; border-radius: 999px; }
        button { padding: 0.8rem 1.2rem; border: none; border-radius: 999px; background: #0f766e; color: white; cursor: pointer; }
        .hint { color: #4b5563; }
    </style>
</head>
<body>
    <main class="panel">
        <h1>FastAPI WebSocket demo</h1>
        <p class="hint">The page connects to <code>/ws</code>, receives a welcome event, and echoes what you send.</p>
        <div id="messages"></div>
        <form id="chat-form">
            <input id="message-input" autocomplete="off" placeholder="Type a message" />
            <button type="submit">Send</button>
        </form>
    </main>
    <script>
        const messages = document.getElementById("messages");
        const form = document.getElementById("chat-form");
        const input = document.getElementById("message-input");
        const socket = new WebSocket(`ws://${location.host}/ws`);

        function appendMessage(text) {
            const line = document.createElement("p");
            line.textContent = text;
            messages.appendChild(line);
            messages.scrollTop = messages.scrollHeight;
        }

        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            appendMessage(`${data.event}: ${data.message}`);
        };

        socket.onopen = () => appendMessage("socket: connected");
        socket.onclose = () => appendMessage("socket: disconnected");

        form.addEventListener("submit", (event) => {
            event.preventDefault();
            if (!input.value.trim()) {
                return;
            }
            socket.send(input.value);
            input.value = "";
        });
    </script>
</body>
</html>
"""


@app.get("/")
async def index() -> HTMLResponse:
    return HTMLResponse(HTML_PAGE)


@app.get("/health")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await websocket.accept()
    app.state.active_connections += 1

    await websocket.send_json(
        {
            "event": "welcome",
            "message": f"connected clients: {app.state.active_connections}",
        }
    )

    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_json(
                {
                    "event": "echo",
                    "message": f"server received: {message}",
                }
            )
    except WebSocketDisconnect:
        pass
    finally:
        app.state.active_connections -= 1
