import pytest

from solution import (
    check_intercept,
    check_intercept_x,
    check_intercept_y,
    find_x_vel_candidates,
    search,
)


@pytest.mark.parametrize(
    ("x_min", "x_max", "velocity", "hits"),
    [
        (5, 10, 5, True),
        (5, 10, 4, True),
        (5, 10, 3, True),
        (5, 10, 2, False),
        (-6, -3, -6, True),
        (-6, -3, -2, True),
        (-6, -3, -1, False),
        (-6, -3, 3, False),
        (-5, 5, 1, True),
        (-5, 5, 0, True),
    ],
)
def test_check_intercept_x(x_min, x_max, velocity, hits):
    assert check_intercept_x(x_min, x_max, velocity) == hits


def test_find_x_vel_candidates():
    target = 20, 30
    expected = [
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
    ]
    assert find_x_vel_candidates(*target) == expected


@pytest.mark.parametrize(
    ("y_max", "y_min", "velocity", "hits"),
    [
        (-5, -10, 2, True),
        (-5, -10, 1, True),
        (-5, -10, -1, True),
        (-5, -10, -11, False),
    ],
)
def test_check_intercept_y(y_min, y_max, velocity, hits):
    assert check_intercept_y(y_min, y_max, velocity) == hits


@pytest.mark.parametrize(
    ("velocity", "hits"),
    [
        ((7, 2), True),
        ((6, 3), True),
        ((9, 0), True),
        ((17, -4), False),
    ],
)
def test_check_intercept(velocity, hits):
    target = (20, 30, -10, -5)
    assert check_intercept(*target, *velocity) == hits


def test_seach():
    target = ((20, 30), (-10, -5))
    candidates = search(target)
    assert max(candidates, key=lambda item: item[1]) == (6, 9)
