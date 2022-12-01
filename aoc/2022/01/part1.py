def load_input(filename: str = "input.txt") -> str:
    with open(filename) as f:
        return f.read()


def find_max_sum(text: str):
    max_ = 0
    for block in text.split("\n\n"):
        total = 0
        for line in block.split("\n"):
            total += int(line)
        max_ = max(max_, total)
    return max_


if __name__ == "__main__":
    input_ = load_input()
    answer = find_max_sum(load_input())
    print(f"Part 1: {answer}")
