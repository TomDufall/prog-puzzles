from part1 import find_shortest_path
from part2 import generate_grid
from test_part1 import GRID


def test_generate_grid():
    tile = [[3]]
    expected = [
        [3, 4, 5, 6, 7],
        [4, 5, 6, 7, 8],
        [5, 6, 7, 8, 9],
        [6, 7, 8, 9, 1],
        [7, 8, 9, 1, 2],
    ]
    actual = generate_grid(tile)
    for i, row in enumerate(expected):
        assert actual[i] == row


def test_generate_grid_2():
    tile = [[3, 1], [2, 4]]
    expected = [
        [3, 1, 4, 2, 5, 3, 6, 4, 7, 5],
        [2, 4, 3, 5, 4, 6, 5, 7, 6, 8],
        [4, 2, 5, 3, 6, 4, 7, 5, 8, 6],
        [3, 5, 4, 6, 5, 7, 6, 8, 7, 9],
        [5, 3, 6, 4, 7, 5, 8, 6, 9, 7],
        [4, 6, 5, 7, 6, 8, 7, 9, 8, 1],
        [6, 4, 7, 5, 8, 6, 9, 7, 1, 8],
        [5, 7, 6, 8, 7, 9, 8, 1, 9, 2],
        [7, 5, 8, 6, 9, 7, 1, 8, 2, 9],
        [6, 8, 7, 9, 8, 1, 9, 2, 1, 3],
    ]

    actual = generate_grid(tile)
    for i, row in enumerate(expected):
        assert actual[i] == row


def test_find_shortest_path():
    grid = generate_grid(GRID)
    assert find_shortest_path(grid) == 315
