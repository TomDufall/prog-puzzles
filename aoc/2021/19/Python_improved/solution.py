from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from functools import wraps
from itertools import combinations, product
from typing import Callable, Optional

ALL_ROTATIONS = {(x, y, 0) for x, y in product(range(4), range(4))}.union(
    (x, 0, z) for x, z in product(range(4), {1, 2})
)


Point3D = tuple[int, int, int]


def point_rotate(point: Point3D, x_rot: int, y_rot: int, z_rot: int) -> Point3D:
    x, y, z = point
    if x_rot == 1:
        x, y, z = x, -1 * z, y
    elif x_rot == 2:
        x, y, z = x, -1 * y, -1 * z
    elif x_rot == 3:
        x, y, z = x, z, -1 * y

    if y_rot == 1:
        x, y, z = z, y, -1 * x
    elif y_rot == 2:
        x, y, z = -1 * x, y, -1 * z
    elif y_rot == 3:
        x, y, z = -1 * z, y, x

    if z_rot == 1:
        x, y, z = y, -1 * x, z
    elif z_rot == 2:
        x, y, z = -1 * y, x, z
    return x, y, z


def calc_point_translation(a: Point3D, b: Point3D) -> Point3D:
    """
    Return a point representing the translation from other to self.
    """
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def point_translate(point: Point3D, translation: Point3D) -> Point3D:
    return (
        point[0] + translation[0],
        point[1] + translation[1],
        point[2] + translation[2],
    )


def point_transform(
    point: Point3D, rotation: tuple[int, int, int], translation: Point3D
) -> Point3D:
    return point_translate(point_rotate(point, *rotation), translation)


def manhattan_distance(a: Point3D, b: Point3D) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


Translation = Point3D
Transformation = tuple[tuple[int, int, int], Translation]


def _try_match_scanner_pair_no_rotation(
    group_one: set[Point3D], group_two: set[Point3D], min_overlap: int = 12
) -> Optional[Translation]:
    """
    Try and match a scanner pair using only translations.
    Return the translation from two to one if successful, else None.
    """
    get_translation = lambda pair: calc_point_translation(pair[0], pair[1])
    for translation in map(get_translation, product(group_one, group_two)):
        matched = 0
        group_two_count = len(group_two)
        for i, point in enumerate(group_two):
            if point_translate(point, translation) in group_one:
                matched += 1
            elif matched + group_two_count - (i + 1) < 12:
                break
            if matched >= min_overlap:
                return translation
    return None


def _try_match_scanner_pair(
    a: set[Point3D], b: set[Point3D], min_overlap: int = 12
) -> Optional[Transformation]:
    for rotation in ALL_ROTATIONS:
        b_rotated = {point_rotate(point, *rotation) for point in b}
        if translation := _try_match_scanner_pair_no_rotation(
            a, b_rotated, min_overlap
        ):
            return rotation, translation
    return None


def _find_overlapping_pair(
    scanners_a: dict[int, set[Point3D]],
    scanners_b: dict[int, set[Point3D]],
    exclude_list: Optional[set[int, int]] = None,
    min_overlap: int = 12,
) -> Optional[tuple[int, int, Transformation, set[int, int]]]:
    """
    Given two lists of scanners, find an overlapping pair and return a tuple of
    (index 1, index 2, transformation from 2 to 1)
    """
    if not exclude_list:
        exclude_list = set()
    for (ia, a), (ib, b) in product(scanners_a.items(), scanners_b.items()):
        if (ia, ib) in exclude_list or (ib, ia) in exclude_list:
            continue
        transformation = _try_match_scanner_pair(a, b)
        if transformation:
            return ia, ib, transformation, exclude_list
        exclude_list.add((ia, ib))
    return None


def timeit(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        response = func(*args, **kwargs)
        end = datetime.now()
        print(
            f"Function {func.__name__} executed in {(end - start).total_seconds()} seconds"
        )
        return response

    return wrapper


@timeit
def merge_scanners_lazy(
    scanners: list[set[Point3D]],
) -> tuple[set[Point3D], dict[int, Point3D]]:
    unmerged_scanners = dict(enumerate(scanners))
    merged_scanners: dict[int, set[Point3D]] = {}
    merged_scanners[0] = unmerged_scanners.pop(0)
    merged_points = merged_scanners[0]
    scanner_locations: dict[int, Point3D] = {0: (0, 0, 0)}
    exclude_list = set()
    while unmerged_scanners:
        last_length = len(unmerged_scanners)
        print(f"{last_length} scanners left to include")
        a, b, transformation, exclude_list = _find_overlapping_pair(
            merged_scanners, unmerged_scanners, exclude_list
        )
        b_points = {
            point_transform(point, *transformation) for point in unmerged_scanners[b]
        }
        scanner_location = point_transform((0, 0, 0), *transformation)
        merged_points = merged_points.union(b_points)
        scanner_locations[b] = scanner_location
        merged_scanners[b] = b_points
        unmerged_scanners.pop(b)

        if len(unmerged_scanners) == last_length:
            raise ValueError("failed to progress")

    return merged_points, scanner_locations


def find_max_scanner_distance(scanner_locations: dict[int, Point3D]) -> int:
    max_distance = 0
    for a, b in combinations(scanner_locations.values(), 2):
        max_distance = max(max_distance, manhattan_distance(a, b))
    return max_distance


def load_input(filepath: str = "input.txt") -> list[set[Point3D]]:
    with open(filepath) as f:
        text = f.read()
    blocks = text.split("\n\n")
    scanners: list[set[Point3D]] = []
    for block in blocks:
        lines = block.splitlines()
        line_to_point = lambda s: tuple(map(int, s.split(",")))
        scanners.append({line_to_point(line) for line in lines[1:]})
    return scanners


if __name__ == "__main__":
    scanners = load_input()
    # scanners = load_input("sample_input.txt")
    merged, scanner_locations = merge_scanners_lazy(scanners)
    max_scanner_distance = find_max_scanner_distance(scanner_locations)
    print(len(merged))
    print(max_scanner_distance)
