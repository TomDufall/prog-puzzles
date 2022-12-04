from part1 import score_strategy


def test_score_strategy():
    strategy = [
        ("A", "Y"),
        ("B", "X"),
        ("C", "Z"),
    ]
    assert score_strategy(strategy) == 15
