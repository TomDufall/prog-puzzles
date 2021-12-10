from __future__ import annotations

from functools import reduce
from typing import Iterable, Optional

from part1 import load_input


def complete_string(line: str) -> Optional[str]:
    """
    If corrupted or fine, return None
    If missing characters off the end, repair and return
    """
    stack = []
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    openers = {"(", "[", "{", "<"}
    closers = {")", "]", "}", ">"}
    for char in line:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if pairs[stack.pop()] != char:
                return None
        else:
            raise ValueError(f"Character {char} not recognised")
    if stack:
        # Unmatched brackets - we can fix this
        return "".join(map(lambda x: pairs[x], reversed(stack)))
    return None


def score_fixes(fixes: Iterable[Optional[str]]) -> int:
    values = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    f = lambda acc, char: acc * 5 + values[char]
    score = lambda line: reduce(f, line, 0)
    scores = [score(fix) for fix in fixes if fix is not None]

    # return median. guaranteed to be odd-length list
    i = len(scores) // 2
    return sorted(scores)[i]


if __name__ == "__main__":
    lines = load_input()
    fixes = map(complete_string, lines)
    score = score_fixes(fixes)
    print(score)
