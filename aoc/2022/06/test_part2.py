import pytest
from part2 import find_start_of_content

@pytest.mark.parametrize(
    ("data", "expected"),
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ]
)
def test_find_start_of_content(data, expected):
    assert find_start_of_content(data) == expected
