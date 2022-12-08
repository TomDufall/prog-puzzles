from typing import Iterable

def load_input(filepath: str = "input.txt") -> list[list[int]]:
    with open(filepath) as f:
        text_lines = f.read().splitlines()
    process_lines = lambda l: list(map(int, l))
    return list(map(process_lines, text_lines))

def get_visible_trees_1d(row: Iterable[int]) -> set[int]:
    max_height = -1
    visible = set()
    for i, height in enumerate(row):
        if height > max_height:
            visible.add(i)
            max_height = height
    return visible

def get_visible_trees(trees):
    visible = set()
    for i, row in enumerate(trees):
        row_len = len(row)
        visible = visible.union({(x, i) for x in get_visible_trees_1d(row)})
        visible = visible.union({(row_len -1 -x, i) for x in get_visible_trees_1d(reversed(row))})
    for i in range(len(trees[0])):
        column = [row[i] for row in trees]
        col_len = len(column)
        visible = visible.union({(i, y) for y in get_visible_trees_1d(column)})
        visible = visible.union({(i, col_len -1 - y) for y in get_visible_trees_1d(reversed(column))})
    return visible

if __name__ == "__main__":
    trees = load_input()
    visible = get_visible_trees(trees)
    print(f"Day 8 part 1: {len(visible)}")
