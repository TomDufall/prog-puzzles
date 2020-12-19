from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from operator import add, mul
from pathlib import Path
from typing import Callable, List, Union


def find_end_bracket(expr: str, i: int):
    layers = 1
    for j, token in enumerate(expr):
        if token == "(":
            layers += 1
        elif token == ")":
            layers -= 1
            if layers == 0:
                return i + j + 1


def parse_expr(expr: List[Union[int, str]]) -> int:
    while "(" in expr:
        start = expr.index("(")
        end = find_end_bracket(expr[start + 1:], start)
        expr = expr[:start] + [parse_expr(expr[start+1:end])] + expr[end+1:]
    while "+" in expr:
        i = expr.index("+")
        expr = expr[:i-1] + [expr[i-1]+expr[i+1]] + expr[i+2:]
    while "*" in expr:
        i = expr.index("*")
        expr = expr[:i-1] + [expr[i-1]*expr[i+1]] + expr[i+2:]
    return expr[0]


def split_str(expr: str) -> List[Union[int, str]]:
    split_str = deque(expr.split(" "))
    split_expr = deque([])
    while len(split_str) > 0:
        group = split_str.popleft()
        if group == "(":
            split_expr.append("(")
            continue
        if group.startswith("("):
            split_expr.append("(")
            split_str.appendleft(group[1:])
            continue
        if group == ")":
            split_expr.append(")")
            continue
        if group.endswith(")"):
            split_str.appendleft(")")
            split_str.appendleft(group[:-1])
            continue
        else:
            try:
                split_expr.append(int(group))
            except ValueError:
                split_expr.append(group)
    return list(split_expr)


if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    filepath = Path(__file__).parent / "input.txt"
    acc = 0
    for line in filepath.read_text().splitlines():
        acc += parse_expr(split_str(line))
    end = datetime.now()
    print(acc)
    print((end - start).total_seconds())
