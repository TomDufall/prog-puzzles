import pytest

from part1 import find_sum_pair, fix_expense_report

@pytest.mark.parametrize(
    ("numbers", "target", "expected"),
    [
        (
            [1721, 979, 366, 299, 675, 1456],
            2020,
            (1721, 299),
        )
    ]
)
def test_find_sum_pair(numbers, target, expected):
    assert set(find_sum_pair(numbers, target)) == set(expected)

@pytest.mark.parametrize(
    ("numbers", "target", "expected"),
    [
        (
            [1721, 979, 366, 299, 675, 1456],
            2020,
            514579,
        ),
    ]
)
def test_fix_expense_report(numbers, target, expected):
    result = fix_expense_report(numbers, target)
    assert result == expected
    