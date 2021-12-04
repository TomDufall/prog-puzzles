from collections import defaultdict
from typing import Dict, Iterable, List


def frequencies(string: str) -> Dict[str, int]:
    freqs: Dict[str, int] = defaultdict(lambda: 0)
    for char in string:
        freqs[char] += 1
    return freqs


def checksum(ids: Iterable[str]) -> int:
    pairs = 0
    triples = 0
    for id_ in ids:
        freqs = frequencies(id_)
        if 2 in freqs.values():
            pairs += 1
        if 3 in freqs.values():
            triples += 1
    return pairs * triples


def load_input(filepath: str = "input.txt") -> List[str]:
    with open(filepath) as f:
        return f.read().splitlines()


if __name__ == "__main__":
    input_ = load_input()
    print(checksum(input_))
