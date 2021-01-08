import pytest

from part1 import calc_seat_id, decode_pass


@pytest.mark.parametrize(
    ("seat_str", "expected_row", "expected_column"),
    [
        ("FBFBBFFRLR", 44, 5),
        ("BFFFBBFRRR", 70, 7),
        ("FFFBBBFRRR", 14, 7),
        ("BBFFBBFRLL", 102, 4),
    ]
)
def test_decode_pass(seat_str, expected_row, expected_column):
    assert decode_pass(seat_str) == (expected_row, expected_column)


@pytest.mark.parametrize(
    ("row", "column", "expected_id"),
    [
        (44, 5, 357),
        (70, 7, 567),
        (14, 7, 119),
        (102, 4, 820),
    ]
)
def test_calc_seat_id(row, column, expected_id):
    assert calc_seat_id((row, column)) == expected_id
