from typing import List

from part1 import load_input


def find_common_frequency(deltas: List[str], start: int = 0) -> int:
    freq = start
    seen_freqs = {freq}
    while True:
        for delta in deltas:
            freq += int(delta)
            if freq in seen_freqs:
                return freq
            seen_freqs.add(freq)
            # no unbounded growth check


if __name__ == "__main__":
    input_ = load_input()
    freq = find_common_frequency(input_)
    print(freq)