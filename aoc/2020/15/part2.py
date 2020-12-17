from typing import List


def play_to_n(nums: List[int], target: int) -> int:
    last_played_dict = {}
    turn = 0
    start = True
    for num in nums:
        turn += 1
        answer = num
        if not start:
            last_played_dict[last] = turn - 1
        else:
            start = False
        last = answer

    for i in range(turn, target):
        last_played_dict[last] = i
        last = i - last_played_dict.get(last, i)
    return last


if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    answer = play_to_n([6,3,15,13,1,0], 30000000)
    end = datetime.now()
    time = (end - start).total_seconds()
    print(f"Answer: {answer}, time: {time}")

# current approx time 18.8s for 3000000