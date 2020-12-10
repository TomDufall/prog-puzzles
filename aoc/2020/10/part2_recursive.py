from functools import lru_cache
from pathlib import Path
from typing import FrozenSet


@lru_cache(maxsize=None)
def count_paths(current: int, adaptors: FrozenSet[int], end: int, reach: int = 3):
    if current == end:
        return 1
    elif current > end:
        raise ValueError("Overshot the end!")
    elif current not in adaptors:
        return 0
    else:
        return sum(
            map(
                lambda x: count_paths(x, adaptors, end, reach),
                range(current + 1, current + 1 + reach)
            )
        )


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    adaptors = set(map(int, filepath.read_text().splitlines()))
    adaptors.add(0)
    adaptors.add(max(adaptors) + 3)
    adaptors = frozenset(adaptors)
    print(count_paths(0, adaptors, max(adaptors)))
