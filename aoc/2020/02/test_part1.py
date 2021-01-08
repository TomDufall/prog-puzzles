from pathlib import Path

import pytest
import pytest_mock  # noqa: F401

from part1 import Password, PasswordPolicy
from part1 import count_valid_passwords, load_input


class TestPasswordPolicy:
    def test_init(self):
        PasswordPolicy(1, 3, "a")

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
        policy = PasswordPolicy(min_, max_, char)
        assert policy.match(password) == expected


class TestPassword:
    @pytest.mark.parametrize("expected", [True, False])
    def test_match_old_format(self, mocker, expected):
        policy = mocker.MagicMock()
        policy.match.return_value = expected
        password = Password(policy, "password")
        assert password.validate() == expected
        policy.match.assert_called_once_with("password")


def test_count_valid_passwords(mocker):
    mock_1 = mocker.MagicMock()
    mock_1.validate.return_value = True
    mock_2 = mocker.MagicMock()
    mock_2.validate.return_value = False
    passwords = [mock_1, mock_2, mock_1]
    assert count_valid_passwords(passwords) == 2


def test_count_valid_passwords_sample_data():
    passwords = load_input(Path("sample_input.txt"))
    assert count_valid_passwords(passwords) == 3


def test_load_input():
    filepath = Path(__file__).parent / "sample_input.txt"
    expected = [
        Password(
            PasswordPolicy(1, 3, "a"),
            "asdf"
        ),
        Password(
            PasswordPolicy(2, 5, "b"),
            "aaabbbbaaab"
        ),
        Password(
            PasswordPolicy(2, 4, "c"),
            "accca"
        ),
        Password(
            PasswordPolicy(1, 2, "d"),
            "ghjkl"
        ),
    ]
    assert load_input(filepath) == expected
