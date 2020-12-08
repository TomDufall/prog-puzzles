from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple


@dataclass
class BootCode:
    instructions: List[str]

    def run(self) -> Tuple[bool, int]:
        # return (success, acc)
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
                return (True, acc)
        return (False, acc)

    @staticmethod
    def heal_code(instructions) -> BootCode:
        mutation_points = (
            i for i in range(len(instructions))
            if instructions[i].split()[0] in ("jmp", "nop")
        )
        for i in mutation_points:
            instr, num = instructions[i].split()
            if instr == "nop":
                instr = "jmp"
            else:
                instr = "nop"
            instrs = instructions.copy()
            instrs[i] = f"{instr} {num}"
            bootcode = BootCode(instrs)
            success, acc = bootcode.run()
            if success:
                return bootcode


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    instructions = filepath.read_text().splitlines()
    print(BootCode.heal_code(instructions).run())