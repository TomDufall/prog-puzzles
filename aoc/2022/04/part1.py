def count_redundant_pairs(pairs: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
    total = 0
    for (a_min, a_max), (b_min, b_max) in pairs:
        if (a_min <= b_min and a_max >= b_max) or (b_min <= a_min and b_max >= a_max):
            total += 1
    return total


def load_input(
    filepath: str = "input.txt",
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    pairs = []
    with open(filepath) as f:
        for a, b in map(lambda l: l.split(","), f.readlines()):
            pairs.append((tuple(map(int, a.split("-"))), tuple(map(int, b.split("-")))))
    return pairs


if __name__ == "__main__":
    pairs = load_input()
    answer = count_redundant_pairs(pairs)
    print(f"Part 1 answer: {answer}")
