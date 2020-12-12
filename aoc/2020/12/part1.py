from dataclasses import dataclass
from typing import List, Tuple
from math import sin, cos, radians
from pathlib import Path

DIRECTIONS = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0),
}


@dataclass
class Ship:
    pos_x: int = 0
    pos_y: int = 0
    direction: int = 0

    def step(self, op: str, value: int) -> None:
        if op in DIRECTIONS:
            vx, vy = DIRECTIONS[op]
            self.pos_x = self.pos_x + vx * value
            self.pos_y = self.pos_y + vy * value
        elif op == "R":
            self.direction = (self.direction + value) % 360
        elif op == "L":
            self.direction = (self.direction - value) % 360
        elif op == "F":
            self.pos_x = round(self.pos_x + sin(radians(self.direction)) * value, 6)
            self.pos_y = round(self.pos_y + cos(radians(self.direction)) * value, 6)
        else:
            raise ValueError(f"Unrecognised operation: {op}")

    def run(self, instructions: List[Tuple[str, int]]) -> None:
        for op, value in instructions:
            self.step(op, value)
            print(ship.pos_x, ship.pos_y, ship.direction)


def load_input(filepath: Path) -> List[Tuple[str, int]]:
    return [(item[0], int(item[1:])) for item in filepath.read_text().splitlines()]


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    ship = Ship(direction=90)
    instr = load_input(filepath)
    ship.run(instr)
    print(abs(ship.pos_x) + abs(ship.pos_y))
