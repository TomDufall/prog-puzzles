from itertools import combinations
from typing import List, Tuple

from part1 import load_input


def is_close_match(str_1: str, str_2: str) -> bool:
    """
    Return True if strings are at most one character different
    """
    errors = 0
    for i, (a, b) in enumerate(zip(str_1, str_2)):
        if a != b:
            errors += 1
        if errors > 1:
            return False
    return True


def find_similar_boxes(ids: List[str]) -> Tuple[str, str]:
    for a, b in combinations(ids, 2):
        if is_close_match(a, b):
            return a, b
    raise Exception("Similar boxes not found")


def find_common_string(a: str, b: str) -> str:
    """
    Return the characters in two strings where they match up.
    """
    return "".join((char1 for char1, char2 in zip(a, b) if char1 == char2))


if __name__ == "__main__":
    input_ = load_input()
    a, b = find_similar_boxes(input_)
    print(a, b)
    print(find_common_string(a, b))
