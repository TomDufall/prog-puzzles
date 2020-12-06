import pytest

from part1 import count_total_group_answers, merge_strings


@pytest.mark.parametrize(
    ("input_", "expected"),
    [
        (
            ["abcx", "abcy", "abcz"],
            "abcxyz"
        ),
        (
            ["abc"],
            "abc"
        ),
        (
            ["a", "b", "c"],
            "abc"
        ),
        (
            ["ab", "ac"],
            "abc"
        ),
        (
            ["a", "a", "a", "a"],
            "a"
        ),
        (
            ["cady", "ipldcyf", "xybgcd", "gcdy", "dygbc"],
            "abcdfgilpxy"
        )
    ]
)
def test_merge_strings(input_, expected):
    assert "".join(sorted(set(merge_strings(input_)))) == expected


@pytest.mark.parametrize(
    ("groups", "expected"),
    [
        (
            [
                ["abc"],
                ["a", "b", "c"],
                ["ab", "ac"],
                ["a", "a", "a", "a"],
                ["b"],
            ],
            11
        )
    ]
)
def test_count_total_group_answers(groups, expected):
    assert count_total_group_answers(groups) == expected
