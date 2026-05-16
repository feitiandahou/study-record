# Python demos

This directory contains independent Python study modules.

## Modules

- `basics/01-asyncio-demo`: compare sequential and concurrent coroutine execution.
- `basics/02-decorator-demo`: demonstrate how decorators wrap and extend functions.
- `fastapi/01-jwt-demo`: minimal JWT login and bearer token flow.
- `fastapi/02-websocket-demo`: minimal WebSocket connect and echo flow.

## With uv

Each demo is an independent `uv` project.

```powershell
cd python/basics/01-asyncio-demo
uv sync
uv run python -m app.main
```

Use the same pattern in any other module directory.

