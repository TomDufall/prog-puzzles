import pytest

from part1 import (
    _can_explode,
    _can_split,
    _explode,
    _split,
    magnitude,
    reduce,
    snail_sum,
)


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        ([[[[[9, 8], 1], 2], 3], 4], [0, 0, 0, 0]),
        ([7, [6, [5, [4, [3, 2]]]]], [1, 1, 1, 1]),
        ([[6, [5, [4, [3, 2]]]], 1], [0, 1, 1, 1]),
        ([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]], [0, 1, 1, 1]),
        ([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], [1, 1, 1, 1]),
    ],
)
def test_can_explode(n, expected):
    actual = _can_explode(n)
    assert actual == expected


@pytest.mark.parametrize(
    ("n", "location", "expected"),
    [
        ([[[[[9, 8], 1], 2], 3], 4], [0, 0, 0, 0], [[[[0, 9], 2], 3], 4]),
        ([7, [6, [5, [4, [3, 2]]]]], [1, 1, 1, 1], [7, [6, [5, [7, 0]]]]),
        ([[6, [5, [4, [3, 2]]]], 1], [0, 1, 1, 1], [[6, [5, [7, 0]]], 3]),
        (
            [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]],
            [0, 1, 1, 1],
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
        ),
        (
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
            [1, 1, 1, 1],
            [[3, [2, [8, 0]]], [9, [5, [7, 0]]]],
        ),
    ],
)
def test_explode(n, location, expected):
    actual = _explode(n, location)
    assert actual == expected


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        ([[[[0, 7], 4], [15, [0, 13]]], [1, 1]], [0, 1, 0]),
        ([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]], [0, 1, 1, 1]),
    ],
)
def test_can_split(n, expected):
    actual = _can_split(n)
    assert actual == expected


@pytest.mark.parametrize(
    ("n", "location", "expected"),
    [
        (
            [[[[0, 7], 4], [15, [0, 13]]], [1, 1]],
            [0, 1, 0],
            [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]],
        ),
        (
            [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]],
            [0, 1, 1, 1],
            [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]],
        ),
    ],
)
def test_split(n, location, expected):
    actual = _split(n, location)
    assert actual == expected


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (
            [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]],
            [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]],
        )
    ],
)
def test_reduce(n, expected):
    actual = reduce(n)
    assert actual == expected


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        (
            [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]],
            [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]],
        ),
        ([[1, 1], [2, 2], [3, 3], [4, 4]], [[[[1, 1], [2, 2]], [3, 3]], [4, 4]]),
        (
            [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
            [[[[3, 0], [5, 3]], [4, 4]], [5, 5]],
        ),
    ],
)
def test_snail_sum(numbers, expected):
    actual = snail_sum(numbers)
    assert actual == expected


@pytest.mark.parametrize(
    ("n", "expected"),
    [([[1, 2], [[3, 4], 5]], 143), ([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], 1384)],
)
def test_magnitude(n, expected):
    actual = magnitude(n)
    assert actual == expected
