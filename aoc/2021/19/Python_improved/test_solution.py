from itertools import product
import pytest

from solution import (
    ALL_ROTATIONS,
    calc_point_translation,
    find_max_scanner_distance,
    _find_overlapping_pair,
    load_input,
    manhattan_distance,
    merge_scanners_lazy,
    point_rotate,
    point_transform,
    point_translate,
    _try_match_scanner_pair,
    _try_match_scanner_pair_no_rotation,
)


def test_all_rotations():
    assert len(ALL_ROTATIONS) == 24


def test_load_input():
    expected = [
        {
            (404, -588, -901),
            (528, -643, 409),
            (-838, 591, 734),
        },
        {
            (686, 422, 578),
            (605, 423, 415),
            (515, 917, -361),
        },
        {
            (649, 640, 665),
            (682, -795, 504),
            (-784, 533, -524),
        },
    ]
    actual = load_input("loading_sample.txt")
    assert actual == expected


def test_point_rotate():
    start = (1, 2, 3)
    points = set()
    for rotation in ALL_ROTATIONS:
        point = point_rotate(start, *rotation)
        points.add(point)
    assert len(points) == 24


def test_point_calc_translation():
    one = (1, 2, 3)
    two = (2, 6, 14)
    expected = (-1, -4, -11)
    assert calc_point_translation(one, two) == expected


def test_point_translation():
    start = (1, 2, 3)
    translation = (4, 7, 12)
    expected = (5, 9, 15)
    assert point_translate(start, translation) == expected


@pytest.mark.parametrize(("a", "b"), [(0, 1), (1, 4)])
def test_try_match_scanner_pair_from_sample(a, b):
    scanners = load_input("sample_input.txt")
    assert _try_match_scanner_pair(scanners[a], scanners[b])


def test_merge_scanners_lazy_merged_point():
    scanners = load_input("sample_input.txt")
    merged, _ = merge_scanners_lazy(scanners)
    assert len(merged) == 79


def test_merge_scanners_lazy_scanner_locations():
    scanners = load_input("sample_input.txt")
    _, scanner_locations = merge_scanners_lazy(scanners)
    assert scanner_locations[0] == (0, 0, 0)
    assert scanner_locations[2] == (1105, -1205, 1229)
    assert scanner_locations[3] == (-92, -2380, -20)


def test_manhattan_distance():
    point_a = (1105, -1205, 1229)
    point_b = (-92, -2380, -20)
    expected = 3621
    assert manhattan_distance(point_a, point_b) == expected


def test_find_max_scanner_distance():
    scanners = load_input("sample_input.txt")
    _, scanner_locations = merge_scanners_lazy(scanners)
    assert find_max_scanner_distance(scanner_locations) == 3621
