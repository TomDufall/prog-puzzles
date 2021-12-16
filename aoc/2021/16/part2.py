from __future__ import annotations

from functools import reduce

from part1 import (
    load_input,
    hexes_to_bin,
    split_packets,
    Packet,
    ValuePacket,
    OperatorPacket,
)


def evaluate_packet(packet: Packet) -> int:
    if isinstance(packet, ValuePacket):
        return packet.value
    elif isinstance(packet, OperatorPacket):
        type_ = packet.type_id
        values = [evaluate_packet(subpacket) for subpacket in packet.subpackets]
        if type_ == 0:
            # Sum
            return sum(values)
        elif type_ == 1:
            # Product
            return reduce(lambda x, y: x * y, values, 1)
        elif type_ == 2:
            # Minimum
            return min(values)
        elif type_ == 3:
            # Maximum
            return max(values)
        elif type_ == 5:
            # Greater than
            if values[0] > values[1]:
                return 1
            return 0
        elif type_ == 6:
            # Less than
            if values[0] < values[1]:
                return 1
            return 0
        elif type_ == 7:
            # Equal to
            if values[0] == values[1]:
                return 1
            return 0
        else:
            raise ValueError("Unrecognised/unexpected packet type")
    else:
        raise ValueError("Unrecognised packet type")


if __name__ == "__main__":
    hex_str = load_input()
    bin_str = hexes_to_bin(hex_str)
    packets = split_packets(bin_str)
    answer = evaluate_packet(packets[0])
    print(answer)
