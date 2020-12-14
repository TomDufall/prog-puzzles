from pathlib import Path

import pytest

from part2 import load_input, resolve_address, run


@pytest.mark.parametrize(
    ("address", "mask", "expected"),
    [
        (
            42,
            "000000000000000000000000000000X1001X",
            [26, 27, 58, 59],
        ),
        (
            26,
            "00000000000000000000000000000000X0XX",
            [16, 17, 18, 19, 24, 25, 26, 27],
        ),
    ]
)
def test_resolve_address(address, mask, expected):
    assert set(resolve_address(address, mask)) == set(expected)


def test_run():
    instrs = [
        ("mask", "", "000000000000000000000000000000X1001X"),
        ("mem", "42", "100"),
        ("mask", "", "00000000000000000000000000000000X0XX"),
        ("mem", "26", "1"),
    ]
    expected = 208
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
