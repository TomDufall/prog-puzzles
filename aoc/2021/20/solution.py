from __future__ import annotations

from itertools import count, product


def get_neighbours(
    point: tuple[int, int], grid: list[list[str]], background: str
) -> list[list[str]]:
    xi, yi = point
    xlen, ylen = len(grid[0]), len(grid)
    output = [["" for _ in range(3)] for _ in range(3)]
    for xdiff, ydiff in product([-1, 0, 1], [-1, 0, 1]):
        xi2, yi2 = xi + xdiff, yi + ydiff
        if xi2 < 0 or yi2 < 0 or xi2 >= xlen or yi2 >= ylen:
            pixel = background
        else:
            pixel = grid[yi2][xi2]
        output[ydiff + 1][xdiff + 1] = pixel
    return output


def grid_to_int(grid: list[list[str]]) -> int:
    n_chars: list[str] = []
    for row in grid:
        for char in row:
            if char == ".":
                i = "0"
            else:
                i = "1"
            n_chars.append(i)
    return int("".join(n_chars), 2)


def apply_algorithm_point(
    algorithm: str, image: list[list[str]], point: tuple[int, int], background: str
) -> str:
    neighbours = get_neighbours(point, image, background)
    new_char_index = grid_to_int(neighbours)
    new_char = algorithm[new_char_index]
    return new_char


def apply_algorithm(
    algorithm: str, image: list[list[str]], background: str
) -> tuple[list[list[str]], str]:
    xlen, ylen = len(image[0]), len(image)
    new_image = []
    for yi in range(
        -1, ylen + 1
    ):  # Pixels off-image still have neighbours in the image
        new_row = []
        for xi in range(-1, xlen + 1):
            new_row.append(
                apply_algorithm_point(algorithm, image, (xi, yi), background)
            )
        new_image.append(new_row)
    new_background = apply_algorithm_point(algorithm, image, (-2, -2), background)
    return new_image, new_background


def apply_algorithm_n(
    algorithm: str, image: list[list[str]], n: int, show_progress: bool = False
) -> list[list[str]]:
    background = "."
    for i in range(n):
        image, background = apply_algorithm(algorithm, image, background)
        if show_progress:
            print(f"{i}/{n} rounds of processing complete")
    return image


def count_lit_pixels(image: list[list[str]]) -> int:
    count = 0
    for row in image:
        count += sum([0 if pixel == "." else 1 for pixel in row])
    return count


def load_input(filepath: str = "input.txt") -> tuple[str, list[list[str]]]:
    with open(filepath) as f:
        algorithm_lines, image_raw = f.read().split("\n\n")
    algorithm = "".join(algorithm_lines.splitlines())
    image = [list(line) for line in image_raw.splitlines()]
    return algorithm, image


if __name__ == "__main__":
    algorithm, image = load_input()

    end_image_1 = apply_algorithm_n(algorithm, image, 2)
    lit_pixels_1 = count_lit_pixels(end_image_1)
    print(f"Part 1 answer: {lit_pixels_1}")

    from datetime import datetime

    start = datetime.now()
    end_image_2 = apply_algorithm_n(algorithm, image, 50, show_progress=True)
    lit_pixels_2 = count_lit_pixels(end_image_2)
    end = datetime.now()
    print(f"Part 2 answer: {lit_pixels_2}")
    print(f"{(end - start).total_seconds()}s part 2 run time")
