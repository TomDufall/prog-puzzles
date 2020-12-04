from itertools import combinations
from pathlib import Path
from typing import List, Optional, Tuple


def find_sum_pair(
    numbers: List[float], target: float
) -> Optional[Tuple[float, float]]:
    """
    Find a pair of numbers in the input list that sum to the target value.
    :param numbers: List of numbers to find a pair in
    :param target: Target to sum to
    :return: Pair of numbers that sum to the target value
    """
    for combination in combinations(numbers, 2):
        a, b = combination
        if a + b == target:
            return a, b
    return None


def fix_expense_report(numbers: List[float], target: float) -> Optional[float]:
    """
    Find a pair of numbers that sum to the target value, return their product.
    :param numbers: List of numbers to find a pair in
    :param target: Target to sum to
    :return: Product of the pair of numbers
    """
    sum_pair = find_sum_pair(numbers, target)
    if sum_pair is None:
        return None
    return sum_pair[0] * sum_pair[1]


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    numbers = list(map(float, input_file.read_text().splitlines()))
    print(fix_expense_report(numbers, 2020))
