from part2 import decode_display, generate_display_decoding


def test_generate_display_decoding():
    signals = [
        "acedgfb",
        "cdfbe",
        "gcdfa",
        "fbcad",
        "dab",
        "cefabd",
        "cdfgeb",
        "eafb",
        "cagedb",
        "ab",
    ]
    expected = {
        "acedgfb": 8,
        "cdfbe": 5,
        "gcdfa": 2,
        "fbcad": 3,
        "dab": 7,
        "cefabd": 9,
        "cdfgeb": 6,
        "eafb": 4,
        "cagedb": 0,
        "ab": 1,
    }
    sorted_expected = {
        "".join(sorted(key)): value for key, value in expected.items()
    }
    assert generate_display_decoding(signals) == sorted_expected


def test_decode_display():
    signals = [
        "acedgfb",
        "cdfbe",
        "gcdfa",
        "fbcad",
        "dab",
        "cefabd",
        "cdfgeb",
        "eafb",
        "cagedb",
        "ab",
    ]
    outputs = ["cdfeb", "fcadb", "cdfeb", "cdbaf"]
    expected = [5, 3, 5, 3]
    assert decode_display(signals, outputs) == expected


def test_decode_display_2():
    signals = [
        "be",
        "cfbegad",
        "cbdgef",
        "fgaecd",
        "cgeb",
        "fdcge",
        "agebfd",
        "fecdb",
        "fabcd",
        "edb",
    ]
    outputs = ["fdgacbe", "cefdb", "cefbgd", "gcbe"]
    expected = [8, 3, 9, 4]
    assert decode_display(signals, outputs) == expected


def test_decode_display_3():
    signals = [
        "edbfga",
        "begcd",
        "cbg",
        "gc",
        "gcadebf",
        "fbgde",
        "acbgfd",
        "abcde",
        "gfcbed",
        "gfec",
    ]
    outputs = ["fcgedb", "cgb", "dgebacf", "gc"]
    expected = [9, 7, 8, 1]
    print(generate_display_decoding(signals))
    assert decode_display(signals, outputs) == expected
