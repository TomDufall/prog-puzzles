from pathlib import Path

import pytest

from part1 import different_sum_pair_exists, find_error

@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([1, 2, 3, 4, 5], 6, True),
        ([1, 2, 3, 4, 5], 10, False),
        ([1, 2, 3, 4, 5, 5], 10, False),
        ([1, 2, 3, 4, 5, 6], 10, True),
    ]
)
def test_different_sum_pair_exists(nums, target, expected):
    assert different_sum_pair_exists(nums, target) == expected


def test_find_error():
    filepath = Path(__file__).parent / "sample_input.txt"
    datastream = map(int, filepath.read_text().splitlines())
    assert find_error(datastream, 5) == 127
