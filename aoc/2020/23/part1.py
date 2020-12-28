from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass
class Cups:
    cups: Deque[int]

    @property
    def answer_str(self) -> None:
        one_index = self.cups.index(1)
        cups_copy = self.cups.copy()
        cups_copy.rotate(-1 * one_index)
        return "".join(map(str, list(cups_copy)[1:]))

    def _step(self) -> None:
        source_cup = self.cups.popleft()
        held_cups = [self.cups.popleft() for _ in range(3)]
        dest_cup = source_cup
        while True:
            dest_cup = (dest_cup - 1) % (len(self.cups) + 4)
            if dest_cup == 0:
                dest_cup = len(self.cups) + 4
            try:
                index = self.cups.index(dest_cup)
            except ValueError:
                continue
            for i, cup in enumerate(held_cups):
                self.cups.insert(index + i + 1, cup)
            break
        self.cups.append(source_cup)

    def step(self, n: int = 1) -> None:
        for _ in range(n):
            self._step()


if __name__ == "__main__":
    SAMPLE_INPUT = "389125467"
    INPUT = "523764819"
    MOVES = 100
    from datetime import datetime
    start = datetime.now()
    game = Cups(deque([int(char) for char in INPUT]))
    game.step(MOVES)
    answer = game.answer_str
    end = datetime.now()
    time = (end - start).total_seconds()
    print(time)
    print(game)
    print(answer)
