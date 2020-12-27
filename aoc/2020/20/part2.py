from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from math import sqrt
from pathlib import Path
from typing import Dict, List

from toolz import concat, frequencies
from toolz.dicttoolz import merge_with, valmap


@dataclass
class Tile:
    id: str
    data: List[str]

    @property
    def edges(self) -> List[str]:
        # all listed reading clockwise
        top = self.data[0]
        bot = self.data[-1][::-1]
        left = "".join([row[0] for row in self.data])[::-1]
        right = "".join([row[-1] for row in self.data])
        return [top, right, bot, left]

    def flip(self, x: bool=False, y: bool=False) -> None:
        if x:
            self.data = list(map(lambda x: x[::-1], self.data))
        if y:
            self.data.reverse()

    def rotate(self, count: int) -> None:
        rotations = count % 4
        for _ in range(rotations):
            self.data = [
                "".join([self.data[i][j] for i in range(len(self.data) -1, -1, -1)])
                for j in range(len(self.data))
            ]

    def get_edge_location(self, edge_str: str) -> (int, int):
        edges = self.edges
        try:
            return edges.index(edge_str), 0
        except ValueError:
            edge_reversed = edge_str[::-1]
            return edges.index(edge_reversed), -1


@dataclass
class TileStore:
    tiles: Dict[Tile]

    @staticmethod
    def from_file(filepath: Path) -> TileStore:
        return TileStore(
            {title[5:]: Tile(title[5:], data.splitlines()) for title, data in 
            map(lambda x: x.split(":\n", 1), filepath.read_text().split("\n\n"))}
        )

    def find_corners(self) -> List[int]:
        edges_dict_list = [
            {min(edge, edge[::-1]): tile.id for edge in tile.edges}
            for tile in self.tiles.values()
        ]
        edges = merge_with(lambda x: x, *edges_dict_list)
        freqs = frequencies(concat(
            (value for value in edges.values() if len(value) == 2))
        )
        corners = [id for id, count in freqs.items() if count == 2]
        if len(corners) != 4:
            raise ValueError("Wrong number of corners!")
        return corners

    def build_image(self) -> List[str]:
        edges_dict_list = [
            {min(edge, edge[::-1]): tile.id for edge in tile.edges}
            for tile in self.tiles.values()
        ]
        edges = merge_with(lambda x: x, *edges_dict_list)
        # id: (x, y)
        first_tile = next(iter(self.tiles.values()))
        to_find = set(first_tile.edges)
        positioned_tiles = {first_tile.id: (0, 0)}
        while to_find:
            next_edge = to_find.pop()
            next_edge = min(next_edge, next_edge[::-1])
            ids = set(edges[next_edge])
            new_id = ids.difference(positioned_tiles.keys())
            if not new_id:
                continue
            elif len(new_id) != 1:
                raise ValueError("Unexpected length")
            else:
                new_id = next(iter(new_id))
                existing_id = next(iter(ids.intersection(positioned_tiles.keys())))
                existing_edge_index, _ = self.tiles[existing_id].get_edge_location(next_edge)
                existing_edge = self.tiles[existing_id].edges[existing_edge_index]
                #print(existing_edge)
                #print(existing_edge_index)
                new_edge_index, new_edge_flip = self.tiles[new_id].get_edge_location(next_edge)
                #print(new_edge_index, new_edge_flip)
                rotation = existing_edge_index - new_edge_index + 2
                self.tiles[new_id].rotate(rotation)
                if existing_edge in self.tiles[new_id].edges:
                    # need to flip
                    if existing_edge_index in {0, 2}:
                        # flip x values
                        self.tiles[new_id].flip(x=True)
                    else:
                        self.tiles[new_id].flip(y=True)
                existing_x, existing_y = positioned_tiles[existing_id]
                if existing_edge_index == 0:
                    new_x, new_y = existing_x, existing_y + 1
                elif existing_edge_index == 1:
                    new_x, new_y = existing_x + 1, existing_y
                elif existing_edge_index == 2:
                    new_x, new_y = existing_x, existing_y - 1
                elif existing_edge_index == 3:
                    new_x, new_y = existing_x - 1, existing_y
                else:
                    raise ValueError("Index out of bounds")
                positioned_tiles[new_id] = new_x, new_y
                to_find.update(self.tiles[new_id].edges)
                #print("--------------------")
        top_left_x = min((x for x, y in positioned_tiles.values()))
        top_left_y = max((y for x, y in positioned_tiles.values()))
        size = int(sqrt(len(positioned_tiles)))
        tiles = [[None for _ in range(size)] for _ in range(size)]
        for id_, pos in positioned_tiles.items():
            x, y = pos
            tiles[top_left_y - y][x - top_left_x] = id_
        image = list(concat(
            [
                [
                "".join((self.tiles[tile].data[y_inner][1:-1] for tile in row_tiles))
                for y_inner in range(1, len(self.tiles[row_tiles[0]].data) - 1)
                ]
                for row_tiles in tiles
            ]
        ))
        return image


# refactor out of earlier class
def flip(image: List[str], x: bool=False, y: bool=False) -> List[str]:
    if x:
        image = list(map(lambda x: x[::-1], image))
    if y:
        image.reverse()
    return image

def rotate(image: List[str], count: int) -> List[str]:
    rotations = count % 4
    for _ in range(rotations):
        image = [
            "".join([image[i][j] for i in range(len(image) -1, -1, -1)])
            for j in range(len(image))
        ]
    return image

def detect_sea_monsters(image: List[str]) -> int:
    SEA_MONSTER = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    count = 0
    for base_y in range(len(image) - len(SEA_MONSTER)):
        for base_x in range(len(image[0]) - len(SEA_MONSTER[0])):
            fail = False
            for rel_y, rel_x in product(range(len(SEA_MONSTER)), range(len(SEA_MONSTER[0]))):
                if SEA_MONSTER[rel_y][rel_x] == "#" and not image[base_y + rel_y][base_x + rel_x] == "#":
                    fail = True
                    break
            if not fail:
                count += 1
    return count          


def detect_max_sea_monsters(image: List[str]) -> int:
    image_variations = [
        image,
        flip(image, x=True),
        rotate(image, 1),
        flip(rotate(image, 1), y=True),
        rotate(image, 2),
        flip(rotate(image, 2), x=True),
        rotate(image, 3),
        flip(rotate(image, 3), y=True),
    ]
    return max(map(detect_sea_monsters, image_variations))

def measure_roughness(image: List[str]) -> int:
    SEA_MONSTER = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    sea_monster_count = detect_max_sea_monsters(image)
    sea_monster_size = sum(map(lambda x: x.count("#"), SEA_MONSTER))
    roughness = sum(map(lambda x: x.count("#"), image)) - sea_monster_count * sea_monster_size
    return roughness

if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    filepath = Path(__file__).parent / "input.txt"
    tiles = TileStore.from_file(filepath)
    corners = tiles.find_corners()
    image = tiles.build_image()
    max_sea_monsters = detect_max_sea_monsters(image)
    roughness = measure_roughness(image)
    end = datetime.now()
    time = (end - start).total_seconds()
    print(time)
    print(corners)
    # for row in image:
    #     print(row)
    print(max_sea_monsters)
    print(roughness)
