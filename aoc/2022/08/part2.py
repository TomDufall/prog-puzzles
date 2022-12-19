from typing import Iterable

from part1 import load_input

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


def get_scenic_score(trees, coord):
    score = 1
    x, y = coord
    start_height = trees[y][x]
    row = trees[y]
    directional_score = 0
    for x2 in range(x - 1, -1, -1):
        if x2< 0:
            break
        directional_score += 1
        if trees[y][x2] >= start_height:
            break
    score *= directional_score
    directional_score = 0
    for x2 in range(x + 1, len(row)):
        if x2 >= len(row):
            break
        directional_score += 1
        if trees[y][x2] >= start_height:
            break
    score *= directional_score    
    col = [trees[y2][x] for y2 in range(len(trees))]
    directional_score = 0
    for y2 in range(y - 1, -1, -1):
        if y2 < 0:
            break
        directional_score += 1
        if trees[y2][x] >= start_height:
            break
    score *= directional_score
    directional_score = 0
    for y2 in range(y + 1, len(col)):
        if y2 >= len(col):
            break
        directional_score += 1
        if trees[y2][x] >= start_height:
            break
    score *= directional_score
    return score

def get_scenic_scores(trees):
    scores = []
    for y, row in enumerate(trees):
        scores.append([])
        for x, col in enumerate(row):
            scores[-1].append(get_scenic_score(trees, (x, y)))
    return scores


if __name__ == "__main__":
    trees = load_input("input.txt")
    scores = get_scenic_scores(trees)
    answer = max(map(max, scores))
    print(f"Day 8 part 2: {answer}")
