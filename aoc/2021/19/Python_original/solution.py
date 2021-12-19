from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from functools import wraps
from itertools import combinations, product
from typing import Callable, Optional

ALL_ROTATIONS = {(x, y, 0) for x, y in product(range(4), range(4))}.union(
    (x, 0, z) for x, z in product(range(4), {1, 2})
)


@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int

    def rotate(self, x_rot: int, y_rot: int, z_rot: int) -> Point3D:
        x, y, z = self.x, self.y, self.z
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
        return Point3D(x, y, z)

    def calc_translation(self, other: Point3D) -> Point3D:
        """
        Return a point representing the translation from other to self.
        """
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def translate(self, translation: Point3D) -> Point3D:
        return Point3D(
            self.x + translation.x, self.y + translation.y, self.z + translation.z
        )

    def transform(
        self, rotation: tuple[int, int, int], translation: Point3D
    ) -> Point3D:
        point = self.rotate(*rotation)
        point = point.translate(translation)
        return point

    def manhattan_distance(self, other: Point3D) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)


Translation = Point3D
Transformation = tuple[tuple[int, int, int], Translation]


def _try_match_scanner_pair_no_rotation(
    group_one: set[Point3D], group_two: set[Point3D], min_overlap: int = 12
) -> Optional[Translation]:
    """
    Try and match a scanner pair using only translations.
    Return the translation from two to one if successful, else None.
    """
    for a, b in product(group_one, group_two):
        # Attempt alignment
        translation = a.calc_translation(b)
        translated_two = {point.translate(translation) for point in group_two}
        if len(group_one.intersection(translated_two)) >= min_overlap:
            # Match if enough shared points
            return translation
    return None


def _try_match_scanner_pair(
    a: set[Point3D], b: set[Point3D], min_overlap: int = 12
) -> Optional[Transformation]:
    for rotation in ALL_ROTATIONS:
        b_rotated = {point.rotate(*rotation) for point in b}
        translation = _try_match_scanner_pair_no_rotation(a, b_rotated, min_overlap)
        if translation:
            return rotation, translation
    return None


def _find_overlapping_pairs(
    scanners: list[set[Point3D]], min_overlap: int = 12
) -> list[tuple[int, int, Transformation]]:
    """
    Given a list of scanners, find overlapping pairs and return a tuple of
    (index 1, index 2, transformation from 2 to 1)
    """
    pairs = []
    for (ia, a), (ib, b) in combinations(enumerate(scanners), 2):
        transformation = _try_match_scanner_pair(a, b)
        if transformation:
            pairs.append((ia, ib, transformation))
            print(f"Found {len(pairs)} pairs")
    return pairs


def merge_pairs(
    scanners: list[set[Point3D]],
    merge_list: list[tuple[int, int, Transformation]],
) -> tuple[set[Point3D], dict[int, Point3D]]:
    merge_list = merge_list.copy()
    merged = scanners[0]
    # Map indexes to the point before them and the transformation used to merge them
    merged_indexes: dict[int, tuple[Optional[int], Transformation]] = {
        0: (None, ((0, 0, 0), Point3D(0, 0, 0)))
    }
    scanner_locations: dict[int, Point3D] = {0: Point3D(0, 0, 0)}
    while merge_list:
        last_length = len(merge_list)
        for a, b, transformation in merge_list:
            scanner_location = Point3D(0, 0, 0)
            if a in merged_indexes and b in merged_indexes:
                merge_list.remove((a, b, transformation))
            elif a in merged_indexes:
                b_points = scanners[b]
                b_points = {point.transform(*transformation) for point in b_points}
                scanner_location = scanner_location.transform(*transformation)
                # Apply transformations from previous scanners to base scanner
                prev: Optional[int] = a
                while prev in merged_indexes:
                    prev, trans2 = merged_indexes[prev]
                    b_points = {point.transform(*trans2) for point in b_points}
                    scanner_location = scanner_location.transform(*trans2)
                merged = merged.union(b_points)
                scanner_locations[b] = scanner_location
                merged_indexes[b] = (a, transformation)
                merge_list.remove((a, b, transformation))
            elif b in merged_indexes:
                # Tidy
                a, b = b, a
                b_points = scanners[b]
                # Should inverse but really cba at this point
                inverse_transformation = _try_match_scanner_pair(
                    scanners[a], scanners[b]
                )
                if not inverse_transformation:
                    raise ValueError("Inverse transformation not found")
                b_points = {
                    point.transform(*inverse_transformation) for point in b_points
                }
                scanner_location = scanner_location.transform(*inverse_transformation)
                # Apply transformations from previous scanners to base scanner
                prev = a
                while prev in merged_indexes:
                    prev, trans2 = merged_indexes[prev]
                    b_points = {point.transform(*trans2) for point in b_points}
                    scanner_location = scanner_location.transform(*trans2)
                merged = merged.union(b_points)
                scanner_locations[b] = scanner_location
                merged_indexes[b] = (a, inverse_transformation)
                merge_list.remove((b, a, transformation))
        if len(merge_list) == last_length:
            raise ValueError("failed to progress")

    return merged, scanner_locations


def timeit(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        response = func(*args, **kwargs)
        end = datetime.now()
        print(f"Func executed in {(end - start).total_seconds()} seconds")
        return response

    return wrapper


@timeit
def merge_scanners(
    scanners: list[set[Point3D]], min_overlap: int = 12
) -> tuple[set[Point3D], dict[int, Point3D]]:
    # Find pairs
    pairs = _find_overlapping_pairs(scanners)
    print(f"Found {len(pairs)} pairs in total")
    scanners_in_pairs = set()
    for a, b, _ in pairs:
        scanners_in_pairs.add(a)
        scanners_in_pairs.add(b)
    if scanners_in_pairs != set(range(len(scanners))):
        raise ValueError("Not all scanners paired")
    merged, scanner_locations = merge_pairs(scanners, pairs)
    return merged, scanner_locations


def find_max_scanner_distance(scanner_locations: dict[int, Point3D]) -> int:
    max_distance = 0
    for a, b in combinations(scanner_locations.values(), 2):
        max_distance = max(max_distance, a.manhattan_distance(b))
    return max_distance


def load_input(filepath: str = "input.txt") -> list[set[Point3D]]:
    with open(filepath) as f:
        text = f.read()
    blocks = text.split("\n\n")
    scanners: list[set[Point3D]] = []
    for block in blocks:
        lines = block.splitlines()
        line_to_point = lambda s: Point3D(*map(int, s.split(",")))
        scanners.append({line_to_point(line) for line in lines[1:]})
    return scanners


if __name__ == "__main__":
    scanners = load_input()
    merged, scanner_locations = merge_scanners(scanners)
    max_scanner_distance = find_max_scanner_distance(scanner_locations)
    print(len(merged))
    print(max_scanner_distance)
