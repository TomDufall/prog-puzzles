from part1 import count_dangerous_areas, Line2D, Point2D
from part2 import map_vent_density_full


def test_map_vent_density_full_diagonal_forward():
    lines = [Line2D(Point2D(0, 0), Point2D(3, 3))]
    expected = {
        Point2D(0, 0): 1,
        Point2D(1, 1): 1,
        Point2D(2, 2): 1,
        Point2D(3, 3): 1,
    }
    assert map_vent_density_full(lines) == expected


def test_map_vent_density_full_diagonal_backward():
    lines = [Line2D(Point2D(3, 3), Point2D(0, 0))]
    expected = {
        Point2D(0, 0): 1,
        Point2D(1, 1): 1,
        Point2D(2, 2): 1,
        Point2D(3, 3): 1,
    }
    assert map_vent_density_full(lines) == expected


def test_map_vent_density_full_diagonal_tricky():
    lines = [Line2D(Point2D(9, 7), Point2D(7, 9))]
    expected = {
        Point2D(9, 7): 1,
        Point2D(8, 8): 1,
        Point2D(7, 9): 1,
    }
    assert map_vent_density_full(lines) == expected


def test_map_vent_density_full_horz_forward():
    lines = [Line2D(Point2D(0, 0), Point2D(3, 0))]
    expected = {
        Point2D(0, 0): 1,
        Point2D(1, 0): 1,
        Point2D(2, 0): 1,
        Point2D(3, 0): 1,
    }
    assert map_vent_density_full(lines) == expected


def test_part2():
    lines = [
        Line2D(Point2D(0, 9), Point2D(5, 9)),
        Line2D(Point2D(8, 0), Point2D(0, 8)),
        Line2D(Point2D(9, 4), Point2D(3, 4)),
        Line2D(Point2D(2, 2), Point2D(2, 1)),
        Line2D(Point2D(7, 0), Point2D(7, 4)),
        Line2D(Point2D(6, 4), Point2D(2, 0)),
        Line2D(Point2D(0, 9), Point2D(2, 9)),
        Line2D(Point2D(3, 4), Point2D(1, 4)),
        Line2D(Point2D(0, 0), Point2D(8, 8)),
        Line2D(Point2D(5, 5), Point2D(8, 2)),
    ]
    assert (count_dangerous_areas(map_vent_density_full(lines))) == 12
