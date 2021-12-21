from __future__ import annotations


def deterministic_die_generator(sides: int = 100):
    def die_func():
        n = 1
        while True:
            yield n
            n += 1
            if n > sides:
                n = 1

    return die_func


def simplify(n):
    while n > 10:
        n -= 10
    return n


def play(a_space: int, b_space: int):
    a_score = 0
    b_score = 0
    die = deterministic_die_generator()()
    die_rolls = 0
    while True:
        a_move = next(die) + next(die) + next(die)
        die_rolls += 3
        a_space = simplify(a_space + a_move)
        a_score += a_space
        if a_score >= 1000:
            return b_score * die_rolls

        b_move = next(die) + next(die) + next(die)
        die_rolls += 3
        b_space = simplify(b_space + b_move)
        b_score += b_space
        if b_score >= 1000:
            return a_score * die_rolls


def load_input(filepath: str = "input.txt") -> tuple[int, int]:
    with open(filepath) as f:
        lines = f.read().splitlines()
    return int(lines[0].split()[-1]), int(lines[1].split()[-1])


if __name__ == "__main__":
    p1_start, p2_start = load_input()
    print(play(p1_start, p2_start))
