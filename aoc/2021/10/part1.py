from __future__ import annotations

from typing import Iterable, Optional


def validate_line(line: str) -> Optional[tuple[int, str]]:
    """
    If no errors, return none.
    If error, return (character, symbol)
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
    for i, char in enumerate(line):
        if char in openers:
            stack.append(char)
        elif char in closers:
            if pairs[stack.pop()] != char:
                return (i, char)
        else:
            raise ValueError(f"Character {char} not recognised")
    if stack:
        # Unmatched brackets
        return len(line), ""
    return None


def sum_errors(errors: Iterable[Optional[tuple[int, str]]]) -> int:
    values = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
        "": 0,  # Ignore incomplete lines for part 1
    }
    total = 0
    for _, char in filter(lambda x: x is not None, errors):
        total += values[char]
    return total


def load_input(filepath: str = "input.txt") -> list[str]:
    with open(filepath) as f:
        return f.read().splitlines()


if __name__ == "__main__":
    lines = load_input()
    errors = map(validate_line, lines)
    answer = sum_errors(errors)
    print(answer)
