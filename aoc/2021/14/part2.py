from __future__ import annotations
from typing import DefaultDict

from part1 import load_input


def step_pairs(
    pairs: dict[tuple[str, str], int], recipes: dict[tuple[str, str], str]
) -> dict[tuple[str, str], int]:
    new_pairs: DefaultDict[tuple[str, str], int] = DefaultDict(lambda: 0)
    for pair, count in pairs.items():
        if pair in recipes:
            middle = recipes[pair]
            first, second = pair
            new_pairs[(first, middle)] += count
            new_pairs[(middle, second)] += count
        else:
            new_pairs[pair] += count
    return new_pairs


def to_pairs(s: str) -> list[tuple[str, str]]:
    pairs: dict[tuple[str, str], int] = DefaultDict(lambda: 0)
    last = s[0]
    for next_ in s[1:]:
        pairs[(last, next_)] += 1
        last = next_
    return pairs


def get_freqs_after_steps(
    template: list[str], recipes: dict[tuple[str, str], str], steps: int
) -> dict[str, int]:
    pairs: dict[tuple[str, str], int] = to_pairs(template)
    first = template[0]
    for _ in range(steps):
        pairs = step_pairs(pairs, recipes)

    freqs: dict[str, int] = DefaultDict(lambda: 0)
    # To avoid counting twice, only count right item
    # Count first item on its own as this will only be on the left
    freqs[first] += 1
    for (_, b), count in pairs.items():
        freqs[b] += count
    return freqs


if __name__ == "__main__":
    from datetime import datetime

    start = datetime.now()
    template, recipes = load_input()
    freqs = get_freqs_after_steps(template, recipes, 40)
    print(max(freqs.values()) - min(freqs.values()))
    end = datetime.now()
    print((end - start).total_seconds())
