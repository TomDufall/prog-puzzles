from collections import defaultdict
from itertools import product

from part1 import count_dangerous_areas, load_input, Line2D, Point2D


def map_vent_density_full(lines: list[Line2D]) -> dict[Point2D, int]:
    vent_count: dict[Point2D, int] = defaultdict(lambda: 0)
    for line in lines:
        x_step = 1 if line.start.x <= line.end.x else -1
        y_step = 1 if line.start.y <= line.end.y else -1
        x_values = range(line.start.x, line.end.x + x_step, x_step)
        y_values = range(line.start.y, line.end.y + y_step, y_step)
        if line.is_diagonal:
            for x, y in zip(x_values, y_values):
                vent_count[Point2D(x, y)] += 1
        else:
            for x, y in product(x_values, y_values):
                vent_count[Point2D(x, y)] += 1
    return vent_count


if __name__ == "__main__":
    lines = load_input()
    vents = map_vent_density_full(lines)
    danger_count = count_dangerous_areas(vents)
    print(danger_count)
