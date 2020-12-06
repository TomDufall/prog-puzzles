from pathlib import Path
from typing import List


def merge_strings(group: List[str]) -> str:
    sets = (set(str_) for str_ in group)
    result = next(sets).intersection(*sets)
    return "".join(result)


def count_total_group_answers(groups: List[List[str]]) -> int:
    group_answers = [merge_strings(group) for group in groups]
    return sum(map(len, group_answers))


def load_input(filepath: Path) -> List[List[str]]:
    groups = filepath.read_text().split("\n\n")
    result = [group.splitlines() for group in groups]
    return result


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    groups = load_input(filepath)
    print(count_total_group_answers(groups))
