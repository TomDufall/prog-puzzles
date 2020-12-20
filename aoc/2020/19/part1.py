from __future__ import annotations
from dataclasses import dataclass
from itertools import tee
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Tuple


@dataclass
class Rules:
    rules: Dict[int, str]

    @staticmethod
    def from_str(input_: str) -> Rules:
        rules = {
            int(i): rule_str for i, rule_str
            in map(
                lambda x: x.split(": "),
                input_.splitlines()
            )
        }
        return Rules(rules)

    def validate(self, case: str) -> bool:
        return self._validate(case)[0]

    def _validate(self, case: str, next_char_i: int = 0, rule_i: int = 0) -> Tuple[bool, int]:
        rule = self.rules[rule_i]
        if next_char_i > len(case):
            return False, None
        if rule.startswith('"'):
            if case[next_char_i] != rule[1]:
                return False, None
            next_char_i += 1
        else:
            subrules = map(lambda x: list(filter(None, x.split(" "))), rule.split("|"))
            fail = True
            for subrule in subrules:
                fail_inner= False
                next_char_i_fork = next_char_i
                for part in subrule:
                    success, next_char_i_fork = self._validate(case, next_char_i_fork, int(part))
                    if not success:
                        fail_inner = True
                        break
                #print(subrule, fail_inner)
                if not fail_inner:
                    fail = False
                    next_char_i = next_char_i_fork
                    break
            if fail:
                return False, None
        if rule_i == 0:
            if next_char_i != len(case):
                return False, None
            return True, None
        else:
            return True, next_char_i

    def count_valid(self, cases: List[str]) -> int:
        return sum((1 for case in cases if self.validate(case)))


def load_input(filepath: Path) -> Tuple[Rules, List[str]]:
    rules_strs, cases_strs = filepath.read_text().split("\n\n")
    rules = Rules.from_str(rules_strs)
    cases = cases_strs.splitlines()
    return rules, cases


if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    filepath = Path(__file__).parent / "input.txt"
    rules, cases = load_input(filepath)
    successes = rules.count_valid(cases)
    end = datetime.now()
    time = (end - start).total_seconds()
    #print(rules)
    #print(cases)
    print(successes)
    print(time)
