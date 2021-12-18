from __future__ import annotations

from itertools import permutations

from part1 import load_input, magnitude, SFNumber, snail_sum


def find_max_pair_sum(numbers: list[SFNumber]) -> int:
    max_ = 0
    for pair in permutations(numbers, 2):
        max_ = max(max_, magnitude(snail_sum(pair)))
    return max_


if __name__ == "__main__":
    numbers = load_input()
    print(find_max_pair_sum(numbers))
