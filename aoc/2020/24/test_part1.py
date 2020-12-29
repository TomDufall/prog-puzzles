from pathlib import Path

import pytest

from part1 import calc_coord_from_str, load_black_tiles

SAMPLE_PATH = Path(__file__).parent / "sample_input.txt"


@pytest.mark.parametrize(
    ("input_", "expected"),
    [
        ("esenee", (3, 0)),
        ("esew", (0, -1)),
        ("nwwswee", (0, 0)),
    ]
)
def test_calc_coord_from_str(input_, expected):
    assert calc_coord_from_str(input_) == expected


def test_load_black_tiles():
    assert len(load_black_tiles(SAMPLE_PATH)) == 10
