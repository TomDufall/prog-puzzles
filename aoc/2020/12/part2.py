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
    waypoint_x: int = 0
    waypoint_y: int = 0

    def step(self, op: str, value: int) -> None:
        if op in DIRECTIONS:
            vx, vy = DIRECTIONS[op]
            self.waypoint_x = self.waypoint_x + vx * value
            self.waypoint_y = self.waypoint_y + vy * value
        elif op == "R":
            angle = radians(-1 * value)
            new_x = round(self.waypoint_x * cos(angle) - self.waypoint_y * sin(angle), 6)
            new_y = round(self.waypoint_x * sin(angle) + self.waypoint_y * cos(angle), 6)
            self.waypoint_x = new_x
            self.waypoint_y = new_y
        elif op == "L":
            angle = radians(value)
            new_x = round(self.waypoint_x * cos(angle) - self.waypoint_y * sin(angle), 6)
            new_y = round(self.waypoint_x * sin(angle) + self.waypoint_y * cos(angle), 6)
            self.waypoint_x = new_x
            self.waypoint_y = new_y
        elif op == "F":
            self.pos_x = self.pos_x + value * self.waypoint_x
            self.pos_y = self.pos_y + value * self.waypoint_y
        else:
            raise ValueError(f"Unrecognised operation: {op}")

    def run(self, instructions: List[Tuple[str, int]]) -> None:
        for op, value in instructions:
            self.step(op, value)


def load_input(filepath: Path) -> List[Tuple[str, int]]:
    return [(item[0], int(item[1:])) for item in filepath.read_text().splitlines()]


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    ship = Ship(direction=90, waypoint_x=10, waypoint_y=1)
    instr = load_input(filepath)
    ship.run(instr)
    print(abs(ship.pos_x) + abs(ship.pos_y))
