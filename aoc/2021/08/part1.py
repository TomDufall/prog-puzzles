from __future__ import annotations


def load_input(filepath: str = "input.txt") -> list[tuple[list[str], list[str]]]:
    data: list[tuple[list[str], list[str]]] = []
    with open(filepath) as f:
        for line in f.read().splitlines():
            patterns_raw, outputs_raw = line.split(" | ")
            data.append((patterns_raw.split(), outputs_raw.split()))
    return data


def count_simple_digits(data: list[tuple[list[str], list[str]]]) -> int:
    """
    Count occurances of the simple to identify digits in the output - 1, 4, 7,
    8. These are easy to spot as they are the only digits with 2, 4, 3, and 7
    segments, respectively.
    """
    count = 0
    for _, outputs in data:
        for output in outputs:
            if len(output) in {2, 4, 3, 7}:
                count += 1
    return count


if __name__ == "__main__":
    data = load_input()
    simple_digits_count = count_simple_digits(data)
    print(simple_digits_count)
