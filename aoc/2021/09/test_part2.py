from part2 import find_basins


def test_find_basins():
    map_ = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]
    basins = find_basins(map_)
    largest_basins = sorted(map(len, basins), reverse=True)
    assert largest_basins[:3] == [14, 9, 9]
