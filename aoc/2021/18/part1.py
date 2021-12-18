from __future__ import annotations

from copy import deepcopy
import json
from typing import Any

SFNumber = Any  # Defining recursive types sucks iirc


def _can_explode(n: SFNumber, max_depth: int = 4) -> list[int]:
    for i, item in enumerate(n):
        if isinstance(item, list):
            if max_depth == 1:
                return [i]
            sub_explosion = _can_explode(item, max_depth - 1)
            if sub_explosion:
                return [i] + sub_explosion
    return None


get_in = (
    lambda struct, indexes: struct
    if indexes == []
    else get_in(struct[indexes[0]], indexes[1:])
)


def _explode(n: SFNumber, location: list[int]) -> SFNumber:
    """
    The left element of the target pair is added to the next number to the
    left. The right element is added to the next number to the right. If no
    next number exists, skip. The pair is then replaced with 0.
    """
    n = deepcopy(n)
    left, right = get_in(n, location)
    # Find left neighbour
    right_split_indexes = [i for i, n in enumerate(location) if n == 1]
    if right_split_indexes:
        last_right_split_index = right_split_indexes[-1]
        path = location[:last_right_split_index] + [0]
        while not isinstance(get_in(n, path), int):
            path += [1]
        last_list = get_in(n, path[:-1])
        last_list[path[-1]] += left
    # Find right neighbour
    left_split_indexes = [i for i, n in enumerate(location) if n == 0]
    if left_split_indexes:
        last_left_split_index = left_split_indexes[-1]
        path = location[:last_left_split_index] + [1]
        while not isinstance(get_in(n, path), int):
            path += [0]
        last_list = get_in(n, path[:-1])
        last_list[path[-1]] += right
    # Remove pair
    path = get_in(n, location[:-1])
    path[location[-1]] = 0
    return n


def _can_split(n: SFNumber) -> list[int]:
    # Iterative rather than recursive to contrast with _can_explode
    # to_visit = [(path, node)], e.g. [([0, 0, 1], [3, 4])]
    to_visit = [([], n)]
    while to_visit:
        path, node = to_visit.pop()
        if isinstance(node, list):
            new_ = [(path + [i], item) for i, item in reversed(list(enumerate(node)))]
            to_visit.extend(new_)
        elif node >= 10:
            return path


def _split(n: SFNumber, location: list[int]) -> SFNumber:
    n = deepcopy(n)
    current = get_in(n, location)
    left = current // 2
    right = current // 2 + current % 2
    insertion_point = get_in(n, location[:-1])
    insertion_point[location[-1]] = [left, right]
    return n


def reduce(n: SFNumber, max_steps=-1) -> SFNumber:
    step = 0
    while max_steps == -1 or step < max_steps:
        step += 1
        if explosion_point := _can_explode(n):
            n = _explode(n, explosion_point)
        elif split_point := _can_split(n):
            n = _split(n, split_point)
        else:
            return n


def snail_sum(numbers: list[SFNumber]) -> SFNumber:
    acc = numbers[0]
    for n in numbers[1:]:
        acc = reduce([acc, n])
    return acc


def magnitude(n: SFNumber) -> int:
    if isinstance(n, int):
        return n
    return 3 * magnitude(n[0]) + 2 * magnitude(n[1])


def load_input(filepath: str = "input.txt") -> list[SFNumber]:
    with open(filepath) as f:
        text = f.read()
    return [json.loads(line) for line in text.splitlines()]


if __name__ == "__main__":
    numbers = load_input()
    total = snail_sum(numbers)
    answer = magnitude(total)
    print(answer)
