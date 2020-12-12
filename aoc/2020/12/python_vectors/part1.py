from dataclasses import dataclass, InitVar
from typing import Optional as Opt, List, Tuple
from math import sin, cos, radians
from pathlib import Path

from vectors import Vector2D


DIRECTIONS = {
    "N": Vector2D(0, 1),
    "S": Vector2D(0, -1),
    "E": Vector2D(1, 0),
    "W": Vector2D(-1, 0),
}


@dataclass
class Ship:
    pos: Opt[Vector2D] = None
    pos_x: InitVar[Opt[int]] = 0
    pos_y: InitVar[Opt[int]] = 0
    direction: int = 0

    def __post_init__(self, pos_x: Opt[int], pos_y: Opt[int]):
        if not self.pos:
            self.pos = Vector2D(pos_x, pos_y)

    def step(self, op: str, value: int) -> None:
        if op in DIRECTIONS:
            self.pos += value * DIRECTIONS[op]
        elif op == "R":
            self.direction = (self.direction + value) % 360
        elif op == "L":
            self.direction = (self.direction - value) % 360
        elif op == "F":
            self.pos = Vector2D(
                round(self.pos.x + sin(radians(self.direction)) * value, 6),
                round(self.pos.y + cos(radians(self.direction)) * value, 6)
            )
        else:
            raise ValueError(f"Unrecognised operation: {op}")

    def run(self, instructions: List[Tuple[str, int]]) -> None:
        for op, value in instructions:
            self.step(op, value)
            print(self)


def load_input(filepath: Path) -> List[Tuple[str, int]]:
    return [(item[0], int(item[1:])) for item in filepath.read_text().splitlines()]


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    ship = Ship(direction=90)
    instr = load_input(filepath)
    ship.run(instr)
    print(abs(ship.pos.x) + abs(ship.pos.y))
