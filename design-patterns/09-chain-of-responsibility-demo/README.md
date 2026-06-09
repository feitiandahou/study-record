# Chain of Responsibility demo

This module demonstrates a minimal Chain of Responsibility pattern in Python:

- `SupportHandler`: links handlers together behind a shared interface.
- `BillingHandler`, `TechnicalHandler`, and `DutyManagerHandler`: each decides whether it can resolve a ticket.
- A ticket moves through the chain until one handler takes responsibility.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```