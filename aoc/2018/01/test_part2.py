import pytest

from part2 import find_common_frequency


@pytest.mark.parametrize(
    ("deltas", "expected"),
    [
        (["+1", "-1"], 0),
        (["+3", "+3", "+4", "-2", "-4"], 10),
        (["-6", "+3", "+8", "+5", "-6"], 5),
        (["+7", "+7", "-2", "-7", "-4"], 14),
    ],
)
def test_find_common_frequency(deltas, expected):
    assert find_common_frequency(deltas) == expected