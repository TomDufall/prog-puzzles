from part1 import nth_play, play

def test_play():
    plays = play([0,3,6])
    expected = [0,3,6,0,3,3,1,0,4,0]
    for num in expected:
        assert next(plays) == num

def test_play_2():
    assert nth_play([0,3,6], 2020) == 436
