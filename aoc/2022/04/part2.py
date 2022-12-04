from part1 import load_input


def count_redundant_pairs(pairs: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
    total = 0
    for (a_min, a_max), (b_min, b_max) in pairs:
        if (
            (b_min <= a_min <= b_max)
            or (b_min <= a_max <= b_max)
            or (a_min <= b_min <= a_max)
            or (a_min <= b_max <= a_max)
        ):
            total += 1
    return total


if __name__ == "__main__":
    pairs = load_input()
    answer = count_redundant_pairs(pairs)
    print(f"Part 1 answer: {answer}")
