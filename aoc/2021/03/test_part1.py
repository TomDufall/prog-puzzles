from part1 import calculate_most_common_bits


def test_calculate_most_common_bits():
    input_ = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    expected = "10110"
    assert calculate_most_common_bits(input_) == expected
