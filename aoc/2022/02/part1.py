SHAPE_SCORE = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

CODE_TO_SHAPE = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}


def score_round(other: str, self: str) -> int:
    other, self = CODE_TO_SHAPE[other], CODE_TO_SHAPE[self]
    if other == self:
        win_score = 3
    elif (
        (other == "rock" and self == "paper")
        or (other == "paper" and self == "scissors")
        or (other == "scissors" and self == "rock")
    ):
        win_score = 6
    else:
        win_score = 0
    return win_score + SHAPE_SCORE[self]


def score_strategy(strategy: list[tuple[str, str]]) -> int:
    total = 0
    for other, self in strategy:
        total += score_round(other, self)
    return total


def load_input(filepath: str = "input.txt") -> list[tuple[str, str]]:
    with open(filepath) as f:
        return [tuple(line.split()) for line in f.readlines()]


if __name__ == "__main__":
    strategy = load_input()
    answer = score_strategy(strategy)
    print(f"Part 1: {answer}")
