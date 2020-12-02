from itertools import combinations
from typing import List, Optional, Tuple

def find_sum_pair(
    numbers: List[float], target: float
) -> Optional[Tuple[float, float]]:
    for combination in combinations(numbers, 2):
        a, b = combination
        if a + b == target:
            return a, b
    return None

def fix_expense_report(numbers: List[float], target: float) -> float:
    sum_pair = find_sum_pair(numbers, target)
    if sum_pair is None:
        return None
    return sum_pair[0] * sum_pair[1]

if __name__ == "__main__":
    with open('input.txt') as f:
        numbers = [float(line.strip()) for line in f.readlines()]
    print(fix_expense_report(numbers, 2020))