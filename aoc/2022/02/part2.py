from part1 import load_input, score_round


def decode_round(other: str, outcome: str) -> int:
    if outcome == "X":
        if other == "A":
            self = "Z"
        elif other == "B":
            self = "X"
        elif other == "C":
            self = "Y"
    elif outcome == "Y":
        # draw
        self = other
    elif outcome == "Z":
        if other == "A":
            self = "Y"
        elif other == "B":
            self = "Z"
        elif other == "C":
            self = "X"
    return other, self


def score_strategy(strategy: list[tuple[str, str]]) -> int:
    total = 0
    for other, self in strategy:
        other, self = decode_round(other, self)
        total += score_round(other, self)
    return total


if __name__ == "__main__":
    strategy = load_input()
    answer = score_strategy(strategy)
    print(f"Part 2: {answer}")
