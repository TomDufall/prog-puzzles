from typing import Iterable, List, Tuple


def calculate_endpoint(
    instructions: Iterable[Tuple[str, int]], start: Tuple[int, int] = (0, 0)
) -> Tuple[int, int]:
    x, y = start
    for direction, number in instructions:
        if direction == "forward":
            x += number
        elif direction == "down":
            y -= number
        elif direction == "up":
            y += number
        else:
            raise ValueError(f"Direction not recognised: {direction}")
    return x, y


def load_input(filepath: str = "input.txt") -> List[Tuple[str, int]]:
    def format_line(line: str) -> Tuple[str, int]:
        direction, number = line.split()
        return direction, int(number)

    with open(filepath) as f:
        return list(map(format_line, f.readlines()))


if __name__ == "__main__":
    instructions = load_input()
    endpoint = calculate_endpoint(instructions)
    print(endpoint[0] * -1 * endpoint[1])
