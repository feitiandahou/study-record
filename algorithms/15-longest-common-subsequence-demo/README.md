# Longest Common Subsequence (LCS) demo

This module demonstrates the Longest Common Subsequence dynamic programming algorithm:

- Finds the longest subsequence common to two sequences (not necessarily contiguous).
- Uses bottom-up DP with space optimization.
- Can reconstruct the actual LCS string in addition to computing its length.
- Time complexity: O(m·n), Space complexity: O(min(m,n)).

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```
