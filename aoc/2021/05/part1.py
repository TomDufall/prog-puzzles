from __future__ import annotations  # backwards-compatibility for type hinting generics

from collections import defaultdict
from dataclasses import dataclass
from itertools import product
from typing import NamedTuple

Point2D = NamedTuple("Point2D", [("x", int), ("y", int)])


@dataclass(frozen=True)
class Line2D:
    start: Point2D
    end: Point2D

    @property
    def is_diagonal(self) -> bool:
        return self.start.x != self.end.x and self.start.y != self.end.y


def map_vent_density(lines: list[Line2D]) -> dict[Point2D, int]:
    vent_count: dict[Point2D, int] = defaultdict(lambda: 0)
    for line in filter(lambda l: not l.is_diagonal, lines):
        x_min, x_max = sorted((line.start.x, line.end.x))
        y_min, y_max = sorted((line.start.y, line.end.y))
        x_values = range(x_min, x_max + 1)
        y_values = range(y_min, y_max + 1)
        for x, y in product(x_values, y_values):
            vent_count[Point2D(x, y)] += 1
    return vent_count


def count_dangerous_areas(vent_map: dict[Point2D, int], threshold: int = 2) -> int:
    return sum(1 for _ in (filter((lambda x: x >= threshold), vent_map.values())))


def load_input(filepath: str = "input.txt") -> list[Line2D]:
    def parse_line(line: str) -> Line2D:
        point_str1, _, point_str2 = line.split()
        point1 = Point2D(*map(int, point_str1.split(",")))
        point2 = Point2D(*map(int, point_str2.split(",")))
        return Line2D(point1, point2)

    with open(filepath) as f:
        return [parse_line(line) for line in f.readlines()]


if __name__ == "__main__":
    lines = load_input()
    vents = map_vent_density(lines)
    danger_count = count_dangerous_areas(vents)
    print(danger_count)
