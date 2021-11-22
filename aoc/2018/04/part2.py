from datetime import datetime
import re
from typing import Dict, List, Set, Tuple

from part1 import calc_minute_sleep_frequencies, load_input

def list_guards(logs: List[Tuple[datetime, str]]) -> Set[str]:
    guards = set()
    for _, text in logs:
        shift_start_match = re.match(r"Guard (?P<guard>\S*) begins shift", text)
        if shift_start_match:
            guards.add(shift_start_match.groupdict()["guard"])
    return guards


if __name__ == "__main__":
    # filename = "input_sample.txt"
    filename = "input.txt"
    logs = load_input(filename)
    guards = list_guards(logs)
    # Dict of guard to (minute, times slept)
    guard_most_slept_minute: Dict[str, Tuple[int, int]] = {}
    for guard in guards:
        freqs = calc_minute_sleep_frequencies(logs, guard)
        guard_most_slept_minute[guard] = max(freqs.items(), key=lambda item: item[1])
    most_common_guard_minute = max(guard_most_slept_minute.items(), key=lambda item: item[1][1])
    guard, (minute, count) = most_common_guard_minute
    print(f"Guard {guard}, minute {minute}, times {count}. Answer {int(guard[1:])*minute}")
