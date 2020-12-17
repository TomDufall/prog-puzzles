import pytest

from part2 import play_to_n


@pytest.mark.parametrize(
    ("start_list", "n", "expected"),
    [
        ([0, 3, 6], 30000000, 175594),
        ([1, 3, 2], 30000000, 2578),
        ([2, 1, 3], 30000000, 3544142),
        ([1, 2, 3], 30000000, 261214),
        ([2, 3, 1], 30000000, 6895259),
        ([3, 2, 1], 30000000, 18),
        ([3, 1, 2], 30000000, 362),
    ]
)
def test_play_to_n(start_list, n, expected):
    assert play_to_n(start_list, n) == expected
