# Design patterns

This directory contains small, focused design pattern examples.

## Modules

- `01-strategy-demo`: choose different discount strategies at runtime.
- `02-observer-demo`: notify multiple listeners when an order status changes.
- `03-factory-method-demo`: let concrete generators choose different report serializers.
- `04-adapter-demo`: adapt a legacy SMS gateway to a common alert sender interface.
- `05-command-demo`: wrap text editor actions as commands with undo support.
- `06-decorator-demo`: layer notification features like SMS and audit logging around a base sender.
- `07-template-method-demo`: keep a fixed deployment checklist while letting channels format the final summary differently.
- `08-state-demo`: move a publishing workflow through draft, review, and published states.
- `09-chain-of-responsibility-demo`: route support tickets through specialized handlers until one can resolve them.
- `08-state-demo`: move an order through draft, paid, and shipped states while changing allowed actions.
- `09-chain-of-responsibility-demo`: pass support tickets through a handler chain until the right owner resolves them.

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

```powershell
cd design-patterns/04-adapter-demo
uv sync
uv run python -m app.main
```

```powershell
cd design-patterns/05-command-demo
uv sync
uv run python -m app.main
```

```powershell
cd design-patterns/06-decorator-demo
uv sync
uv run python -m app.main
```

```powershell
cd design-patterns/07-template-method-demo
uv sync
uv run python -m app.main
```

```powershell
cd design-patterns/08-state-demo
uv sync
uv run python -m app.main
```

```powershell
cd design-patterns/09-chain-of-responsibility-demo
uv sync
uv run python -m app.main
```

```powershell
cd design-patterns/08-state-demo
uv sync
uv run python -m app.main
```

```powershell
cd design-patterns/09-chain-of-responsibility-demo
uv sync
uv run python -m app.main
```
