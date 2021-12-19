from itertools import product
import pytest

from solution import (
    ALL_ROTATIONS,
    _find_overlapping_pairs,
    find_max_scanner_distance,
    load_input,
    Point3D,
    _try_match_scanner_pair,
    merge_scanners,
)


def test_all_rotations():
    assert len(ALL_ROTATIONS) == 24


def test_load_input():
    expected = [
        {
            Point3D(404, -588, -901),
            Point3D(528, -643, 409),
            Point3D(-838, 591, 734),
        },
        {
            Point3D(686, 422, 578),
            Point3D(605, 423, 415),
            Point3D(515, 917, -361),
        },
        {
            Point3D(649, 640, 665),
            Point3D(682, -795, 504),
            Point3D(-784, 533, -524),
        },
    ]
    actual = load_input("loading_sample.txt")
    assert actual == expected


def test_point_rotate():
    start = Point3D(1, 2, 3)
    points = set()
    for rotation in ALL_ROTATIONS:
        point = start.rotate(*rotation)
        points.add(point)
    assert len(points) == 24


def test_point_calc_translation():
    one = Point3D(1, 2, 3)
    two = Point3D(2, 6, 14)
    expected = Point3D(-1, -4, -11)
    assert one.calc_translation(two) == expected


def test_point_translation():
    start = Point3D(1, 2, 3)
    translation = Point3D(4, 7, 12)
    expected = Point3D(5, 9, 15)
    assert start.translate(translation) == expected


@pytest.mark.parametrize(("a", "b"), [(0, 1), (1, 4)])
def test_try_match_scanner_pair_from_sample(a, b):
    scanners = load_input("sample_input.txt")
    assert _try_match_scanner_pair(scanners[a], scanners[b])


def test_find_overlapping_pairs():
    scanners = load_input("sample_input.txt")
    pairs = _find_overlapping_pairs(scanners)
    assert len(pairs) >= len(scanners) - 1


def test_merge_scanners_merged_points():
    scanners = load_input("sample_input.txt")
    merged, _ = merge_scanners(scanners)
    assert len(merged) == 79


def test_merge_scanners_scanner_locations():
    scanners = load_input("sample_input.txt")
    _, scanner_locations = merge_scanners(scanners)
    assert scanner_locations[0] == Point3D(0, 0, 0)
    assert scanner_locations[2] == Point3D(1105, -1205, 1229)
    assert scanner_locations[3] == Point3D(-92, -2380, -20)


def test_manhattan_distance():
    assert (
        Point3D(1105, -1205, 1229).manhattan_distance(Point3D(-92, -2380, -20)) == 3621
    )


def test_find_max_scanner_distance():
    scanners = load_input("sample_input.txt")
    _, scanner_locations = merge_scanners(scanners)
    assert find_max_scanner_distance(scanner_locations) == 3621
