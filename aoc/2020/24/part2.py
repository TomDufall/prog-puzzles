from pathlib import Path
from typing import Set

from part1 import Coord, DIRECTIONS, load_black_tiles


def find_neighbours(coord: Coord) -> Set[Coord]:
    return {(coord[0] + diff[0], coord[1] + diff[1]) for diff in DIRECTIONS.values()}


def step(black_coords: Set[Coord], n: int = 1) -> Set[Coord]:
    for _ in range(n):
        new_coords = set()
        all_neighbours = set().union(*[find_neighbours(coord) for coord in black_coords])
        for coord in all_neighbours:
            black_neighbours = len(find_neighbours(coord).intersection(black_coords))
            if coord in black_coords:
                if black_neighbours == 1 or black_neighbours == 2:
                    new_coords.add(coord)
            else:
                if black_neighbours == 2:
                    new_coords.add(coord)
        black_coords = new_coords
    return black_coords


if __name__ == "__main__":
    INPUT = Path(__file__).parent / "input.txt"
    from datetime import datetime
    start = datetime.now()
    initial = load_black_tiles(INPUT)
    answer = (len(step(initial, n=100)))
    end = datetime.now()
    time = (end - start).total_seconds()
    print(time)
    print(answer)
