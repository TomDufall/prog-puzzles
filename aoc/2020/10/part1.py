from pathlib import Path
from typing import Dict, List, Tuple

from toolz.itertoolz import frequencies, sliding_window


def count_diffs(adaptor_chain: List[int]) -> Dict[int, int]:
    def calc_diff(ab: Tuple[int]) -> int:
        a, b = ab
        return b - a
    diffs = map(calc_diff, sliding_window(2, adaptor_chain))
    return frequencies(diffs)


def validate_adaptor_chain(adaptor_chain: List[int]) -> bool:
    def valid_step(ab: Tuple[int]) -> bool:
        a, b = ab
        if b < a or b > a + 3:
            return False
        return True
    return all(map(valid_step, sliding_window(2, adaptor_chain)))


def join_adaptors(adaptors: List[int]) -> List[int]:
    adaptor_chain = [0]
    adaptor_chain.extend(sorted(adaptors))
    adaptor_chain.append(adaptor_chain[-1] + 3)
    if not validate_adaptor_chain(adaptor_chain):
        raise ValueError("Adaptor chain invalid")
    return adaptor_chain


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    adaptors = list(map(int, filepath.read_text().splitlines()))
    diffs = (count_diffs(join_adaptors(adaptors)))
    print(diffs)
    print(diffs[1] * diffs[3])
