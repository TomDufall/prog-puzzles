from collections import deque
from itertools import combinations
from pathlib import Path
from typing import Iterable, Iterator

from part1 import find_error


def find_sum_stream(datastream: Iterator[int], target: int) -> int:
    """
    Find a contiguous group of values in the datastream (min 2) that sum to
    the target value.
    Return the sum of the min and max in this group.
    """
    window = deque()
    while True:
        if sum(window) == target and len(window) > 1:
            return min(window) + max(window)
        elif sum(window) > target:
            window.popleft()
        else:
            try:
                window.append(next(datastream))
            except StopIteration:
                return None

if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    data = list(map(int, filepath.read_text().splitlines()))
    error = find_error(iter(data), 25)
    print(find_sum_stream(iter(data), error))
