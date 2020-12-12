from dataclasses import dataclass, InitVar
from typing import List, Tuple, Optional as Opt
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
    waypoint: Opt[Vector2D] = None
    waypoint_x: InitVar[Opt[int]] = 0
    waypoint_y: InitVar[Opt[int]] = 0

    def __post_init__(self, pos_x: Opt[int], pos_y: Opt[int], waypoint_x: Opt[int], waypoint_y: Opt[int]):
        if not self.pos:
            self.pos = Vector2D(pos_x, pos_y)
        if not self.waypoint:
            self.waypoint = Vector2D(waypoint_x, waypoint_y)

    def step(self, op: str, value: int) -> None:
        if op in DIRECTIONS:
            self.waypoint += value * DIRECTIONS[op]
        elif op == "R":
            angle = radians(-1 * value)
            self.waypoint = Vector2D(
                round(self.waypoint.x * cos(angle) - self.waypoint.y * sin(angle), 6),
                round(self.waypoint.x * sin(angle) + self.waypoint.y * cos(angle), 6)
            )
        elif op == "L":
            angle = radians(value)
            self.waypoint = Vector2D(
                round(self.waypoint.x * cos(angle) - self.waypoint.y * sin(angle), 6),
                round(self.waypoint.x * sin(angle) + self.waypoint.y * cos(angle), 6)
            )
        elif op == "F":
            self.pos += value * self.waypoint
        else:
            raise ValueError(f"Unrecognised operation: {op}")

    def run(self, instructions: List[Tuple[str, int]]) -> None:
        for op, value in instructions:
            self.step(op, value)


def load_input(filepath: Path) -> List[Tuple[str, int]]:
    return [(item[0], int(item[1:])) for item in filepath.read_text().splitlines()]


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    ship = Ship(waypoint_x=10, waypoint_y=1)
    instr = load_input(filepath)
    ship.run(instr)
    print(abs(ship.pos.x) + abs(ship.pos.y))
