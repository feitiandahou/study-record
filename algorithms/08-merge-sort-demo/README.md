# Merge Sort demo

This module demonstrates a minimal merge sort implementation in Python:

- Divide the list into two halves recursively until each sublist has one element.
- Merge sorted sublists back in order to produce the final sorted list.
- Time complexity O(n log n), space complexity O(n).

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```
