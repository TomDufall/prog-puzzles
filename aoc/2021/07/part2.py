from __future__ import annotations

from part1 import load_input


def find_min_moves(crabs: list[int]):
    grouping_cost: dict[int, int] = {}
    for position in range(min(crabs), max(crabs) + 1):
        cost = 0
        for crab_pos in crabs:
            diff = abs(position - crab_pos)
            # Cost increases for each step - triangle numbers
            cost += diff * (diff + 1) // 2
        grouping_cost[position] = cost
    return grouping_cost


if __name__ == "__main__":
    input_ = load_input()
    min_moves = find_min_moves(input_)
    answer = min(min_moves.items(), key=lambda item: item[1])
    print(answer)
