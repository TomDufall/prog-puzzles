from __future__ import annotations

from itertools import chain


def _neighbours(x, y, max_x, max_y) -> list[tuple[int, int]]:
    diffs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    return [
        (x + xdiff, y + ydiff)
        for xdiff, ydiff in diffs
        if 0 <= x + xdiff <= max_x and 0 <= y + ydiff <= max_y
    ]


def find_shortest_path(grid: list[list[int]], iter_limit=10000) -> int:
    start = 0, 0
    end = len(grid[0]) - 1, len(grid) - 1
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1
    seen_start: dict[tuple[int, int], int] = {}
    visited_start: dict[tuple[int, int], int] = {start: 0}
    seen_end: dict[tuple[int, int], int] = {}
    visited_end: dict[tuple[int, int], int] = {end: grid[end[1]][end[0]]}
    for x, y in _neighbours(*start, max_x, max_y):
        seen_start[x, y] = grid[y][x] + visited_start[start]
    for x, y in _neighbours(*end, max_x, max_y):
        seen_end[x, y] = visited_end[end] + grid[y][x]

    i = 0
    while True:
        i += 1
        if i > iter_limit:
            raise Exception("Ran for too long - quitting")
        next_ = min(
            chain(seen_start.items(), seen_end.items()),
            key=lambda item: item[1],
        )[0]
        if next_ in seen_start and next_ in visited_end:
            return seen_start[next_] + visited_end[next_] - grid[next_[1]][next_[0]]
        elif next_ in seen_end and next_ in visited_start:
            return seen_end[next_] + visited_start[next_] - grid[next_[1]][next_[0]]
        elif next_ in seen_start:
            visited_start[next_] = seen_start.pop(next_)
            for x, y in _neighbours(*next_, max_x, max_y):
                distance = visited_start[next_] + grid[y][x]
                if (x, y) in visited_start:
                    continue
                if (x, y) in seen_start and distance >= seen_start[(x, y)]:
                    continue
                seen_start[(x, y)] = distance
        elif next_ in seen_end:
            visited_end[next_] = seen_end.pop(next_)
            for x, y in _neighbours(*next_, max_x, max_y):
                distance = visited_end[next_] + grid[y][x]
                if (x, y) in visited_end:
                    continue
                if (x, y) in seen_end and distance >= seen_end[(x, y)]:
                    continue
                seen_end[(x, y)] = distance


def load_input(filepath: str = "input.txt") -> list[list[str]]:
    with open(filepath) as f:
        return [list(map(int, list(line))) for line in f.read().splitlines()]


if __name__ == "__main__":
    from datetime import datetime

    start = datetime.now()
    grid = load_input()
    length = find_shortest_path(grid)
    end = datetime.now()
    print(length)
    print((end - start).total_seconds())
