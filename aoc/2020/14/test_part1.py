from pathlib import Path

from part1 import load_input, run


def test_run():
    instrs = [
        ("mask", "", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"),
        ("mem", "8", "11"),
        ("mem", "7", "101"),
        ("mem", "8", "0"),
    ]
    expected = 165
    assert run(instrs) == expected


def test_load_input():
    filepath = Path(__file__).parent / "sample_input_1.txt"
    expected = [
        ("mask", "", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"),
        ("mem", "8", "11"),
        ("mem", "7", "101"),
        ("mem", "8", "0"),
    ]
    assert load_input(filepath) == expected
