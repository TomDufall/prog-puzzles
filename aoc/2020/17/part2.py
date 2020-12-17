from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Iterable, List, Set, Tuple

from toolz import concat, count

Point = Tuple[int, int, int, int]

@dataclass
class Cube:
    data: Set[Point]

    @staticmethod
    def from_filepath(filepath: Path) -> List[List[bool]]:
        return Cube(list(concat([
            [(x, y, 0, 0) for x, char in enumerate(line) if char == "#"]
            for y, line in enumerate(filepath.read_text().splitlines())
        ])))

    @staticmethod
    def neighbours(points: Iterable[Point]) -> List[Point]:
        return set(concat([list(product({x - 1, x, x + 1}, {y - 1, y, y + 1}, {z - 1, z, z + 1}, {w - 1, w, w + 1})) for x, y, z, w in points]))

    def count_active_neighbours(self, point: Point) -> int:
        # Includes self, if active
        return count((neighbour for neighbour in self.neighbours([point]) if neighbour in self.data))

    def step(self) -> None:
        new_data = set()
        for point in self.neighbours(self.data):
            neighbour_count = self.count_active_neighbours(point)
            if point in self.data and (neighbour_count == 3 or neighbour_count == 4):
                new_data.add(point)
            elif point not in self.data and neighbour_count == 3:
                new_data.add(point)
        self.data = new_data
        return

    def step_n(self, n: int) -> None:
        for _ in range(n):
            self.step()


if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    filepath = Path(__file__).parent /"input.txt"
    cube = Cube.from_filepath(filepath)
    cube.step_n(6)
    end = datetime.now()
    time = (end - start).total_seconds()
    print(len(cube.data))
    print(time)
