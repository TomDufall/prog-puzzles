from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class BootCode:
    instructions: List[str]

    def detect_loop(self) -> int:
        i = 0
        visited = set()
        acc = 0
        while i not in visited:
            visited.add(i)
            instr, num = self.instructions[i].split()
            if instr == "nop":
                i += 1
            elif instr == "acc":
                i += 1
                acc += int(num)
            elif instr == "jmp":
                i += int(num)
            else:
                raise ValueError(f"Unrecognised instruction: {instr}")
            if i >= len(self.instructions):
                # No loop
                return None
        return acc



if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    instructions = filepath.read_text().splitlines()
    code = BootCode(instructions)
    print(code.detect_loop())