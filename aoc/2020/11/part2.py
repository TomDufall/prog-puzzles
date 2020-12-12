from dataclasses import dataclass
from itertools import product
from pathlib import Path

from part1 import (
    load_input,
    SeatingSimulation as SeatingSimulationPart1,
    StringArray2D,
)


@dataclass
class SeatingSimulation(SeatingSimulationPart1):
    crowding_limit: int = 4

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
            x2 = x
            y2 = y
            while True:
                x2 = x2 + dx
                y2 = y2 + dy
                if x2 < 0 or y2 < 0 or x2 > max_x or y2 > max_y:
                    break
                elif layout[y2][x2] == character:
                    count += 1
                    break
                elif layout[y2][x2] == "L":
                    break
        return count


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    layout = load_input(filepath)
    sim = SeatingSimulation(layout)
    print(sim.run())
