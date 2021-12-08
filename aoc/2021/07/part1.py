from __future__ import annotations


def find_min_moves(crabs: list[int]):
    grouping_cost: dict[int, int] = {}
    for position in range(min(crabs), max(crabs) + 1):
        grouping_cost[position] = sum((abs(position - crab_pos) for crab_pos in crabs))
    return grouping_cost


def load_input(filepath: str = "input.txt") -> list[int]:
    with open(filepath) as f:
        return [int(n) for n in f.read().split(",")]


if __name__ == "__main__":
    input_ = load_input()
    min_moves = find_min_moves(input_)
    answer = min(min_moves.items(), key=lambda item: item[1])
    print(answer)
