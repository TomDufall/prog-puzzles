from itertools import islice
from typing import Iterator, List


# https://docs.python.org/3/library/itertools.html#itertools-recipes
def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)


def play(nums: List[int]) -> Iterator:
    last_played_dict = {}
    turn = 0
    start = True
    for num in nums:
        turn += 1
        answer = num
        yield num
        if not start:
            last_played_dict[last] = turn - 1
        else:
            start = False
        last = answer

    while True:
        turn += 1
        last_played_turn = last_played_dict.get(last)
        if last_played_turn is None:
            answer = 0
        else:
            answer = turn - last_played_turn - 1
        last_played_dict[last] = turn - 1
        last = answer
        yield answer


def nth_play(nums: List[int], n: int) -> int:
    """
    Return the (1-indexed) nth play from the game started with nums.
    """
    plays = play(nums)
    return nth(plays, n - 1)


if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    plays = play([6,3,15,13,1,0])
    print(nth(plays, 2020 - 1))
    end = datetime.now()
    print((end - start).total_seconds())
