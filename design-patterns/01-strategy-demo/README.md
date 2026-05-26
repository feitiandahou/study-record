# Strategy demo

This module demonstrates a minimal Strategy pattern in Python:

- `RegularDiscount`: no discount.
- `VipDiscount`: applies a 20% discount.
- `CheckoutService`: selects the strategy at runtime.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```