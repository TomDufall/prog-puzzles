from part1 import checksum, frequencies

SAMPLE_INPUT = [
    "abcdef",
    "bababc",
    "abbcde",
    "abcccd",
    "aabcdd",
    "abcdee",
    "ababab",
]


def test_frequencies():
    input_ = "ababbcdddd"
    expected = {
        "a": 2,
        "b": 3,
        "c": 1,
        "d": 4,
    }
    assert frequencies(input_) == expected


def test_checksum():
    assert checksum(SAMPLE_INPUT) == 12
