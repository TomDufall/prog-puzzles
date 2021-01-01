import pytest

from part1 import break_handshake, handshake, transform


@pytest.mark.parametrize(
    ("subject_number", "loop_size", "expected"),
    [
        (7, 8, 5764801),
        (7, 11, 17807724),
        (17807724, 8, 14897079),
        (5764801, 11, 14897079),
    ]
)
def test_transform(subject_number, loop_size, expected):
    assert transform(subject_number, loop_size) == expected


def test_handshake():
    assert handshake(8, 11) == 14897079


def test_break_handshake():
    assert break_handshake(5764801, 17807724) == 14897079
