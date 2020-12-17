from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import re
from typing import List, Tuple


@dataclass
class TicketRules:
    allowed_ranges: List[Tuple[int, int]]

    @staticmethod
    def from_filepath(filepath: Path) -> TicketRules:
        rules = []
        for line in filepath.read_text().split("\n\n")[0].splitlines():
            range_pattern = r"(\d+-\d+)"
            ranges = re.findall(range_pattern, line)
            rules.extend([tuple(range_.split("-", 1)) for range_ in ranges])
        return TicketRules(rules)

    def ticket_error_rate(self, ticket: List[int]) -> int:
        error = 0
        for val in ticket:
            val = int(val)
            match = False
            for min_, max_ in self.allowed_ranges:
                if val >= int(min_) and val <= int(max_):
                    match = True
                    break
            if not match:
                error += val
        return error


def load_tickets(filepath: Path) -> List[List[int]]:
    other_tickets_section = filepath.read_text().split("\n\n")[2]
    other_tickets = []
    for other_ticket in other_tickets_section.splitlines()[1:]:
        other_tickets.append(other_ticket.split(","))
    return other_tickets


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    rules = TicketRules.from_filepath(filepath)
    other_tickets = load_tickets(filepath)
    error_rate = sum(map(lambda t: rules.ticket_error_rate(t), other_tickets))
    print(error_rate)
