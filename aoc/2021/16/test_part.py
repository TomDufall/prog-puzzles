import pytest

from part1 import (
    hex_to_bin,
    hexes_to_bin,
    split_packets,
    sum_version_numbers,
    OperatorPacket,
    ValuePacket,
)


@pytest.mark.parametrize(
    ("bin_char", "expected"),
    [("F", "1111"), ("A", "1010"), ("9", "1001"), ("1", "0001"), ("0", "0000")],
)
def test_hex_to_bin(bin_char, expected):
    assert hex_to_bin(bin_char) == expected


@pytest.mark.parametrize(
    ("bin_str", "expected"),
    [
        ("9A", "10011010"),
        ("07", "00000111"),
        ("10", "00010000"),
    ],
)
def test_hexes_to_bin(bin_str, expected):
    assert hexes_to_bin(bin_str) == expected


def test_split_packets_value():
    bin_str = "110100101111111000101000"
    expected = [ValuePacket(6, 4, 2021)]
    assert split_packets(bin_str) == expected


def test_split_packets_operator():
    bin_str = "00111000000000000110111101000101001010010001001000000000"
    literal_1 = ValuePacket(6, 4, 10)
    literal_2 = ValuePacket(2, 4, 20)
    expected = OperatorPacket(1, 6, [literal_1, literal_2])
    assert split_packets(bin_str) == [expected]


def test_split_packets_operator():
    bin_str = "11101110000000001101010000001100100000100011000001100000"
    literal_1 = ValuePacket(2, 4, 1)
    literal_2 = ValuePacket(4, 4, 2)
    literal_3 = ValuePacket(1, 4, 3)
    expected = OperatorPacket(7, 3, [literal_1, literal_2, literal_3])
    assert split_packets(bin_str) == [expected]


def test_count_packets():
    literal_1 = ValuePacket(2, 4, 1)
    literal_2 = ValuePacket(4, 4, 2)
    literal_3 = ValuePacket(1, 4, 3)
    packets = [OperatorPacket(7, 3, [literal_1, literal_2, literal_3])]
    assert sum_version_numbers(packets) == 14


@pytest.mark.parametrize(
    ("hex_str", "expected"),
    [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_full(hex_str, expected):
    actual = sum_version_numbers(split_packets(hexes_to_bin(hex_str)))
    assert actual == expected
