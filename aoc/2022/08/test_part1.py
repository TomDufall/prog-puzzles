from part1 import get_visible_trees_1d, load_input

def test_load_input():
    expected = [
        [3,0,3,7,3],
        [2,5,5,1,2],
        [6,5,3,3,2],
        [3,3,5,4,9],
        [3,5,3,9,0],
    ]
    assert load_input("sample_input.txt") == expected

def test_get_visible_trees_1d():
    row = [3, 0, 3, 7, 3]
    expected = {0, 3}
    assert get_visible_trees_1d(row) == expected