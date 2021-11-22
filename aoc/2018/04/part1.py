from datetime import datetime, time
import re
from typing import Dict, List, Tuple

def load_input(filename: str = "input.txt") -> List[Tuple[datetime, str]]:
    with open(filename) as f:
        lines = f.readlines()
    parsed = []
    for line in lines:
        timestamp, text = line[1:].split("] ", 1)
        parsed_timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
        parsed.append((parsed_timestamp, text))
    return sorted(parsed, key=lambda x: x[0])

def calc_sleep_duration_in_shift(start: datetime, end: datetime) -> int:
    """
    Calc sleep duration for a period between 00:00 and 00:59 inclusive based on two timestamps.
    """
    start_min = 0 if start.hour == 23 else start.minute
    end_min = 59 if end.hour != 0 else end.minute
    return end_min - start_min

def calc_asleep_time(logs: List[Tuple[datetime, str]]) -> Dict[str, int]:
    """
    Only count between 00:00 and 00:59 inclusive
    Assume guard awake when not on duty at 00:00 - only count sleep on shift
    """
    guard_sleep: Dict[str, int] = {}
    guard: str = "unknown"

    for i, (timestamp, text) in enumerate(logs):
        shift_start_match = re.match(r"Guard (?P<guard>\S*) begins shift", text)
        if shift_start_match:
            # clean up end of shift
            if i != 0 and "wakes up" not in logs[i - 1][1]:
                # guard asleep at end of shift
                last_action_time = logs[i - 1][0]
                guard_sleep[guard] += calc_sleep_duration_in_shift(last_action_time, timestamp)

            guard = shift_start_match.groupdict()["guard"]
            if guard not in guard_sleep:
                guard_sleep[guard] = 0
            continue
        elif "wakes up" in text:
            last_action_time = logs[i - 1][0]
            guard_sleep[guard] += calc_sleep_duration_in_shift(last_action_time, timestamp)
    return guard_sleep

def calc_sleep_minutes_in_shift(start: datetime, end: datetime) -> List[int]:
    """
    Calc sleep minutes slept in a period between 00:00 and 00:59 inclusive based on two timestamps.
    """
    start_min = 0 if start.hour == 23 else start.minute
    end_min = 59 if end.hour != 0 else end.minute
    return list(range(start_min, end_min + 1))

def calc_minute_sleep_frequencies(logs: List[Tuple[datetime, str]], guard: str) -> Dict[int, int]:
    """
    Only count between 00:00 and 00:59 inclusive
    Assume guard awake when not on duty at 00:00 - only count sleep on shift
    Find minute most commonly asleep
    """
    sleeping_minutes = {}

    for i, (timestamp, text) in enumerate(logs):
        shift_start_match = re.match(r"Guard (?P<guard>\S*) begins shift", text)
        if shift_start_match:
            # clean up end of shift
            # guard can be asleep at end of shift
            if i != 0 and new_guard == guard and "wakes up" not in logs[i - 1][1]:
                # guard asleep at end of shift
                last_action_time = logs[i - 1][0]
                sleep_minutes = calc_sleep_minutes_in_shift(last_action_time, timestamp)
                for minute in sleep_minutes:
                    if minute not in sleeping_minutes:
                        sleeping_minutes[minute] = 1
                    else:
                        sleeping_minutes[minute] += 1

            new_guard = shift_start_match.groupdict()["guard"]
        elif new_guard != guard:
            continue
        elif "wakes up" in text:
            last_action_time = logs[i - 1][0]
            sleep_minutes = calc_sleep_minutes_in_shift(last_action_time, timestamp)
            for minute in sleep_minutes:
                if minute not in sleeping_minutes:
                    sleeping_minutes[minute] = 1
                else:
                    sleeping_minutes[minute] += 1
    return sleeping_minutes
                    
def calc_most_slept_minute(logs: List[Tuple[datetime, str]], guard: str) -> int:
    sleeping_minutes = calc_minute_sleep_frequencies(logs, guard)
    return max(sleeping_minutes.items(), key=lambda item: item[1])[0]

if __name__ == "__main__":
    # filename = "input_sample.txt"
    filename = "input.txt"
    _input = load_input(filename)
    print(_input[0])
    guard_sleep = calc_asleep_time(_input)
    print(guard_sleep)
    sleepiest_guard = max(guard_sleep.items(), key=lambda item: item[1])[0]
    common_minute = calc_most_slept_minute(_input, sleepiest_guard)
    print(f"guard: {sleepiest_guard} at minute {common_minute}. Answer {int(sleepiest_guard[1:]) * common_minute}")
