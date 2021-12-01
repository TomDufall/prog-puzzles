from part1 import calculate_drift


def test_calculate_drift():
    assert calculate_drift(["+5", "-4", "3"]) == 4
