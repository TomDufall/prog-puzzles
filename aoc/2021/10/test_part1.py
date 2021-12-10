import pytest

from part1 import sum_errors, validate_line


@pytest.mark.parametrize(
    "line",
    [
        "()",
        "[]",
        "{}",
        "<>",
        "([])",
        "{()()()}",
        "<([{}])>",
        "[<>({}){}[([])<>]]",
        "(((((((((())))))))))",
    ],
)
def test_validate_line_pass(line):
    assert validate_line(line) is None


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("(]", (1, "]")),
        ("{()()()>", (7, ">")),
        ("(((()))}", (7, "}")),
        ("<([]){()}[{}])", (13, ")")),
    ],
)
def test_validate_line_errors(line, expected):
    assert validate_line(line) == expected


def test_sum_errors():
    errors = [
        None,
        (5, ")"),  # 3
        (7, "]"),  # 57
        (2, "}"),  # 1197
        None,
        (21, "}"),  # 1197
        (131, ">"),  # 25137
    ]
    expected = 27591
    assert sum_errors(errors) == expected
