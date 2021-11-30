from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from toolz import concat


@dataclass
class ForwardLinkedItem:
    value: int
    next_: Optional[ForwardLinkedItem]

    def __repr__(self):
        return f"LinkedItem(value={self.value}, next_={self.next_.value})"


@dataclass
class IndexableForwardLinkedCircle:
    items: Dict[int, ForwardLinkedItem]

    def __init__(self, items: List[int]):
        first = ForwardLinkedItem(items[0], None)
        item_dict = {items[0]: first}
        prev = first
        for item in items[1:]:
            new = ForwardLinkedItem(item, None)
            prev.next_ = new
            prev = new
            item_dict[item] = new
        prev.next_ = first
        self.items = item_dict

    def __getitem__(self, key):
        return self.items[key]


@dataclass
class Cups:
    cups: IndexableForwardLinkedCircle
    first_cup: ForwardLinkedItem
    moves: int = 0

    def __init__(self, input_: str, count: int):
        cups = list(
            concat(
                [
                    map(int, list(input_)),
                    range(len(input_) + 1, count + 1)
                ]
            )
        )
        self.cups = IndexableForwardLinkedCircle(cups)
        self.first_cup = self.cups[int(input_[0])]

    @property
    def answer_str(self) -> Tuple[int, int]:
        cup_one = self.cups.items[1]
        return (cup_one.next_.value, cup_one.next_.next_.value)

    def step(self, n: int = 1) -> None:
        for _ in range(n):
            held_cups = (self.first_cup.next_, self.first_cup.next_.next_, self.first_cup.next_.next_.next_)
            held_cups_labels = {self.first_cup.next_.value, self.first_cup.next_.next_.value, self.first_cup.next_.next_.next_.value}
            source_cup_label = self.first_cup.value
            dest_cup_label = source_cup_label
            while True:
                dest_cup_label -= 1
                if dest_cup_label == 0:
                    dest_cup_label = len(self.cups.items)
                elif dest_cup_label in held_cups_labels:
                    continue
                elif dest_cup_label == source_cup_label:
                    raise Exception("Stuck in infinite loop")
                break
            insertion_point = self.cups.items[dest_cup_label]
            self.first_cup.next_ = held_cups[-1].next_
            held_cups[-1].next_ = insertion_point.next_
            insertion_point.next_ = held_cups[0]

            self.first_cup = self.first_cup.next_
            self.moves += 1


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
