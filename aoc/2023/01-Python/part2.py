words = {
    "thousand": 0,
    "hundred": 0,
    "ninety": 90,
    "eighty": 80,
    "seventy": 70,
    "sixty": 60,
    "fifty": 50,
    "fourty": 40,
    "thirty": 30,
    "twenty": 20,
    "nineteen": 19,
    "eighteen": 18,
    "seventeen": 17,
    "sixteen": 16,
    "fifteen": 15,
    "fourteen": 14,
    "thirteen": 13,
    "twelve": 12,
    "eleven": 11,
    "ten": 10,
    "nine": 9,
    "eight": 8,
    "seven": 7,
    "six": 6,
    "five": 5,
    "four": 4,
    "three": 3,
    "two": 2,
    "one": 1,
    "zero": 0,
}


def load_input(filename: str = "input.txt") -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()


def parse_digits(string: str) -> str:
    result = ""
    for i, char in enumerate(string):
        if char in "0123456789":
            result += char
        else:
            for word in words:
                if string[i:].startswith(word):
                    result += str(words[word])
                    continue
    return result


def parse_input(_input: list[str]) -> int:
    total = 0
    for line in _input:
        digits = parse_digits(line)
        # print(f"line: {line}, parsed: {digits}")
        total += int(f"{digits[0]}{digits[-1]}")
    return total


if __name__ == "__main__":
    _input = load_input()
    print(parse_input(_input))
