# Design patterns

This directory contains small, focused design pattern examples.

## Modules

- `01-strategy-demo`: choose different discount strategies at runtime.
- `02-observer-demo`: notify multiple listeners when an order status changes.
- `03-factory-method-demo`: let concrete generators choose different report serializers.

## With uv

```powershell
cd design-patterns/01-strategy-demo
uv sync
uv run python -m app.main
```

```powershell
cd design-patterns/02-observer-demo
uv sync
uv run python -m app.main
```

```powershell
cd design-patterns/03-factory-method-demo
uv sync
uv run python -m app.main
```