"""Longest Common Subsequence (LCS) algorithm using dynamic programming."""


def lcs_length(text1: str, text2: str) -> int:
    """
    Compute the length of the longest common subsequence.

    Args:
        text1: First string.
        text2: Second string.

    Returns:
        Length of the LCS.
    """
    m, n = len(text1), len(text2)

    # dp[i][j] = LCS length for text1[:i] and text2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs_string(text1: str, text2: str) -> str:
    """
    Reconstruct the actual longest common subsequence string.

    Args:
        text1: First string.
        text2: Second string.

    Returns:
        The LCS string.
    """
    m, n = len(text1), len(text2)

    # Build DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS
    lcs = []
    i, j = m, n

    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs))


def main() -> None:
    """Demonstrate LCS algorithm."""
    text1 = "abcde"
    text2 = "ace"

    length = lcs_length(text1, text2)
    lcs = lcs_string(text1, text2)

    print(f"text1={text1}")
    print(f"text2={text2}")
    print(f"LCS length={length}")
    print(f"LCS string={lcs}")

    # More examples
    examples = [
        ("AGGTAB", "GXTXAYB"),
        ("HELLO", "WORLD"),
        ("ABC", "ABC"),
        ("", "ABC"),
    ]

    print("\nMore examples:")
    for s1, s2 in examples:
        length = lcs_length(s1, s2)
        lcs = lcs_string(s1, s2)
        print(f"  lcs({s1!r}, {s2!r}) = {lcs!r} (length={length})")


if __name__ == "__main__":
    main()
