import pytest

from part1 import hexes_to_bin, split_packets
from part2 import evaluate_packet


@pytest.mark.parametrize(
    ("hex_str", "expected"),
    [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ],
)
def test_full(hex_str, expected):
    packets = split_packets(hexes_to_bin(hex_str))
    actual = evaluate_packet(packets[0])
    assert actual == expected
