from typing import Tuple, List

from part1 import calc_seat_id, decode_pass


def make_blocks(nums: List[int]) -> Tuple[int, int]:
    # return gap
    nums = sorted(nums)
    last = nums[0]
    for num in nums[1:]:
        if num == last + 1:
            last = num
        else:
            return (last, num)
    raise Exception("No gap found")


if __name__ == "__main__":
    with open("input.txt") as f:
        passes = f.read().splitlines()
        # print(passes)
    seat_ids = list(map(
        calc_seat_id,
        map(
            decode_pass,
            passes
        )
    ))
    print(max(seat_ids))
    print(make_blocks(seat_ids))
