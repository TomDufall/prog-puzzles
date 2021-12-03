from part2 import calc_oxygen_rating, calculate_co2_rating, filter_numbers, most_common


def test_most_common():
    numbers = ["1", "1", "0"]
    assert most_common(numbers) == "1"


def test_most_common_tie():
    numbers = ["1", "0"]
    assert most_common(numbers) == "1"


def test_most_common_missing():
    numbers = ["0"] * 5
    assert most_common(numbers) == "0"


def test_filter_numbers():
    criteria = lambda numbers: "1"
    input_ = ["110", "111", "010"]
    assert filter_numbers(input_, criteria) == "111"
