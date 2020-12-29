from pathlib import Path
from typing import Dict, Tuple, Set


Coord = Tuple[int, int]

DIRECTIONS: Dict[str, Coord] = {
    "e": (1, 0),
    "se": (0, -1),
    "sw": (-1, -1),
    "w": (-1, 0),
    "nw": (0, 1),
    "ne": (1, 1),
}


def calc_coord_from_str(input_: str) -> Coord:
    """
    Convert a coordinate string into an x/y coord.
    Coords are x along W/E(+) direction, y along SE/NW(+).
    """
    coords = (0, 0)
    chars = iter(input_)
    while True:
        try:
            next_ = next(chars)
            if next_ in {"n", "s"}:
                next_ += next(chars)
        except StopIteration:
            return coords
        diff = DIRECTIONS[next_]
        coords = (coords[0] + diff[0], coords[1] + diff[1])


def load_black_tiles(filepath: Path) -> Set[Coord]:
    flips = map(calc_coord_from_str, filepath.read_text().splitlines())
    black_tiles: Set[Tuple[int, int]] = set()
    for coord in flips:
        if coord in black_tiles:
            black_tiles.remove(coord)
        else:
            black_tiles.add(coord)
    return set(black_tiles)


if __name__ == "__main__":
    SAMPLE_INPUT = Path(__file__).parent / "sample_input.txt"
    INPUT = Path(__file__).parent / "input.txt"
    from datetime import datetime
    start = datetime.now()
    answer = len(load_black_tiles(INPUT))
    end = datetime.now()
    time = (end - start).total_seconds()
    print(time)
    print(answer)
