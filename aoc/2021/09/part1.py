from __future__ import annotations

from itertools import product


def find_low_points(map_: list[list[int]]) -> list[int]:
    low_points: list[int] = []
    for x, y in product(range(len(map_[0])), range(len(map_))):
        is_low = True
        for xdiff, ydiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x2, y2 = x + xdiff, y + ydiff
            if x2 >= 0 and y2 >= 0 and x2 < len(map_[0]) and y2 < len(map_):
                if map_[y2][x2] <= map_[y][x]:
                    is_low = False
                    break
        if is_low:
            low_points.append(map_[y][x])
    return low_points


def load_input(filepath: str = "input.txt") -> list[list[int]]:
    with open(filepath) as f:
        parse_line = lambda line: [int(n) for n in line]
        return list(map(parse_line, f.read().splitlines()))


if __name__ == "__main__":
    map_ = load_input()
    low_points = find_low_points(map_)
    risk_levels = [x + 1 for x in low_points]
    print(sum(risk_levels))
