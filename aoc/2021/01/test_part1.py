from part1 import count_increases


def test_count_increase():
    input_ = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected = 7
    assert count_increases(input_) == expected
