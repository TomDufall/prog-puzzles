import pytest

from part2 import flip, rotate, Tile


@pytest.mark.parametrize(
    ("image", "flip_x", "flip_y", "expected"),
    [
        (["..#."], False, False, ["..#."]),
        (["..#.", "#.#."], False, False, ["..#.", "#.#."]),
        (["..#."], True, False, [".#.."]),
        (["..#.", "#.#."], True, False, [".#..", ".#.#"]),
        (["..#."], False, True, ["..#."]),
        (["..#.", "#.#."], False, True, ["#.#.", "..#."]),
        (["..#."], True, True, [".#.."]),
        (["..#.", "#.#."], True, True, [".#.#", ".#.."]),
    ]
)
def test_flip(image, flip_x, flip_y, expected):
    assert flip(image, flip_x, flip_y) == expected


@pytest.mark.parametrize(
    ("image", "count", "expected"),
    [
        (["..x", "x.x", "..x"], 0, ["..x", "x.x", "..x"]),
        (["..x", "x.x", "..x"], 1, [".x.", "...", "xxx"]),
        (["..x", "x.x", "..x"], 2, ["x..", "x.x", "x.."]),
        (["..x", "x.x", "..x"], 3, ["xxx", "...", ".x."]),
        (["..x", "x.x", "..x"], 4, ["..x", "x.x", "..x"]),
        (["..x", "x.x", "..x"], 5, [".x.", "...", "xxx"]),
        (["..x", "x.x", "..x"], -1, ["xxx", "...", ".x."]),
    ]
)
def test_rotate(image, count, expected):
    assert rotate(image, count) == expected


class TestTile():
    def test_edges(self):
        tile = Tile("1", ["...x", "x.x.", "xxxx", "xxx."])
        top = "...x"
        right = "x.x."
        bot = ".xxx"
        left = "xxx."
        expected = (top, right, bot, left)
        assert tile.edges == expected
