from part1 import TobogganMap
from part2 import multiply_collisions

import pytest

SAMPLE_INPUT = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


@pytest.mark.parametrize(
    ("vector", "expected"),
    [
        ((1, 1), 2),
        ((3, 1), 7),
        ((5, 1), 3),
        ((7, 1), 4),
        ((1, 2), 2),
    ]
)
def test_traverse(vector, expected):
    map_ = TobogganMap(SAMPLE_INPUT)
    assert map_.traverse(vector, (0, 0)) == expected


def test_multiply_collisions():
    map_ = TobogganMap(SAMPLE_INPUT)
    cases = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    assert multiply_collisions(map_, cases) == 336
