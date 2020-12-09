from pathlib import Path

from part2 import find_sum_stream


def test_find_sum_stream():
    filepath = Path(__file__).parent / "sample_input.txt"
    datastream = map(int, filepath.read_text().splitlines())
    assert find_sum_stream(datastream, 127) == 62
