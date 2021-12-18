from __future__ import annotations

from itertools import product
import re


def check_intercept_x(x_min, x_max, vel) -> bool:
    x = 0
    if x_min <= x <= x_max:
        return True
    while (vel > 0 and x < x_min) or (vel < 0 and x > x_max):
        x += vel
        if x_min <= x <= x_max:
            return True
        if vel > 0:
            vel -= 1
        elif vel < 0:
            vel += 1
    return False


def find_x_vel_candidates(x_min: int, x_max: int) -> list[int]:
    x_vel_max = x_max
    if x_max / x_min < 0:  # signs don't match
        raise NotImplementedError
    else:
        x_vel_min = 0
    step = 1 if x_min > 0 else -1
    return [
        x
        for x in range(x_vel_min, x_vel_max + step, step)
        if check_intercept_x(x_min, x_max, x)
    ]


def check_intercept_y(y_min, y_max, vel) -> bool:
    y = 0
    if y_min <= y <= y_max:
        return True
    while vel > 0 or y > y_max:
        y += vel
        if y_min <= y <= y_max:
            return True
        vel -= 1
    return False


def find_y_vel_candidates(y_min: int, y_max: int) -> list[int]:
    y_vel_min = y_min
    step = 1
    y_vel_max = 200  # absolute guess
    candidates = [
        y
        for y in range(y_vel_min, y_vel_max + step, step)
        if check_intercept_y(y_min, y_max, y)
    ]
    if candidates[-1] == y_vel_max:
        raise ValueError("Might have stopped searching y early")
    return candidates


def search(target: tuple[tuple[int, int], tuple[int, int]]) -> list[tuple[int, int]]:
    (x_min, x_max), (y_min, y_max) = target
    x_candidates = find_x_vel_candidates(x_min, x_max)
    y_candidates = find_y_vel_candidates(y_min, y_max)
    candidates = [
        (x_vel, y_vel)
        for x_vel, y_vel in product(x_candidates, y_candidates)
        if check_intercept(x_min, x_max, y_min, y_max, x_vel, y_vel)
    ]
    return candidates


def check_intercept(x_min, x_max, y_min, y_max, x_vel, y_vel) -> bool:
    x, y = 0, 0
    while y_vel > 0 or y > y_min:
        # Step position
        x, y = x + x_vel, y + y_vel
        # Check for target
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True
        # Apply drag and gravity
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        y_vel -= 1
    return False


def find_max_y(y_vel) -> int:
    y = 0
    while y_vel > 0:
        y += y_vel
        y_vel -= 1
    return y


def load_input(filepath: str = "input.txt") -> tuple[tuple[int, int], tuple[int, int]]:
    with open(filepath) as f:
        line = f.read()
    pattern = r"^target area: x=(?P<x_min>\-?[\d]*)\.\.(?P<x_max>\-?[\d]*), y=(?P<y_min>\-?[\d]*)\.\.(?P<y_max>\-?[\d]*)$"
    match = re.match(pattern, line)
    if not match:
        raise ValueError("Input not parsed")
    x_range = int(match.groupdict()["x_min"]), int(match.groupdict()["x_max"])
    y_range = int(match.groupdict()["y_min"]), int(match.groupdict()["y_max"])
    return x_range, y_range


if __name__ == "__main__":
    target = load_input()
    candidates = search(target)
    funnest = max(candidates, key=lambda item: item[1])
    print(funnest)
    print(find_max_y(funnest[1]))
    print(len(candidates))
