from collections import deque
from operator import add, mul
from pathlib import Path
from typing import List


def is_int(chars: str) -> bool:
    try:
        int(chars)
        return True
    except ValueError:
        return False


def eval_recursive(expr) -> int:
    #print(expr)
    acc = 0
    operator = None
    while len(expr) > 0:
        token = expr.popleft()
        if is_int(token):
            if not operator:
                acc = int(token)
            else:
                acc = operator(acc, int(token))
                operator = None
        elif token == "+":
            operator = add
        elif token == "*":
            operator = mul
        elif token == "(":
            #print("recursing")
            expr.appendleft(eval_recursive(expr))
        elif token == ")":
            break
        else:
            raise ValueError(f"Unrecognised operator: {token}")
        #print(acc, operator, expr)
    return acc


def eval(expr: str) -> int:
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
            split_expr.append(group)
    return eval_recursive(split_expr)


if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    filepath = Path(__file__).parent / "input.txt"
    acc = 0
    for line in filepath.read_text().splitlines():
        acc += eval(line)
    end = datetime.now()
    print(acc)
    print((end - start).total_seconds())
    