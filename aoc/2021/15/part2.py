from __future__ import annotations

from part1 import find_shortest_path, load_input


def generate_grid(tile: list[list[int]]):
    """
    Grid is generated by repeating a tile 5 times in each direction.
    Risk of each space in the tile increase by 1 for each move down/across, but
    wraps to 0 after 9.
    """

    def simplify_risk(x):
        while x > 9:
            x -= 9
        return x

    grid = []
    for y in range(len(tile) * 5):
        y_tile = y // len(tile)
        source_y = y % len(tile)
        row = []
        for x_tile in range(5):
            x_segment = [simplify_risk(x + x_tile + y_tile) for x in tile[source_y]]
            row.extend(x_segment)
        grid.append(row)
    return grid


if __name__ == "__main__":
    from datetime import datetime

    start = datetime.now()
    tile = load_input()
    grid = generate_grid(tile)
    length = find_shortest_path(grid, 1000000)

    end = datetime.now()
    print(length)
    print((end - start).total_seconds())
