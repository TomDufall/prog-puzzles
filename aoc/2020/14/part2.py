from itertools import product
from pathlib import Path
from typing import Iterator, List, Tuple


def resolve_address(addr: int, mask: str) -> Iterator[int]:
    addr_bin = bin(addr)[2:].zfill(36)
    # Apply 1 mask
    masked_addr_parts = []
    for i in range(len(mask)):
        mask_op = mask[i]
        if mask_op == "0":
            masked_addr_parts.append(addr_bin[i])
        else:
            masked_addr_parts.append(mask_op)
    masked_addr = "".join(masked_addr_parts)
    # Expand possibilities for Xs - 0 or 1
    bit_values = product({0, 1}, repeat=mask.count("X"))
    while True:
        try:
            values = iter(next(bit_values))
        except StopIteration:
            return
        resolved_addr = []
        for i in range(len(masked_addr)):
            if masked_addr[i] == "X":
                resolved_addr.append(str(next(values)))
            else:
                resolved_addr.append(masked_addr[i])
        yield int("".join(resolved_addr), 2)


def run(instrs: List[Tuple[str, str, str]]) -> int:
    memory = {}
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    for instr, addr, value in instrs:
        if instr == "mask":
            mask = value
        elif instr == "mem":
            addrs = resolve_address(int(addr), mask)
            for resolved_addr in addrs:
                memory[resolved_addr] = int(value)
        else:
            raise ValueError(f"Unrecognised instruction: {instr}")
    return sum(memory.values())


def load_input(filepath: Path) -> List[Tuple[str, str, str]]:
    instructions = []
    for line in filepath.read_text().splitlines():
        instr, value = line.split(" = ")
        if instr == "mask":
            instructions.append((instr, "", value))
        elif instr.startswith("mem"):
            instr, addr = instr.split("[")
            addr = addr[:-1]
            instructions.append((instr, addr, value))
        else:
            raise ValueError(f"Unrecognised instruction: {instr}")
    return instructions


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    instrs = load_input(filepath)
    result = run(instrs)
    print(result)
