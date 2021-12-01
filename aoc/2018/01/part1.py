from typing import List


def calculate_drift(deltas: List[str], start: int = 0) -> int:
    total = start
    for delta in deltas:
        total += int(delta)
    return total


def load_input(filepath="input.txt") -> List[str]:
    with open(filepath) as f:
        return list(f.readlines())


if __name__ == "__main__":
    input_ = load_input()
    drift = calculate_drift(input_)
    print(drift)
