from app.main import lcs_length, lcs_string


def test_lcs_length_basic() -> None:
    assert lcs_length("abcde", "ace") == 3


def test_lcs_length_identical_strings() -> None:
    assert lcs_length("abc", "abc") == 3


def test_lcs_length_no_common_subsequence() -> None:
    assert lcs_length("abc", "xyz") == 0


def test_lcs_length_one_empty_string() -> None:
    assert lcs_length("abc", "") == 0
    assert lcs_length("", "xyz") == 0


def test_lcs_length_both_empty() -> None:
    assert lcs_length("", "") == 0


def test_lcs_string_basic() -> None:
    result = lcs_string("abcde", "ace")
    assert result == "ace"


def test_lcs_string_aggtab() -> None:
    result = lcs_string("AGGTAB", "GXTXAYB")
    assert result == "GTAB"
    assert len(result) == 4


def test_lcs_string_no_common() -> None:
    result = lcs_string("abc", "xyz")
    assert result == ""


def test_lcs_string_empty() -> None:
    assert lcs_string("", "abc") == ""
    assert lcs_string("abc", "") == ""


def test_lcs_string_single_char() -> None:
    assert lcs_string("a", "a") == "a"
    assert lcs_string("a", "b") == ""


def test_lcs_string_one_substring() -> None:
    result = lcs_string("abc", "abc")
    assert result == "abc"


def test_lcs_length_longer_strings() -> None:
    # Longer string test
    text1 = "ABCDGH"
    text2 = "AEDFHR"
    result = lcs_length(text1, text2)
    assert result == 3


def test_lcs_string_longer_strings() -> None:
    text1 = "ABCDGH"
    text2 = "AEDFHR"
    result = lcs_string(text1, text2)
    assert result == "ADH"
