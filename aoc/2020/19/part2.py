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

    @staticmethod
    def test_rule(rule: str, case: str, i: int) -> Tuple[bool, List[int]]:
        pass

    def _validate(self, case: str, next_char_i: int = 0, rule_i: int = 0) -> Tuple[bool, List[int]]:
        rule = self.rules[rule_i]
        # if next_char_i > len(case):
        #     return False, None
        if rule.startswith('"'):
            try:
                if case[next_char_i] != rule[1]:
                    return False, []
                next_char_i += 1
                next_char_i = [next_char_i]
            except IndexError:
                return False, []
        else:
            subrules = map(lambda x: list(filter(None, x.split(" "))), rule.split("|"))
            next_char_i_2 = []
            for subrule in subrules:
                next_i = [next_char_i]
                for part in subrule:
                    next_next_i = []
                    for i in next_i:
                        success, possible_next_next_i = self._validate(case, i, int(part))
                        #print(success, possible_next_next_i, i, part, case[i-1:])
                        if success:
                            next_next_i.extend(possible_next_next_i)
                    next_i = next_next_i
                #print(subrule, next_i)
                next_char_i_2.extend(next_i)
            if len(next_char_i_2) == 0:
                return False, []
            next_char_i = next_char_i_2
            #print(next_char_i)
        if rule_i == 0:
            for next_char_i_case in next_char_i:
                if next_char_i_case == len(case):
                    return True, []
            return False, []
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
    filepath = Path(__file__).parent / "input_2.txt"
    rules, cases = load_input(filepath)
    successes = rules.count_valid(cases)
    end = datetime.now()
    time = (end - start).total_seconds()
    #print(rules)
    #print(cases)
    print(successes)
    print(time)
