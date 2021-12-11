from __future__ import annotations

from copy import deepcopy
from itertools import product


def step(grid: list[list[int]]) -> tuple[list[list[int]], int]:
    """
    Step forward the simulation.
    Return grid, flashes during step.
    """
    grid = deepcopy(grid)
    to_flash = set()
    # Increment step
    for y, x in product(range(len(grid)), range(len(grid[0]))):
        grid[y][x] += 1
        if grid[y][x] == 10:
            to_flash.add((y, x))

    # Process flashes
    adjacent = {(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)}
    flashes = 0
    while to_flash:
        y, x = to_flash.pop()
        flashes += 1
        for ydiff, xdiff in adjacent:
            y2, x2 = y + ydiff, x + xdiff
            if y2 < 0 or x2 < 0 or y2 >= len(grid) or x2 >= len(grid[0]):
                continue
            grid[y2][x2] += 1
            if grid[y2][x2] == 10:
                to_flash.add((y2, x2))

    # Normalise grid - >= 10 goes to 0
    for y, x in product(range(len(grid)), range(len(grid[0]))):
        if grid[y][x] >= 10:
            grid[y][x] = 0
    return grid, flashes


def steps(grid: list[list[int]], steps: int) -> tuple[list[list[int]], int]:
    flashes = 0
    for _ in range(steps):
        grid, new_flashes = step(grid)
        flashes += new_flashes
    return grid, flashes


def load_input(filepath: str = "input.txt") -> list[list[int]]:
    with open(filepath) as f:
        return [[int(n) for n in line] for line in f.read().splitlines()]


if __name__ == "__main__":
    grid = load_input()
    _, flashes = steps(grid, 100)
    print(flashes)
