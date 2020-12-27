from __future__ import annotations
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Deque, Set, Tuple


@dataclass
class Combat:
    p1: Deque[str]
    p2: Deque[str]
    turn: int = 0
    history: Set[Tuple[Tuple[str], Tuple[str]]] = field(default_factory=set)
    game_depth: int = 0

    @staticmethod
    def from_file(filepath: Path) -> Combat:
        players = filepath.read_text().split("\n\n")
        p1 = deque(map(int, players[0].splitlines()[1:]))
        p2 = deque(map(int, players[1].splitlines()[1:]))
        return Combat(p1, p2)

    def step(self) -> None:
        if self.turn > 10000:
            raise Exception("Running too long?")
        if len(self.p1) == 0 or len(self.p2) == 0 or (tuple(self.p1), tuple(self.p2)) in self.history:
            raise StopIteration
        self.history.add((tuple(self.p1), tuple(self.p2)))
        card_1 = self.p1.popleft()
        card_2 = self.p2.popleft()
        if len(self.p1) >= card_1 and len(self.p2) >= card_2:
            # RECURSE!
            subgame = Combat(deque(list(self.p1)[:card_1]), deque(list(self.p2)[:card_2]), game_depth=self.game_depth + 1)
            subgame.run()
            winner = subgame.get_winner()
        else:
            # Regular Combat
            if card_1 > card_2:
                winner = "p1"
            elif card_2 > card_1:
                winner = "p2"
            else:
                raise ValueError("Two equal cards")
        if winner == "p1":
            self.p1.append(card_1)
            self.p1.append(card_2)
        elif winner == "p2":
            self.p2.append(card_2)
            self.p2.append(card_1)
        else:
            raise ValueError("No winner found")
        self.turn += 1

    def get_winner(self) -> str:
        if len(self.p1) > 0 and len(self.p2) > 0:
            return "p1"
        else:
            return "p1" if len(self.p1) > 0 else "p2"

    def calculate_score(self) -> int:
        if len(self.p1) > 0 and len(self.p2) > 0:
            winning_deck = self.p1
        else:
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
