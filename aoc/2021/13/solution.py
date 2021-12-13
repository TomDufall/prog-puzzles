from __future__ import annotations


def fold(
    coords: set[tuple[int, int]], folds: list[tuple[str, int]]
) -> set[tuple[int, int]]:
    for axis, value in folds:
        new_coords: set[tuple[int, int]] = set()
        for x, y in coords:
            if axis == "x":
                if x > value:
                    x = value - (x - value)
            elif axis == "y":
                if y > value:
                    y = value - (y - value)
            new_coords.add((x, y))
        coords = new_coords
    return coords


def print_coords(coords: set[tuple[int, int]]) -> None:
    _, max_y = max(coords, key=lambda item: item[1])
    max_x, _ = max(coords, key=lambda item: item[0])
    rows = []
    for y in range(max_y + 1):
        x_values = {x2 for x2, y2 in coords if y2 == y}
        row = "".join(["▮" if i in x_values else " " for i in range(max_x + 1)])
        rows.append(row)
    print("\n".join(rows))


def load_input(
    filepath: str = "input.txt",
) -> tuple[set[tuple[int, int]], list[tuple[str, int]]]:
    """
    Load input file.
    Return coords, folds, where coords is a list of x, y coords (right, down)
    and folds is a list of (axis, coord), e.g. x, 3 means fold along x=3.
    """
    with open(filepath) as f:
        text = f.read()
    coords_str, folds_str = text.split("\n\n")
    coords = {tuple(map(int, line.split(",", 1))) for line in coords_str.splitlines()}

    folds: tuple[str, int] = []
    for line in folds_str.splitlines():
        instr = line.split(" ")[-1]
        axis, num = instr.split("=")
        folds.append((axis, int(num)))

    return coords, folds


if __name__ == "__main__":
    coords, folds = load_input()
    one_step = fold(coords, [folds[0]])
    print(f"After 1 step, {len(one_step)} points remain")

    folded = fold(coords, folds)
    print_coords(folded)
