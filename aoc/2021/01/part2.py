from collections import deque
from typing import Iterable, List

from part1 import count_increases, load_input


def rolling_window_sum(numbers: Iterable, length: int) -> List[int]:
    values = iter(numbers)
    seed = [next(values) for i in range(length)]
    window = deque(seed, maxlen=length)
    sums = [sum(window)]
    for value in values:
        window.append(value)
        sums.append(sum(window))
    return sums


if __name__ == "__main__":
    input_ = load_input()
    sums = rolling_window_sum(input_, 3)
    increases = count_increases(sums)
    print(increases)