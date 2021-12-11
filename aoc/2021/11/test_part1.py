from part1 import step


def test_step_small():
    grid0 = [
        [1, 1, 1, 1, 1],
        [1, 9, 9, 9, 1],
        [1, 9, 1, 9, 1],
        [1, 9, 9, 9, 1],
        [1, 1, 1, 1, 1],
    ]
    flashes1 = 9
    grid1 = [
        [3, 4, 5, 4, 3],
        [4, 0, 0, 0, 4],
        [5, 0, 0, 0, 5],
        [4, 0, 0, 0, 4],
        [3, 4, 5, 4, 3],
    ]
    flashes2 = 0
    grid2 = [
        [4, 5, 6, 5, 4],
        [5, 1, 1, 1, 5],
        [6, 1, 1, 1, 6],
        [5, 1, 1, 1, 5],
        [4, 5, 6, 5, 4],
    ]
    actual1, actual_flash1 = step(grid0)
    # Need to deep compare lists
    for actual_row, grid1_row in zip(actual1, grid1):
        assert actual_row == grid1_row
    assert actual_flash1 == flashes1

    actual2, actual_flash2 = step(grid1)
    # Need to deep compare lists
    for actual_row, grid2_row in zip(actual2, grid2):
        assert actual_row == grid2_row
    assert actual_flash2 == flashes2
