from part2 import rolling_window_sum


def test_rolling_window_sum():
    input_ = [607, 618, 618, 617, 647, 716, 769, 792]
    expected = [1843, 1853, 1882, 1980, 2132, 2277]
    assert rolling_window_sum(input_, 3) == expected
