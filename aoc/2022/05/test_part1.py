from part1 import load_input, CrateStore

class CrateStore2(CrateStore)
    def rearrange(self, instructions: list[tuple[int, int, int]]):
        for count, start, end in instructions:
            buffer = []
            for i in range(count):
                buffer.append(self.stacks[start - 1].pop())
            self.stacks[end - 1].extend(reversed(buffer))

if __name__ == "__main__":
    crate_store, instructions = load_input("sample_input.txt")
    crate_store.rearrange(instructions)
    answer = "".join(crate_store.top_crates)
    print(f"Day 5 part 2: {answer}")
