from collections import defaultdict
from functools import reduce
from operator import mul

def parse_input(filename: str = "input.txt") -> list[dict[str, int]]:
    with open(filename) as f:
        text = f.read().splitlines()
    bags = []
    for line in text:
        bag = defaultdict(int)
        game_id_str, rounds_str = line.split(": ")
        game_id = int(game_id_str.split(" ")[-1])
        valid = True
        for round_str in rounds_str.split("; "):
            for req in round_str.split(", "):
                num, colour = req.split(" ")
                num = int(num)
                if num > bag[colour]:
                    bag[colour] = num
        bags.append(bag)
    return bags

def calculate_result(bags: list[dict[str, int]]) -> int:
    total = 0
    for bag in bags:
        power = reduce(mul, bag.values(), 1)
        total += power
    return total

if __name__ == "__main__":
    bags = parse_input()
    result = calculate_result(bags)
    print(result)