from part1 import count_simple_digits


def test_count_simple_digits():
    data = [([], ["fgae", "cfgab", "fg", "bagce"])]
    expected = 2
    assert count_simple_digits(data) == expected
