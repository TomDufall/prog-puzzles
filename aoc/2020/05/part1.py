from math import ceil, floor, pow
from typing import Tuple, List


def decode_pass(pass_: str, row_len: int = 7) -> Tuple[int, int]:
    row_range: List[int] = [0, int(pow(2, row_len)) - 1]
    col_range: List[int] = [0, int(pow(2, (len(pass_)) - row_len)) - 1]
    for char in pass_[:row_len]:
        midpoint = row_range[0] + (row_range[1] - row_range[0]) / 2
        if char == "F":
            row_range[1] = floor(midpoint)
        elif char == "B":
            row_range[0] = ceil(midpoint)
        else:
            raise ValueError("Unrecognised character")
    for char in pass_[row_len:]:
        midpoint = col_range[0] + (col_range[1] - col_range[0]) / 2
        if char == "L":
            col_range[1] = floor(midpoint)
        elif char == "R":
            col_range[0] = ceil(midpoint)
        else:
            raise ValueError("Unrecognised character")
    if row_range[0] != row_range[1] or col_range[0] != col_range[1]:
        raise Exception("Something went wrong - seat not agreed")
    return (row_range[0], col_range[0])


def calc_seat_id(pass_: Tuple[int, int]) -> int:
    return pass_[0] * 8 + pass_[1]


if __name__ == "__main__":
    with open("input.txt") as f:
        passes = f.read().splitlines()
    seat_ids = map(
        calc_seat_id,
        map(
            decode_pass,
            passes
        )
    )
    print(max(seat_ids))
