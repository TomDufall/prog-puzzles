def load_input(filename: str = "input.txt") -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()


def keep_digits(string: str) -> str:
    result = ""
    for char in string:
        if char in "0123456789":
            result += char
    return result


def parse_input(_input: str) -> int:
    total = 0
    for line in _input:
        digits = keep_digits(line)
        total += int(f"{digits[0]}{digits[-1]}")
    return total


if __name__ == "__main__":
    _input = load_input()
    print(parse_input(_input))
