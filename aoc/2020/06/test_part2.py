import pytest

from part2 import count_total_group_answers, merge_strings


@pytest.mark.parametrize(
    ("input_", "expected"),
    [
        (
            ["abcx", "abcy", "abcz"],
            "abc"
        ),
        (
            ["abc"],
            "abc"
        ),
        (
            ["a", "b", "c"],
            ""
        ),
        (
            ["ab", "ac"],
            "a"
        ),
        (
            ["a", "a", "a", "a"],
            "a"
        ),
        (
            ["cady", "ipldcyf", "xybgcd", "gcdy", "dygbc"],
            "cdy"
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
            6
        )
    ]
)
def test_count_total_group_answers(groups, expected):
    assert count_total_group_answers(groups) == expected
