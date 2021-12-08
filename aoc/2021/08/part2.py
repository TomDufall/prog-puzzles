from __future__ import annotations

from collections import defaultdict

from part1 import load_input


def get_only(items: list[str]) -> str:
    if len(items) != 1:
        raise ValueError("More than one item")
    return items[0]


def generate_display_decoding(digit_attempts: list[str]) -> dict[str, int]:
    """
    Given an unordered list of outputs for each input (0-9), calculate the
    mapping of actual signal to intended signal.

    Deduction process - digits
    1: 2 segments
    4: 4 segments
    7: 3 segments
    8: 7 segments
    6: 6 segments and missing one of the segments in 1
    9: 6 segments and missing one of the same segments as 4
    0: the other 6 segment
    2: 5 segments and missing a segment that every other digit has
    5: 5 seg and missing same seg as 6
    3: remaining 5 seg
    """
    # Easy digits - 1,4, 7, 8
    mapping: dict[int, str] = {}
    mapping[1] = get_only(list(filter(lambda x: len(x) == 2, digit_attempts)))
    mapping[4] = get_only(list(filter(lambda x: len(x) == 4, digit_attempts)))
    mapping[7] = get_only(list(filter(lambda x: len(x) == 3, digit_attempts)))
    mapping[8] = get_only(list(filter(lambda x: len(x) == 7, digit_attempts)))

    six_segments = [x for x in digit_attempts if len(x) == 6]
    # Find 6 - 6-seg and missing one of the segments in 1
    segs_one = {x for x in mapping[1]}
    for maybe in six_segments:
        missing_segs = {x for x in iter("abcdefg") if x not in maybe}
        if len(missing_segs.intersection(segs_one)) > 0:
            mapping[6] = maybe
            six_segments.remove(maybe)
            break
    else:
        raise ValueError

    # Find 9 - 6-seg and missing one of the same segs as 4
    # Find 0 - last 6-seg
    for maybe in six_segments:
        missing_segs_four = {x for x in iter("abcdefg") if x not in mapping[4]}
        missing_segs = {x for x in iter("abcdefg") if x not in maybe}
        if len(missing_segs.intersection(missing_segs_four)) > 0:
            mapping[9] = maybe
            six_segments.remove(maybe)
            mapping[0] = get_only(six_segments)
            break

    # Find 2 - 5-seg and missing a segment every other digit has
    segment_freqs: dict[str, int] = defaultdict(lambda: 0)
    for digit in digit_attempts:
        for segment in digit:
            segment_freqs[segment] += 1
    five_segments = [x for x in digit_attempts if len(x) == 5]
    two_missing_digit = get_only(
        [key for key, value in segment_freqs.items() if value == 9]
    )
    two = get_only([x for x in five_segments if two_missing_digit not in x])
    mapping[2] = two
    five_segments.remove(two)

    # Find 5 - 5-seg and missing same seg as 6
    # Find 3 - remaining 5-seg
    missing_segs_six = {x for x in iter("abcdefg") if x not in mapping[6]}
    for attempt in five_segments:
        missing_segs = {x for x in iter("abcdefg") if x not in attempt}
        if len(missing_segs.intersection(missing_segs_six)) > 0:
            mapping[5] = attempt
            five_segments.remove(attempt)
            mapping[3] = get_only(five_segments)

    if len(mapping) != 10:
        raise ValueError("Mappings missing")
    return {"".join(sorted(value)): key for key, value in mapping.items()}


def decode_display(digit_attempts: list[str], outputs: list[str]) -> list[int]:
    decoding_mapping = generate_display_decoding(digit_attempts)
    return [decoding_mapping["".join(sorted(output))] for output in outputs]


if __name__ == "__main__":
    data = load_input()

    def get_display_value(item):
        digits = decode_display(item[0], item[1])
        return int("".join(map(str, digits)))

    total = sum(map(get_display_value, data))
    print(total)
