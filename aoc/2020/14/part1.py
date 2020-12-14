from pathlib import Path
from typing import List, Tuple


def run(instrs: List[Tuple[str, str, str]]) -> int:
    memory = {}
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    for instr, addr, value in instrs:
        if instr == "mask":
            mask = value
        elif instr == "mem":
            value_bin = bin(int(value)).split("b", 1)[1]
            if len(value_bin) < len(mask):
                extras = len(mask) - len(value_bin)
                value_bin = "0" * extras + value_bin
                masked_value = []
                for i in range(len(mask)):
                    mask_op = mask[i]
                    if mask_op == "X":
                        masked_value.append(value_bin[i])
                    else:
                        masked_value.append(mask_op)
                result = int("".join(masked_value), 2)
                memory[addr] = result
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
