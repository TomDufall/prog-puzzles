from typing import Iterable, List


def count_increases(input_: Iterable[int]) -> int:
    increases = 0
    values = iter(input_)
    prev_value = next(values)
    for value in values:
        if value > prev_value:
            increases += 1
        prev_value = value
    return increases


def load_input(filepath: str = "input.txt") -> List[int]:
    with open(filepath) as f:
        return [int(line) for line in f.readlines()]


if __name__ == "__main__":
    input_ = load_input()
    increases = count_increases(input_)
    print(increases)
