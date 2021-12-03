from typing import Dict, Iterable, List


def calculate_most_common_bits(numbers: Iterable[str]) -> str:
    # Map of character index to character frequency dict
    frequencies: Dict[int, Dict[str, int]] = {}
    for number in numbers:
        for i, char in enumerate(number):
            if i not in frequencies:
                frequencies[i] = {}
            frequencies[i][char] = frequencies[i].get(char, 0) + 1
    return "".join(
        (max(d.items(), key=lambda item: item[1])[0]) for d in frequencies.values()
    )


def load_input(filepath: str = "input.txt") -> List[str]:
    with open(filepath) as f:
        return f.read().splitlines()


def invert_bin_string(string: str) -> str:
    return "".join(["1" if char == "0" else "0" for char in string])


if __name__ == "__main__":
    input_ = load_input()
    most_common_bits_str = calculate_most_common_bits(input_)
    least_common_bits_str = invert_bin_string(most_common_bits_str)
    most_common_bits = int(most_common_bits_str, 2)
    least_common_bits = int(least_common_bits_str, 2)
    print(most_common_bits_str, least_common_bits_str)
    print(most_common_bits, least_common_bits)
    print(most_common_bits * least_common_bits)
