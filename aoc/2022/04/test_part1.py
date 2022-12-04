from part1 import count_redundant_pairs, load_input


def test_part1():
    input_ = load_input("sample_input.txt")
    assert count_redundant_pairs(input_) == 2
