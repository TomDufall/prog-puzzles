from collections import deque
from itertools import combinations
from pathlib import Path
from typing import Iterable, Iterator


def different_sum_pair_exists(nums: Iterable[int], target: int) -> bool:
    return target in (x + y for x, y in combinations(nums, 2) if x != y)


def find_error(datastream: Iterator[int], preamble_size: int) -> int:
    buffer = deque(
        [next(datastream) for i in range(preamble_size)], preamble_size
    )
    while True:
        try:
            value = next(datastream)
            if not different_sum_pair_exists(buffer, value):
                return value
            buffer.append(value)
        except StopIteration:
            return None


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    datastream = map(int, filepath.read_text().splitlines())
    print(find_error(datastream, 25))
