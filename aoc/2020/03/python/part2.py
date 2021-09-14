from functools import reduce
import operator
from pathlib import Path
from typing import List, Tuple

from part1 import load_input, TobogganMap


def multiply_collisions(
        map_: TobogganMap, vectors: List[Tuple[int, int]]
) -> int:
    collision_counts = map(lambda vector: map_.traverse(vector), vectors)
    return reduce(operator.mul, collision_counts, 1)


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    map_ = TobogganMap(load_input(filepath))
    cases = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    print(multiply_collisions(map_, cases))
