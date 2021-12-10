import pytest

from part2 import complete_string, score_fixes


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
        ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
        ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
        ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
        ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>"),
        ("[<>({}){}[([])<>]]", None),
    ],
)
def test_complete_string(string, expected):
    assert complete_string(string) == expected


@pytest.mark.parametrize(
    ("fixes", "expected"),
    [
        (["}}]])})]"], 288957),
        ([")}>]})"], 5566),
        (["}}>}>))))"], 1480781),
        (["]]}}]}]}>"], 995444),
        (["])}>"], 294),
        (["}}]])})]", ")}>]})", "}}>}>))))", "]]}}]}]}>", "])}>"], 288957),
    ],
)
def test_score_fixes(fixes, expected):
    assert score_fixes(fixes) == expected
