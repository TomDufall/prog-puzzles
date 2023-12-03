from typing import Union


def load_input(filename: str = "input.txt") -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()


def find_numbers(rows: list[str]) -> list[tuple[int, list[tuple[int, int]]]]:
    digits = "0123456789"
    result = []
    for row_id, row in enumerate(rows):
        number = ""
        number_cells = []
        i = 0
        while i < len(row):
            if (char := row[i]) in digits:
                # New or extended number
                number += char
                number_cells.append((row_id, i))
            elif number:
                # Number ended
                result.append((int(number), number_cells))
                number = ""
                number_cells = []
            i += 1
        if number:
            result.append((int(number), number_cells))
    return result


def safe_grid(grid: list[str], default: Union[str, None]):
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1

    def safe_index(row: int, col: int) -> Union[str, None]:
        if row < 0 or col < 0 or row > max_row or col > max_col:
            return default
        else:
            return grid[row][col]

    return safe_index


def find_gears(grid: list[str]) -> list[tuple[int, int]]:
    gears = []
    for row_id, row in enumerate(grid):
        for col_id, val in enumerate(row):
            if val == "*":
                gears.append((row_id, col_id))
    return gears


def calculate_gear_ratios(
    gears: list[tuple[int, int]], numbers: list[tuple[int, list[tuple[int, int]]]]
):
    ratios = []
    # Check gears against numbers
    for gear_row, gear_col in gears:
        num_1: Union[int, None] = None
        num_2: Union[int, None] = None
        neighbours = {
            (gear_row - 1, gear_col - 1),
            (gear_row - 1, gear_col),
            (gear_row - 1, gear_col + 1),
            (gear_row, gear_col - 1),
            (gear_row, gear_col + 1),
            (gear_row + 1, gear_col - 1),
            (gear_row + 1, gear_col),
            (gear_row + 1, gear_col + 1),
        }
        for number, coords in numbers:
            if neighbours.intersection(set(coords)):
                if not num_1:
                    num_1 = number
                else:
                    num_2 = number
                    break
        if num_1 and num_2:
            ratios.append(num_1 * num_2)
    return ratios


def generate_answer(filename: "input.txt"):
    grid = load_input(filename)
    numbers = find_numbers(grid)
    gears = find_gears(grid)
    ratios = calculate_gear_ratios(gears, numbers)
    answer = sum(ratios)
    return answer


if __name__ == "__main__":
    print(generate_answer("input.txt"))
