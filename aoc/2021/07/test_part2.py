from part2 import find_min_moves


def test_find_min_moves():
    input_ = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    min_moves = find_min_moves(input_)
    assert min_moves[2] == 206
    assert min_moves[5] == 168
