from itertools import combinations
from functools import reduce
import operator
from typing import List, Optional, Tuple

def find_sum_group(
    numbers: List[float], target: float, group_size: int
) -> Optional[Tuple[float]]:
    for combination in combinations(numbers, group_size):
        if sum(combination) == target:
            return combination
    return None

def fix_expense_report(
    numbers: List[float], target: float, group_size: int
) -> Optional[float]:
    matched_entries = find_sum_group(numbers, target, group_size)
    if matched_entries:
        return reduce(operator.mul, matched_entries, 1)
    return None

if __name__ == "__main__":
    with open('input.txt') as f:
        numbers = [float(line.strip()) for line in f.readlines()]
    print(fix_expense_report(numbers, 2020, 3))