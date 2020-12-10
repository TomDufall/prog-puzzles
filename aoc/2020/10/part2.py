from pathlib import Path
from typing import List

from part1 import join_adaptors

def count_valid_arrangements(
    adaptors: List[int], adaptor_range: int = 3
) -> int:
    # sort list and ensure full chain is valid
    chain = join_adaptors(adaptors)
    if len(chain) != len(set(chain)):
        raise ValueError("Adaptors must be unique")
    ways_to_end = {chain.pop(): 1}
    for adaptor in reversed(chain):
        ways_to_end[adaptor] = sum(
            map(
                lambda x: ways_to_end.get(x, 0),
                range(adaptor + 1, adaptor + 1 + adaptor_range)
            )
        )
    return ways_to_end[0]


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    adaptors = list(map(int, filepath.read_text().splitlines()))
    print(count_valid_arrangements(adaptors))
