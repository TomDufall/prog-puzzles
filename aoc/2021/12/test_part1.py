from part1 import find_routes, load_input


def test_load_input():
    expected = {
        "start": {"A", "b"},
        "A": {"b", "c", "end", "start"},
        "b": {"A", "d", "end", "start"},
        "c": {"A"},
        "d": {"b"},
        "end": {"A", "b"},
    }
    assert load_input("sample_input.txt") == expected


def test_find_routes():
    paths = {
        "start": {"A", "b", "start"},
        "A": {"b", "c", "end"},
        "b": {"A", "d", "end", "start"},
        "c": {"A"},
        "d": {"b"},
        "end": {"A", "b"},
    }
    expected = [
        ["start", "A", "b", "A", "c", "A", "end"],
        ["start", "A", "b", "A", "end"],
        ["start", "A", "b", "end"],
        ["start", "A", "c", "A", "b", "A", "end"],
        ["start", "A", "c", "A", "b", "end"],
        ["start", "A", "c", "A", "end"],
        ["start", "A", "end"],
        ["start", "b", "A", "c", "A", "end"],
        ["start", "b", "A", "end"],
        ["start", "b", "end"],
    ]
    assert sorted(find_routes(paths)) == sorted(expected)
