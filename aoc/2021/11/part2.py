from __future__ import annotations

from part1 import load_input, step


def find_sync_step(grid: list[list[int]], max_steps: int = 1000) -> int:
    for i in range(max_steps):
        grid, flashes = step(grid)
        if flashes == len(grid) * len(grid[0]):
            return i + 1
    raise ValueError(f"Sync point not found within {max_steps} steps")


if __name__ == "__main__":
    grid = load_input()
    sync_point = find_sync_step(grid, 1000)
    print(sync_point)
