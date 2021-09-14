from pathlib import Path

import pytest
import pytest_mock  # noqa: F401

from part2 import (
    Password,
    UpdatedPasswordPolicy,
    count_valid_passwords,
    load_input_new_format,
)


class TestUpdatedPasswordPolicy:
    def test_init(self):
        UpdatedPasswordPolicy(1, 3, "a")

    @pytest.mark.parametrize(
        ("index_1", "index_2", "char", "password", "expected"),
        [
            (1, 3, "a", "edam", True),
            (1, 3, "a", "dog", False),
            (1, 4, "a", "armada", False),
            (1, 3, "b", "adam", False),
        ]
    )
    def test_match(self, index_1, index_2, char, password, expected):
        policy = UpdatedPasswordPolicy(index_1, index_2, char)
        assert policy.match(password) == expected


def test_count_valid_passwords():
    passwords = load_input_new_format(Path("sample_input.txt"))
    assert count_valid_passwords(passwords) == 2


def test_load_input_new_format():
    filepath = Path(__file__).parent / "sample_input.txt"
    expected = [
        Password(
            UpdatedPasswordPolicy(1, 3, "a"),
            "asdf"
        ),
        Password(
            UpdatedPasswordPolicy(2, 5, "b"),
            "aaabbbbaaab"
        ),
        Password(
            UpdatedPasswordPolicy(2, 4, "c"),
            "accca"
        ),
        Password(
            UpdatedPasswordPolicy(1, 2, "d"),
            "ghjkl"
        ),
    ]
    assert load_input_new_format(filepath) == expected
