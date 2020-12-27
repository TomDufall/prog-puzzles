from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import List

from toolz import concat, frequencies
from toolz.dicttoolz import merge_with, valmap


@dataclass
class Tile:
    id: str
    data: List[str]

    @property
    def edges(self) -> List[str]:
        top = self.data[0]
        bot = self.data[-1]
        left = "".join([row[0] for row in self.data])
        right = "".join([row[-1] for row in self.data])
        return [top, bot, left, right]


@dataclass
class TileStore:
    tiles: List[Tile]

    @staticmethod
    def from_file(filepath: Path) -> TileStore:
        return TileStore(
            [Tile(title[5:], data.splitlines()) for title, data in 
            map(lambda x: x.split(":\n", 1), filepath.read_text().split("\n\n"))]
        )

    def find_corners(self) -> List[int]:
        edges = {}
        edges_dict_list = [
            {min(edge, edge[::-1]): tile.id for edge in tile.edges}
            for tile in self.tiles
        ]
        edges = merge_with(lambda x: x, *edges_dict_list)
        freqs = frequencies(concat(
            (value for value in edges.values() if len(value) == 2))
        )
        corners = [id for id, count in freqs.items() if count == 2]
        if len(corners) != 4:
            raise ValueError("Wrong number of corners!")
        return corners


if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    filepath = Path(__file__).parent / "input.txt"
    tiles = TileStore.from_file(filepath)
    corners = tiles.find_corners()
    answer = int(corners[0]) * int(corners[1]) * int(corners[2]) * int(corners[3])
    end = datetime.now()
    time = (end - start).total_seconds()
    print(time)
    print(corners)
    print(answer)
