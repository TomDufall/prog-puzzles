from part1 import load_input


def sum_elf_foods(text):
    elves = []
    for block in text.split("\n\n"):
        total = 0
        for line in block.split("\n"):
            total += int(line)
        elves.append(total)
    return elves


def sum_top_three_elves(text):
    elves = sorted(sum_elf_foods(text), reverse=True)
    return elves[0] + elves[1] + elves[2]


if __name__ == "__main__":
    input_ = load_input()
    answer = sum_top_three_elves(input_)
    print(f"Part 2: {answer}")
