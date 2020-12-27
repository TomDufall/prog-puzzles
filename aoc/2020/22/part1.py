from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Deque


@dataclass
class Combat:
    p1: Deque[str]
    p2: Deque[str]
    turn: int = 0

    @staticmethod
    def from_file(filepath: Path) -> Combat:
        players = filepath.read_text().split("\n\n")
        p1 = deque(map(int, players[0].splitlines()[1:]))
        p2 = deque(map(int, players[1].splitlines()[1:]))
        return Combat(p1, p2)

    def step(self) -> None:
        if len(self.p1) == 0 or len(self.p2) == 0:
            raise StopIteration
        card_1 = self.p1.popleft()
        card_2 = self.p2.popleft()
        if card_1 > card_2:
            self.p1.append(card_1)
            self.p1.append(card_2)
        elif card_2 > card_1:
            self.p2.append(card_2)
            self.p2.append(card_1)
        else:
            raise ValueError("Two equal cards")

    def calculate_score(self) -> int:
        winning_deck = self.p1 if len(self.p1) > 0 else self.p2
        return sum((
            (index + 1) * card for index, card in
            enumerate(reversed(winning_deck))
        ))

    def run(self) -> int:
        while True:
            try:
                self.step()
            except StopIteration:
                return self.calculate_score()


if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    filepath = Path(__file__).parent / "input.txt"
    game = Combat.from_file(filepath)
    score = game.run()
    end = datetime.now()
    time = (end - start).total_seconds()
    print(time)
    print(score)
