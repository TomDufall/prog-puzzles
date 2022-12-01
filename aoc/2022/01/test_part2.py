from part1 import load_input
from part2 import sum_elf_foods, sum_top_three_elves


def test_sum_elves():
    input_ = "1\n2\n3\n\n1\n4"
    expected = [6, 5]
    assert sum_elf_foods(input_) == expected


def test_sum_top_three_elves():
    input_ = "2\n\n1\n\n2\n4\n\n10"
    expected = 18
    assert sum_top_three_elves(input_) == expected


def test_part2():
    input_ = load_input("sample_input.txt")
    assert sum_top_three_elves(input_) == 45000
