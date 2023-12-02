bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def parse_input(filename: str = "input.txt") -> int:
    with open(filename) as f:
        text = f.read().splitlines()
    possible_rounds = []
    for line in text:
        game_id_str, rounds_str = line.split(": ")
        game_id = int(game_id_str.split(" ")[-1])
        valid = True
        for round_str in rounds_str.split("; "):
            for req in round_str.split(", "):
                num, colour = req.split(" ")
                if int(num) > bag[colour]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            possible_rounds.append(game_id)
    return sum(possible_rounds)



if __name__ == "__main__":
    result = parse_input()
    print(result)