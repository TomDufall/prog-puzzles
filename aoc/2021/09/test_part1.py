from part1 import find_low_points


def test_find_low_point():
    map_ = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]
    expected = [1, 0, 5, 5]
    low_points = find_low_points(map_)
    assert sorted(low_points) == sorted(expected)
