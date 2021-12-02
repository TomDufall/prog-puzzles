from part1 import calculate_endpoint


def test_calculate_endpoint():
    instructions = [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]
    expected = 15, -10
    assert calculate_endpoint(instructions) == expected
