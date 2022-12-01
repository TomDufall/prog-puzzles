from part1 import find_max_sum, load_input


def test_part1():
    input_ = load_input("sample_input.txt")
    assert find_max_sum(input_) == 24000
