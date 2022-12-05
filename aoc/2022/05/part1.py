from dataclasses import dataclass


@dataclass
class CrateStore:
    stacks: list[list[str]]

    @property
    def top_crates(self):
        return [stack[-1] for stack in self.stacks]

    def rearrange(self, instructions: list[tuple[int, int, int]]):
        for count, start, end in instructions:
            for i in range(count):
                self.stacks[end - 1].append(self.stacks[start - 1].pop())

def load_input(
    filepath: str = "input.txt",
) -> tuple[CrateStore, list[tuple[int, int, int]]]:
    with open(filepath) as f:
        crate_text, move_text = f.read().split("\n\n")
    width = int(crate_text[-2]) # doesn't handle > 1 char
    crate_store = CrateStore([[] for i in range(width)])
    for line in reversed(crate_text.splitlines()[:-1]):
        for i in range(width):
            label = line[i*4 + 1]
            if label == " ":
                continue
            crate_store.stacks[i].append(label)

    moves = []
    for _, count, _, start, _, end in map(lambda x: x.split(), move_text.splitlines()):
        moves.append((int(count), int(start), int(end)))
    return crate_store, moves


if __name__ == "__main__":
    crate_store, instructions = load_input()
    crate_store.rearrange(instructions)
    answer = "".join(crate_store.top_crates)
    print(f"Day 5 part 1: {answer}")
