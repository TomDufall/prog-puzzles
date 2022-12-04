from part1 import load_input
from part2 import count_redundant_pairs


def test_part2():
    input_ = load_input("sample_input.txt")
    assert count_redundant_pairs(input_) == 4
