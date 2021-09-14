from part1 import TobogganMap

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


def test_traverse():
    map_ = TobogganMap(SAMPLE_INPUT)
    assert map_.traverse((3, 1), (0, 0)) == 7
