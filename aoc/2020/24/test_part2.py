from pathlib import Path

import pytest

from part1 import load_black_tiles
from part2 import find_neighbours, step

SAMPLE_PATH = Path(__file__).parent / "sample_input.txt"


@pytest.mark.parametrize(
    ("base", "expected"),
    [
        ((0, 0), {(1, 0), (0, -1), (-1, -1), (-1, 0), (0, 1), (1, 1)}),
        ((3, 4), {(4, 4), (3, 3), (2, 3), (2, 4), (3, 5), (4, 5)}),
    ]
)
def test_find_neighbours(base, expected):
    assert set(find_neighbours(base)) == expected


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 10),
        (1, 15),
        (2, 12),
        (3, 25),
        (4, 14),
        (5, 23),
        (6, 28),
        (7, 41),
        (8, 37),
        (9, 49),
        (10, 37),
        (20, 132),
        (30, 259),
        (40, 406),
        (50, 566),
        (60, 788),
        (70, 1106),
        (80, 1373),
        (90, 1844),
        (100, 2208),
    ]
)
def test_step(n, expected):
    initial = load_black_tiles(SAMPLE_PATH)
    assert len(step(initial, n)) == expected
