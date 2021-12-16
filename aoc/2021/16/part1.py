from __future__ import annotations
from abc import ABC

from dataclasses import dataclass
from itertools import count, islice


class Packet(ABC):
    pass


@dataclass
class ValuePacket(Packet):
    version: int  # 3 bit
    type_id: int  # 3 bit
    value: int


@dataclass
class OperatorPacket(Packet):
    version: int
    type_id: int
    subpackets: list[Packet]


def split_packets(bin_str: str, max_packets: int = -1) -> list[Packet]:
    chars = iter(bin_str)
    packets = []
    try:
        while True:
            if max_packets != -1 and len(packets) >= max_packets:
                break
            try:
                version = int("".join(islice(chars, 3)), 2)
                type_id = int("".join(islice(chars, 3)), 2)
            except ValueError:
                # Finished?
                break

            if type_id == 4:
                # Literal value packet
                # While first bit is 0, keep reading
                value_parts = []
                while True:
                    more, *bits = islice(chars, 5)
                    value_parts.extend(bits)
                    if more != "1":
                        break
                value_str = "".join(value_parts)
                value = int(value_str, 2)
                packet = ValuePacket(version, type_id, value)
                packets.append(packet)
            else:
                # Operator packet
                length_type_id = next(chars)
                if length_type_id == "0":
                    # next 15 bits are the length of the sub-packets in the packet
                    length_str = "".join(islice(chars, 15))
                    if length_str == "":
                        break
                    length = int(length_str, 2)
                    sub_packets_str = "".join(islice(chars, length))
                    sub_packets = split_packets(sub_packets_str)
                    packet = OperatorPacket(version, type_id, sub_packets)
                    packets.append(packet)
                else:  # 1
                    # Next 11 bits are the number of sub-packets immediately contained by this packet
                    sub_packet_count = int("".join(islice(chars, 11)), 2)
                    sub_packets = split_packets(chars, max_packets=sub_packet_count)
                    packet = OperatorPacket(version, type_id, sub_packets)
                    packets.append(packet)
    except StopIteration:
        pass
    return packets


def hex_to_bin(char: str) -> str:
    return f"{int(char, 16):04b}"


def hexes_to_bin(s: str) -> str:
    return "".join([hex_to_bin(char) for char in s])


def load_input(filepath: str = "input.txt") -> str:
    with open(filepath) as f:
        return f.read()


def sum_version_numbers(packets: list[Packet]) -> int:
    acc = 0
    for packet in packets:
        acc += packet.version
        if isinstance(packet, OperatorPacket):
            acc += sum_version_numbers(packet.subpackets)
    return acc


if __name__ == "__main__":
    input_ = load_input()
    binary = hexes_to_bin(input_)
    packets = split_packets(binary)
    print(sum_version_numbers(packets))
