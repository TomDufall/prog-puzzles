from __future__ import annotations

from functools import cache
from itertools import product

from part1 import load_input, simplify

possible_three_rolls = list(product([1, 2, 3], [1, 2, 3], [1, 2, 3]))


@cache
def play(
    a_space: int,
    b_space: int,
    a_score: int = 0,
    b_score: int = 0,
    next_move: str = "a",
    max_score: int = 21,
) -> tuple[int, int]:
    """
    Return tuple of (a_win_count, b_win_count)
    """
    a_wins = b_wins = 0
    if next_move == "a":
        next_move = "b"
        for a_move in possible_three_rolls:
            possible_a_space = simplify(a_space + sum(a_move))
            possible_a_score = a_score + possible_a_space
            if possible_a_score >= max_score:
                a_wins += 1
            else:
                sub_a_wins, sub_b_wins = play(
                    possible_a_space,
                    b_space,
                    possible_a_score,
                    b_score,
                    next_move,
                    max_score,
                )
                a_wins += sub_a_wins
                b_wins += sub_b_wins
    elif next_move == "b":
        next_move = "a"
        for b_move in possible_three_rolls:
            possible_b_space = simplify(b_space + sum(b_move))
            possible_b_score = b_score + possible_b_space
            if possible_b_score >= max_score:
                b_wins += 1
            else:
                sub_a_wins, sub_b_wins = play(
                    a_space,
                    possible_b_space,
                    a_score,
                    possible_b_score,
                    next_move,
                    max_score,
                )
                a_wins += sub_a_wins
                b_wins += sub_b_wins
    else:
        print("Next move var invalid")
    return a_wins, b_wins


if __name__ == "__main__":
    p1_start, p2_start = load_input()
    a_wins, b_wins = play(p1_start, p2_start)
    winner = max({"A": a_wins, "B": b_wins}.items(), key=lambda item: item[1])[0]
    print(f"A wins {a_wins}, B wins {b_wins}, {winner} wins the most")
    print(f"Answer is {max(a_wins, b_wins)}")
