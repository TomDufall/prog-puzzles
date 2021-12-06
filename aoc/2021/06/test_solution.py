from solution import step


def test_step_countdown():
    initial_state = {
        1: 1,
        2: 1,
        3: 2,
        4: 1,
    }
    expected = {
        0: 1,
        1: 1,
        2: 2,
        3: 1,
    }
    assert step(initial_state, 1) == expected


def test_step_spawn():
    initial_state = {
        0: 1,
        1: 1,
        2: 2,
        3: 1,
    }
    expected = {
        0: 1,
        1: 2,
        2: 1,
        6: 1,
        8: 1,
    }
    assert step(initial_state, 1) == expected
