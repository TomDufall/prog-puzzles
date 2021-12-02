from typing import Iterable, Tuple
from part1 import load_input


def calculate_endpoint(
    instructions: Iterable[Tuple[str, int]], start: Tuple[int, int, int] = (0, 0, 0)
) -> Tuple[int, int, int]:
    x, y, aim = start
    for direction, number in instructions:
        if direction == "forward":
            x += number
            y += number * aim
        elif direction == "down":
            aim -= number
        elif direction == "up":
            aim += number
        else:
            raise ValueError(f"Direction not recognised: {direction}")
    return x, y, aim


if __name__ == "__main__":
    instructions = load_input()
    x, y, aim = calculate_endpoint(instructions)
    print(x * -1 * y)
