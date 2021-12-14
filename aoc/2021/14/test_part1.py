import pytest

from part1 import step


@pytest.mark.parametrize(
    ("steps", "expected"),
    [
        (1, "NCNBCHB"),
        (2, "NBCCNBBBCBHCB"),
        (3, "NBBBCNCCNBBNBNBBCHBHHBCHB"),
        (4, "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"),
    ],
)
def test_step(steps, expected):
    template = list("NNCB")
    recipes = {
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
    assert step(template, recipes, steps) == list(expected)
