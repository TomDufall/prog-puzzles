from __future__ import annotations
from dataclasses import dataclass
from profilehooks import profile
from typing import Dict, List, Tuple

from toolz import concat


@dataclass
class IndexableForwardLinkedCircle:
    items: Dict[int, int]

    def __init__(self, items: List[int]):
        item_dict = {}
        prev = items[0]
        for item in items[1:]:
            item_dict[prev] = item
            prev = item
        item_dict[items[-1]] = items[0]
        self.items = item_dict

    def __getitem__(self, key):
        return self.items[key]


@dataclass
class Cups:
    cups: IndexableForwardLinkedCircle
    first_cup: int
    moves: int = 0

    def __init__(self, input_: str, count: int):
        cups = list(concat([map(int, list(input_)), range(len(input_) + 1, count + 1)]))
        self.cups = IndexableForwardLinkedCircle(cups)
        self.first_cup = int(input_[0])

    @property
    def answer_str(self) -> Tuple[int, int]:
        return (self.cups.items[1], self.cups.items[self.cups.items[1]])

    @profile
    def step(self, n: int = 1) -> None:
        cups = self.cups.items
        first_cup = self.first_cup
        for _ in range(n):
            # held_cups = (self.first_cup.next_, self.first_cup.next_.next_, self.first_cup.next_.next_.next_)
            held_0 = cups[first_cup]
            held_1 = cups[held_0]
            held_2 = cups[held_1]
            dest_cup_label = first_cup
            while True:
                dest_cup_label -= 1
                if dest_cup_label == 0:
                    dest_cup_label = len(cups)
                # elif dest_cup_label in held_cups_labels
                if (
                    dest_cup_label == held_0
                    or dest_cup_label == held_1
                    or dest_cup_label == held_2
                ):
                    continue
                elif dest_cup_label == first_cup:
                    self.first_cup = first_cup
                    raise Exception("Stuck in infinite loop")
                break

            cups[first_cup] = cups[held_2]
            cups[held_2] = cups[dest_cup_label]
            cups[dest_cup_label] = held_0

            first_cup = cups[first_cup]
            # self.moves += 1
        self.first_cup = first_cup


if __name__ == "__main__":
    SAMPLE_INPUT = "389125467"
    INPUT = "523764819"
    MOVES = 10000000
    COUNT = 1000000
    from datetime import datetime

    start = datetime.now()
    game = Cups(INPUT, COUNT)
    init = datetime.now()
    game.step(MOVES)
    answer = game.answer_str
    end = datetime.now()
    init_time = (init - start).total_seconds()
    time = (end - start).total_seconds()
    print(init_time, time)
    print(answer)
    print(answer[0] * answer[1])
