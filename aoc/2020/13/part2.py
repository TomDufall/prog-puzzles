from datetime import datetime
from functools import reduce
from math import gcd
from operator import mul
from pathlib import Path
from typing import Iterable, Set, Tuple, List

def lcm(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    def lcm_pair(x: int, y: int) -> int:
        return x * y // gcd(x, y)
    return reduce(lcm_pair, nums)

def test_time(start: int, ids: List[int]) -> bool:
    time = start
    for id in ids:
        if id:
            if time % id != 0:
                return False
        time += 1
    return True

def find_mod_result(repeater: int, mod: int, start: int, target: int) -> int:
    target = target % mod
    results = set()
    count = 0
    acc = start
    while True:
        if acc == target:
            return count
        if acc in results:
            return None
        results.add(acc)
        count += 1
        acc = (acc + repeater) % mod

def find_solution(ids: List[int], limit: int = 10000000000000000) -> int:
    time = ids[0]
    solved = [ids[0]]
    for i in range(1, len(ids)):
        next_val = ids[i]
        if (time + i) % next_val == 0:
            solved.append(next_val)
            continue
        current_diff = time + i % next_val
        multiplier = find_mod_result(
            repeater=lcm(solved),
            mod=next_val,
            start=current_diff,
            target=0
        )
        time += multiplier * lcm(solved)
        solved.append(next_val)
    return time

def find_solution_simple(ids: List[int], limit: int = 10000000000000000) -> int:
    time = ids[0]
    solved = [ids[0]]
    for i in range(1, len(ids)):
        val = ids[i]
        step = lcm(solved)
        while time <= limit and (time + i) % val != 0:
            time += step
        if time > limit:
            raise Exception("Reached limit")
        solved.append(val)
    return time

def load_list(ids: List[str]) -> List[int]:
    return [int(id) if id.isdigit() else 1 for id in ids]

def load_input(filepath: Path) -> Tuple[int, List[str]]:
    with filepath.open() as f:
        target = int(f.readline())
        buses = load_list(f.readline().rstrip("\n").split(","))
    return (target, buses)

if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    target, buses = load_input(filepath)
    start = datetime.now()
    solution = find_solution_simple(buses)
    end = datetime.now()
    print(f"solution: {solution} in time: {(end - start).total_seconds()}s")
