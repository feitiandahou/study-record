from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_index_page_loads() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "FastAPI WebSocket demo" in response.text


def test_websocket_echo_flow() -> None:
    with client.websocket_connect("/ws") as websocket:
        welcome = websocket.receive_json()
        assert welcome["event"] == "welcome"

        websocket.send_text("hello websocket")
        echoed = websocket.receive_json()
        assert echoed == {
            "event": "echo",
            "message": "server received: hello websocket",
        }