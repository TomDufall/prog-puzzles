from part1 import score_commons


def find_commons(bags: list[tuple[str, str]]) -> list[str]:
    lines = iter(bags)
    commons = []
    while True:
        try:
            a, b, c = next(lines), next(lines), next(lines)
        except StopIteration:
            break
        commons.append(next(iter(set(a[:-1]).intersection(b[:-1], c[:-1]))))
    return commons


def load_input(filepath: str = "input.txt") -> list[tuple[str, str]]:
    parsed = []
    with open(filepath) as f:
        return f.readlines()


if __name__ == "__main__":
    input_ = load_input()
    commons = find_commons(input_)
    answer = score_commons(commons)
    print(f"Part 2: {answer}")
