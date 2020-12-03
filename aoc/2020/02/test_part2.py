from pathlib import Path

import pytest
import pytest_mock

from part2 import Password, OriginalPasswordPolicy, UpdatedPasswordPolicy
from part2 import (
    count_valid_passwords, load_input_old_format, load_input_new_format
)


class TestOriginalPasswordPolicy:
    def test_init(self):
        OriginalPasswordPolicy(1, 3, "a")

    @pytest.mark.parametrize(
        ("min_", "max_", "char", "password", "expected"),
        [
            (1, 1, "a", "edam", True),
            (1, 1, "a", "dog", False),
            (1, 3, "a", "armada", True),
            (1, 3, "a", "adam", True),
            (1, 1, "n", "banana", False),
        ]
    )
    def test_match(self, min_, max_, char, password, expected):
        policy = OriginalPasswordPolicy(min_, max_, char)
        assert policy.match(password) == expected


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


class TestPassword:
    @pytest.mark.parametrize("expected", [True, False])
    def test_match_old_format(self, mocker, expected):
        policy = mocker.MagicMock()
        policy.match.return_value = expected
        password = Password(policy, "password")
        assert password.validate() == expected
        policy.match.assert_called_once_with("password")


def test_count_valid_passwords():
    passwords = load_input_old_format(Path("sample_input.txt"))
    assert count_valid_passwords(passwords) == 3


def test_load_input_old_format():
    filepath = Path(__file__).parent / "sample_input.txt"
    expected = [
        Password(
            OriginalPasswordPolicy(1, 3, "a"),
            "asdf"
        ),
        Password(
            OriginalPasswordPolicy(2, 5, "b"),
            "aaabbbbaaab"
        ),
        Password(
            OriginalPasswordPolicy(2, 7, "c"),
            "accca"
        ),
        Password(
            OriginalPasswordPolicy(1, 2, "d"),
            "ghjkl"
        ),
    ]
    assert load_input_old_format(filepath) == expected


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
            UpdatedPasswordPolicy(2, 7, "c"),
            "accca"
        ),
        Password(
            UpdatedPasswordPolicy(1, 2, "d"),
            "ghjkl"
        ),
    ]
    assert load_input_new_format(filepath) == expected
