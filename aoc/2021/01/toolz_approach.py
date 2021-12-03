from typing import Iterable

from toolz import sliding_window


def calc_part1(nums: Iterable[int]) -> int:
    return sum([1 if y > x else 0 for x, y in sliding_window(2, nums)])


def calc_part2(nums: Iterable[int]) -> int:
    return calc_part1([sum(group) for group in sliding_window(3, nums)])


if __name__ == "__main__":
    with open("input.txt") as f:
        input_ = [int(line) for line in f.readlines()]
    print(f"Part 1: {calc_part1(input_)}")
    print(f"Part 2: {calc_part2(input_)}")
