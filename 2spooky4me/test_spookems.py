import pytest

from spookems import change_spookiness


@pytest.mark.parametrize(
    ("text", "operation", "expected"),
    [
        ("2spooky4me", "+2", "4spooky6me"),
        ("2spooky4me", "-2", "0spooky2me"),
        ("2spooky4me", "*6", "12spooky24me"),
        ("2spooky4me", "/2", "1spooky2me"),
        ("2spooky4me", "^2", "4spooky16me"),
        ("2spooky4me", "*-3", "-6spooky-12me"),
        ("2spooky4me", "/-2", "-1spooky-2me"),
        ("2spooky4me", "+-1", "1spooky3me"),
        ("2spooky4me", "--3", "5spooky7me"),
        ("me", "+2", "me"),
        ("me", "/2", "me"),
        ("8", "^2", "64"),
        ("", "/2", ""),
        ("me2spooky", "*4", "me8spooky"),
        ("10for10", "/2", "5for5"),
        ("3spooky7me", "/2", "1spooky3me"),
    ],
)
def test_change_spookiness(text, operation, expected):
    assert change_spookiness(text, operation) == expected
