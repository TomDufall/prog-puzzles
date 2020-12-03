from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple


@dataclass
class TobogganMap:
    map_: List[str]

    def traverse(
            self, vector: Tuple[int, int],
            start: Tuple[int, int] = (0, 0),
    ) -> int:
        x, y = start
        collisions = 0
        # continue until off the bottom of the map
        while y < len(self.map_):
            if self.map_[y][x] != ".":
                collisions += 1
            x = (x + vector[0]) % len(self.map_[0])
            y += vector[1]
        return collisions


def load_input(filepath: Path) -> List[str]:
    return [line.strip() for line in filepath.read_text().splitlines()]


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    map_ = TobogganMap(load_input(filepath))
    print(map_.traverse((3, 1)))
