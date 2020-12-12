from copy import deepcopy
from dataclasses import dataclass, field
from itertools import product
from pathlib import Path
from typing import List

StringArray2D = List[List[str]]


@dataclass
class SeatingSimulation:
    layout: StringArray2D
    current: StringArray2D = field(init=False)
    crowding_limit: int = 3

    def __post_init__(self):
        self.current = self.layout

    @staticmethod
    def count_surrounding_character(
            layout: StringArray2D,
            x: int,
            y: int,
            character: str,
    ) -> int:
        to_check = product([-1, 0, 1], [-1, 0, 1])
        count = 0
        max_x = len(layout[0]) - 1
        max_y = len(layout) - 1
        for dx, dy in to_check:
            if dx == 0 and dy == 0:
                continue
            x2 = x + dx
            y2 = y + dy
            if x2 < 0 or y2 < 0 or x2 > max_x or y2 > max_y:
                continue
            elif layout[y2][x2] == character:
                count += 1
        return count

    def step(self) -> None:
        current = self.current
        next_ = deepcopy(current)
        for x, y in product(range(len(current[0])), range(len(current))):
            if current[y][x] == ".":
                continue
            count = self.count_surrounding_character(current, x, y, "#")
            if current[y][x] == "L" and count == 0:
                next_[y][x] = "#"
            elif current[y][x] == "#" and count > self.crowding_limit:
                next_[y][x] = "L"
        self.current = next_

    def run(self, limit=1000) -> int:
        step = 0
        while step < limit:
            prev = self.current
            self.step()
            if self.current == prev:
                return sum("".join(row).count("#") for row in self.current)
            step += 1


def load_input(filepath: Path) -> StringArray2D:
    strings = filepath.read_text().splitlines()
    return [list(string) for string in strings]


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    layout = load_input(filepath)
    sim = SeatingSimulation(layout)
    print(sim.run())
