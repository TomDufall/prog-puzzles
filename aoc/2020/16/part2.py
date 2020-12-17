from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import re
from typing import List, Tuple


@dataclass
class TicketRules:
    fields: List[Tuple[str, List[int]]]

    @staticmethod
    def from_string_list(rules_strs: List[str]) -> TicketRules:
        fields = []
        for rule in rules_strs:
            name = rule.split(":", 1)[0]
            ranges = re.findall(r"(\d+-\d+)", rule)
            fields.append(
                (name, list(
                    list(map(int, range_.split("-", 1))) for range_ in ranges)
                )
            )
        return TicketRules(fields)


    def is_possibly_valid_ticket_entry(self, num: int) -> bool:
        for field in self.fields:
            for range_ in field[1]:
                if range_[0] <= num <= range_[1]:
                    return True
        return False


    def is_possibly_valid_ticket(self, ticket: List[int]) -> bool:
        for entry in ticket:
            if not self.is_possibly_valid_ticket_entry(entry):
                return False
        return True


    def fits_field(self, value: int, field_index: int) -> bool:
        for range_ in self.fields[field_index][1]:
            if range_[0] <= value <= range_[1]:
                return True
        return False


    def fits_fields(self, value: int) -> Set[int]:
        return {i for i in range(len(self.fields)) if self.fits_field(value, i)}


    def calculate_possible_fields(self, tickets: List[List[int]]) -> List[Set[int]]:
        possible_indexes = [set(range(len(self.fields))) for _ in range(len(self.fields))]
        for ticket in tickets:
            if not self.is_possibly_valid_ticket(ticket):
                continue
            for i, entry in enumerate(ticket):
                fits_fields = self.fits_fields(entry)
                possible_indexes[i] = possible_indexes[i].intersection(fits_fields)
        return possible_indexes


    def calculate_fields(self, tickets: List[List[int]]) -> List[str]:
        possible_indexes = self.calculate_possible_fields(tickets)
        known_1 = set()
        change = True
        while change == True:
            change = False
            for i in range(len(possible_indexes)):
                if i not in known_1 and len(possible_indexes[i]) == 1:
                    value = next(iter(possible_indexes[i]))
                    known_1.add(i)
                    change = True
                    for j in range(len(possible_indexes)):
                        if j != i:
                            possible_indexes[j].discard(value)
        for possibility in product(*possible_indexes):
            if len(set(possibility)) == len(self.fields):
                return [self.fields[i][0] for i in possibility]
        return None


def load_input(
    filepath: Path
) -> Tuple[TicketRules, List[int], List[List[int]]]:
    rules_str, my_ticket_str, others_str = filepath.read_text().split("\n\n")
    rules = TicketRules.from_string_list(rules_str.splitlines())
    my_ticket = [
        int(num_str) for num_str in my_ticket_str.splitlines()[1].split(",")
    ]
    other_tickets = [
        [int(num_str) for num_str in other_ticket.split(",")]
        for other_ticket in others_str.splitlines()[1:]
    ]
    return (rules, my_ticket, other_tickets)


if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    filepath = Path(__file__).parent / "input.txt"
    rules, my_ticket, other_tickets = load_input(filepath)
    fields = rules.calculate_fields(other_tickets)
    result = 1
    for i in range(len(fields)):
        if fields[i].startswith("departure"):
            result *= my_ticket[i]
    end = datetime.now()
    time = (end - start).total_seconds()
    print(result)
    print(time)
