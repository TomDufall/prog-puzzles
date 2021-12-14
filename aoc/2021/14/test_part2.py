from part2 import get_freqs_after_steps, step_pairs, to_pairs

RECIPES = {
    ("C", "H"): "B",
    ("H", "H"): "N",
    ("C", "B"): "H",
    ("N", "H"): "C",
    ("H", "B"): "C",
    ("H", "C"): "B",
    ("H", "N"): "C",
    ("N", "N"): "C",
    ("B", "H"): "H",
    ("N", "C"): "B",
    ("N", "B"): "B",
    ("B", "N"): "B",
    ("B", "B"): "N",
    ("B", "C"): "B",
    ("C", "C"): "N",
    ("C", "N"): "C",
}


def test_to_pairs():
    template = "NNCB"
    expected = {
        ("N", "N"): 1,
        ("N", "C"): 1,
        ("C", "B"): 1,
    }
    assert dict(to_pairs(template)) == expected


def test_step_pairs_1():
    template = list("NNCB")
    pairs = {
        ("N", "N"): 1,
        ("N", "C"): 1,
        ("C", "B"): 1,
    }
    expected = {
        ("N", "C"): 1,
        ("C", "N"): 1,
        ("N", "B"): 1,
        ("B", "C"): 1,
        ("C", "H"): 1,
        ("H", "B"): 1,
    }
    assert step_pairs(pairs, RECIPES) == expected


def test_step_pairs_2():
    template = list("NNCB")
    pairs = {
        ("N", "N"): 1,
        ("N", "C"): 1,
        ("C", "B"): 1,
    }
    # NBCCNBBBCBHCB
    expected = {
        ("C", "N"): 1,
        ("N", "B"): 2,
        ("B", "C"): 2,
        ("C", "C"): 1,
        ("B", "B"): 2,
        ("C", "B"): 2,
        ("B", "H"): 1,
        ("H", "C"): 1,
    }
    one = step_pairs(pairs, RECIPES)
    two = step_pairs(one, RECIPES)
    assert two == expected


# {('N', 'B'): 4, ('B', 'B'): 4, ('B', 'C'): 3, ('C', 'N'): 2, ('N', 'C'): 1, ('C', 'C'): 1, ('B', 'N'): 2, ('C', 'H'): 2, ('H', 'B'): 3, ('B', 'H'): 1, ('H', 'H'): 1}

# {('N', 'B'): 9, ('B', 'B'): 9, ('B', 'N'): 6, ('B', 'C'): 4, ('C', 'C'): 2, ('C', 'N'): 3, ('N', 'C'): 1, ('C', 'B'): 5, ('B', 'H'): 3, ('H', 'C'): 3, ('H', 'H'): 1, ('H', 'N'): 1, ('N', 'H'): 1})


def test_get_freqs_after_steps_one():
    template = list("NNCB")
    expected = {
        "B": 2,
        "C": 2,
        "H": 1,
        "N": 2,
    }
    freqs = get_freqs_after_steps(template, RECIPES, 1)
    assert freqs == expected


def test_get_freqs_after_steps_two():
    template = list("NNCB")
    expected = {
        "B": 6,
        "C": 4,
        "H": 1,
        "N": 2,
    }
    freqs = get_freqs_after_steps(template, RECIPES, 2)
    assert freqs == expected


def test_get_freqs_after_steps():
    template = list("NNCB")
    freqs = get_freqs_after_steps(template, RECIPES, 40)
    assert freqs["B"] == 2192039569602
    assert max(freqs.values()) == 2192039569602
    assert freqs["H"] == 3849876073
    assert min(freqs.values()) == 3849876073
