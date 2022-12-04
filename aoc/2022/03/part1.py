import string

LETTERS = {
    key: val
    for val, key in enumerate(
        [*string.ascii_lowercase, *string.ascii_uppercase], start=1
    )
}


def score_commons(commons: list[str]) -> int:
    return sum(map(lambda char: LETTERS[char], commons))


def find_commons(bags: list[tuple[str, str]]) -> list[str]:
    commons = []
    for a, b in bags:
        commons.append(next(iter(set(a).intersection(b))))
    return commons


def load_input(filepath: str = "input.txt") -> list[tuple[str, str]]:
    parsed = []
    with open(filepath) as f:
        for line in f.readlines():
            length = len(line)
            parsed.append((line[: length // 2], line[length // 2 : -1]))
    return parsed


if __name__ == "__main__":
    input_ = load_input()
    commons = find_commons(input_)
    answer = score_commons(commons)
    print(f"Part 1: {answer}")
