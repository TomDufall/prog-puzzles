import pytest

from part2 import find_mod_result, find_solution, find_solution_simple, load_list

@pytest.mark.parametrize(
    ("repeater", "mod", "start", "target", "expected"),
    [
        (7, 13, 0, 2, 4)
    ]
)
def test_find_mod_result(repeater, mod, start, target, expected):
    assert find_mod_result(repeater, mod, start, target) == expected


@pytest.mark.parametrize(
    ("expected", "ids"),
    [
        (
            3417,
            ["17", "x", "13", "19"],
        ),
        (
            754018, 
            ["67", "7", "59", "61"],
        ),
        (
            779210,
            ["67", "x", "7", "59", "61"],
        ),
        (
            1261476,
            ["67", "7", "x", "59", "61"],
        ),
        (
            1202161486,
            ["1789", "37", "47", "1889"],
        ),
    ]
)
def test_find_solution(ids, expected):
    assert find_solution(load_list(ids)) == expected


@pytest.mark.parametrize(
    ("expected", "ids"),
    [
        (
            3417,
            ["17", "x", "13", "19"],
        ),
        (
            754018, 
            ["67", "7", "59", "61"],
        ),
        (
            779210,
            ["67", "x", "7", "59", "61"],
        ),
        (
            1261476,
            ["67", "7", "x", "59", "61"],
        ),
        (
            1202161486,
            ["1789", "37", "47", "1889"],
        ),
    ]
)
def test_find_solution_simple(ids, expected):
    assert find_solution_simple(load_list(ids)) == expected
