import pytest

from part2 import find_sum_group, fix_expense_report

@pytest.mark.parametrize(
    ("numbers", "target", "group_size", "expected"),
    [
        (
            [1721, 979, 366, 299, 675, 1456],
            2020,
            2,
            (1721, 299),
        ),
        (
            [1721, 979, 366, 299, 675, 1456],
            2020,
            3,
            (979, 366, 675),
        ),
    ]
)
def test_find_sum_pair(numbers, target, group_size, expected):
    result = find_sum_group(numbers, target, group_size)
    assert sorted(result) == sorted(expected)

@pytest.mark.parametrize(
    ("numbers", "target", "group_size", "expected"),
    [
        (
            [1721, 979, 366, 299, 675, 1456],
            2020,
            2,
            514579,
        ),
        (
            [1721, 979, 366, 299, 675, 1456],
            2020,
            3,
            241861950,
        ),
    ]
)
def test_fix_expense_report(numbers, target, group_size, expected):
    result = fix_expense_report(numbers, target, group_size)
    assert result == expected
