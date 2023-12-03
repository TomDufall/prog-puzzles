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


def check_valid_parts(
    grid: list[str], parts: list[tuple[int, list[tuple[int, int]]]]
) -> list[int]:
    get_cell = safe_grid(grid, ".")
    ignore = "0123456789."
    valid_parts = []
    for number, coords in parts:
        valid = False
        first = True
        for row, col in coords:
            if first:
                if (
                    get_cell(row - 1, col - 1) not in ignore
                    or get_cell(row - 1, col) not in ignore
                    or get_cell(row, col - 1) not in ignore
                    or get_cell(row + 1, col - 1) not in ignore
                    or get_cell(row + 1, col) not in ignore
                ):
                    valid = True
                    break
                first = False
            if (
                get_cell(row - 1, col + 1) not in ignore
                or get_cell(row, col + 1) not in ignore
                or get_cell(row + 1, col + 1) not in ignore
            ):
                valid = True
                break
        if valid:
            valid_parts.append(number)
    return valid_parts


def generate_answer(filename: "input.txt"):
    _input = load_input(filename)
    numbers = find_numbers(_input)
    valid_parts = check_valid_parts(_input, numbers)
    return sum(valid_parts)


if __name__ == "__main__":
    print(generate_answer("input.txt"))
