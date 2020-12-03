from itertools import combinations
from functools import reduce
import operator

with open("input.txt") as f:
    nums = [float(l.strip()) for l in f.readlines()]
for comb in combinations(nums, 3):
    if sum(comb) == 2020:
        print(reduce(operator.mul, comb, 1))
