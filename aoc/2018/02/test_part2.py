import pytest

from part2 import is_close_match


@pytest.mark.parametrize(
    ("str_1", "str_2", "expected"),
    [
        ["abcd", "abcd", True],
        ["abcd", "abdd", True],
        ["abcd", "abdc", False],
        ["aa", "bb", False],
        ["a", "b", True],
    ],
)
def test_is_close_match(str_1: str, str_2: str, expected: bool):
    assert is_close_match(str_1, str_2) == expected
