from itertools import combinations
from functools import reduce
import operator
from pathlib import Path
from typing import List, Optional, Tuple


def find_sum_group(
    numbers: List[float], target: float, group_size: int
) -> Optional[Tuple[float]]:
    """
    Find a group of numbers in the input list that sum to the target value.
    :param numbers: List of numbers to find a group in
    :param target: Target to sum to
    :param group_size: The size of the group
    :return: Tuple of numbers that sum to the target value
    """
    for combination in combinations(numbers, group_size):
        if sum(combination) == target:
            return combination
    return None


def fix_expense_report(
    numbers: List[float], target: float, group_size: int
) -> Optional[float]:
    """
    Find a group of numbers that sum to the target value, return their product.
    :param numbers: List of numbers to find a group in
    :param target: Target to sum to
    :param group_size: Size of the group to search for
    :return: Product of the group of numbers
    """
    matched_entries = find_sum_group(numbers, target, group_size)
    if matched_entries:
        return reduce(operator.mul, matched_entries, 1)
    return None


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    numbers = [
        float(line.strip()) for line in input_file.read_text().splitlines()
    ]
    print(fix_expense_report(numbers, 2020, 3))
