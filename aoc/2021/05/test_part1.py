from part1 import count_dangerous_areas, Point2D


def test_count_dangerous_areas():
    vent_count = {
        Point2D(0, 0): 1,
        Point2D(1, 1): 2,
        Point2D(2, 2): 3,
    }
    assert count_dangerous_areas(vent_count) == 2
