from typing import List

import pytest

from part2 import calc_oxygen_rating, calculate_co2_rating, filter_numbers, most_common


@pytest.mark.parametrize(
    ("input_", "expected"),
    [
        (["1", "1", "0"], "1"),
        (["1", "0", "0", "0", "1"], "0"),
        (["1", "0"], "1"),
        (["0"] * 5, "0"),
    ],
)
def test_most_common(input_: List[str], expected: str):
    assert most_common(input_) == expected


def test_filter_numbers():
    input_ = ["110", "111", "010"]
    assert filter_numbers(input_, lambda n: "1") == "111"
    assert filter_numbers(input_, lambda n: "0") == "010"
