from __future__ import annotations

from functools import reduce
from itertools import product
from operator import mul

from part1 import load_input


def find_low_points(map_: list[list[int]]) -> list[tuple[tuple[int, int], int]]:
    low_points: list[tuple[tuple[int, int], int]] = []
    for x, y in product(range(len(map_[0])), range(len(map_))):
        is_low = True
        for xdiff, ydiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x2, y2 = x + xdiff, y + ydiff
            if x2 >= 0 and y2 >= 0 and x2 < len(map_[0]) and y2 < len(map_):
                if map_[y2][x2] <= map_[y][x]:
                    is_low = False
                    break
        if is_low:
            low_points.append(((x, y), map_[y][x]))
    return low_points


def find_basins(map_: list[list[int]]) -> list[list[tuple[int, int]]]:
    low_points = find_low_points(map_)
    basins: list[list[tuple[int, int]]] = []

    for low_point, _ in low_points:
        basin = {low_point}
        to_search = {low_point}
        while len(to_search) > 0:
            x, y = to_search.pop()
            for xdiff, ydiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x2, y2 = x + xdiff, y + ydiff
                if x2 >= 0 and y2 >= 0 and x2 < len(map_[0]) and y2 < len(map_):
                    if 9 > map_[y2][x2] >= map_[y][x]:
                        if (x2, y2) not in basin:
                            basin.add((x2, y2))
                            to_search.add((x2, y2))
        basins.append(basin)

    return basins


def load_input(filepath: str = "input.txt") -> list[list[int]]:
    with open(filepath) as f:
        parse_line = lambda line: [int(n) for n in line]
        return list(map(parse_line, f.read().splitlines()))


if __name__ == "__main__":
    map_ = load_input()
    basins = find_basins(map_)
    largest_basins = sorted(map(len, basins), reverse=True)
    print(
        reduce(
            mul,
            largest_basins[:3],
        )
    )
