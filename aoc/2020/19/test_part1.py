from pathlib import Path

import pytest

from part1 import load_input, Rules


class TestRules():
    @pytest.mark.parametrize(
        ("case", "expected"),
        [
            ("ababbb", True),
            ("bababa", False),
            ("abbbab", True),
            ("aaabbb", False),
            ("aaaabbb", False),
        ]
    )
    def test_validate(self, case, expected):
        rules = Rules(
            {
                0: "4 1 5",
                1: "2 3 | 3 2",
                2: "4 4 | 5 5",
                3: "4 5 | 5 4",
                4: '"a"',
                5: '"b"',
            }
        )
        assert rules.validate(case) == expected

    def test_count_valid(self):
        rules = Rules(
            {
                0: "4 1 5",
                1: "2 3 | 3 2",
                2: "4 4 | 5 5",
                3: "4 5 | 5 4",
                4: '"a"',
                5: '"b"',
            }
        )
        cases = [
            "ababbb",
            "bababa",
            "abbbab",
            "aaabbb",
            "aaaabbb",
        ]
        assert rules.count_valid(cases) == 2


def test_load_input():
    sample_path = Path(__file__).parent / "sample_input_1.txt"
    expected_rules = Rules(
        {
            0: "4 1 5",
            1: "2 3 | 3 2",
            2: "4 4 | 5 5",
            3: "4 5 | 5 4",
            4: '"a"',
            5: '"b"',
        }
    )
    expected_cases = [
        "ababbb",
        "bababa",
        "abbbab",
        "aaabbb",
        "aaaabbb",
    ]
    expected = (expected_rules, expected_cases)
    assert load_input(sample_path) == expected
