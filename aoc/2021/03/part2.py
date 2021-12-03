from typing import Callable, List

from part1 import load_input


def filter_numbers(numbers: List[str], calculate_criteria: Callable) -> str:
    for i in range(len(numbers[0])):
        if len(numbers) == 1:
            break
        keep_value = calculate_criteria([number[i] for number in numbers])
        numbers = list(filter(lambda n: n[i] == keep_value, numbers))
    if len(numbers) == 1:
        return numbers[0]
    raise Exception("Failed to fully filter numbers")


def most_common(numbers: List[str]) -> str:
    count = {}
    for number in numbers:
        count[number] = count.get(number, 0) + 1
    return "1" if count.get("1", 0) >= count.get("0", 0) else "0"


def calc_oxygen_rating(numbers: List[str]) -> str:
    return filter_numbers(numbers, most_common)


def calculate_co2_rating(numbers: List[str]) -> str:
    def least_common(numbers: List[str]) -> str:
        count = {}
        for number in numbers:
            count[number] = count.get(number, 0) + 1
        return "0" if count.get("0", 0) <= count.get("1", 0) else "1"

    return filter_numbers(numbers, least_common)


if __name__ == "__main__":
    input_ = load_input()
    oxygen_str = calc_oxygen_rating(input_)
    co2_string = calculate_co2_rating(input_)
    print(oxygen_str, co2_string)
    print(int(oxygen_str, 2), int(co2_string, 2))
    print(int(oxygen_str, 2) * int(co2_string, 2))
