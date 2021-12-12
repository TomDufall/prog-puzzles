from part2 import find_routes


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
        ["start", "A", "b", "A", "b", "A", "c", "A", "end"],
        ["start", "A", "b", "A", "b", "A", "end"],
        ["start", "A", "b", "A", "b", "end"],
        ["start", "A", "b", "A", "c", "A", "b", "A", "end"],
        ["start", "A", "b", "A", "c", "A", "b", "end"],
        ["start", "A", "b", "A", "c", "A", "c", "A", "end"],
        ["start", "A", "b", "A", "c", "A", "end"],
        ["start", "A", "b", "A", "end"],
        ["start", "A", "b", "d", "b", "A", "c", "A", "end"],
        ["start", "A", "b", "d", "b", "A", "end"],
        ["start", "A", "b", "d", "b", "end"],
        ["start", "A", "b", "end"],
        ["start", "A", "c", "A", "b", "A", "b", "A", "end"],
        ["start", "A", "c", "A", "b", "A", "b", "end"],
        ["start", "A", "c", "A", "b", "A", "c", "A", "end"],
        ["start", "A", "c", "A", "b", "A", "end"],
        ["start", "A", "c", "A", "b", "d", "b", "A", "end"],
        ["start", "A", "c", "A", "b", "d", "b", "end"],
        ["start", "A", "c", "A", "b", "end"],
        ["start", "A", "c", "A", "c", "A", "b", "A", "end"],
        ["start", "A", "c", "A", "c", "A", "b", "end"],
        ["start", "A", "c", "A", "c", "A", "end"],
        ["start", "A", "c", "A", "end"],
        ["start", "A", "end"],
        ["start", "b", "A", "b", "A", "c", "A", "end"],
        ["start", "b", "A", "b", "A", "end"],
        ["start", "b", "A", "b", "end"],
        ["start", "b", "A", "c", "A", "b", "A", "end"],
        ["start", "b", "A", "c", "A", "b", "end"],
        ["start", "b", "A", "c", "A", "c", "A", "end"],
        ["start", "b", "A", "c", "A", "end"],
        ["start", "b", "A", "end"],
        ["start", "b", "d", "b", "A", "c", "A", "end"],
        ["start", "b", "d", "b", "A", "end"],
        ["start", "b", "d", "b", "end"],
        ["start", "b", "end"],
    ]
    actual = find_routes(paths)
    assert sorted(actual) == sorted(expected)
