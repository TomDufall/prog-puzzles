from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class PasswordPolicy:
    min_count: int
    max_count: int
    character: str

    def match(self, password: str):
        occurrences = password.count(self.character)
        return occurrences >= self.min_count and occurrences <= self.max_count


@dataclass
class Password:
    policy: PasswordPolicy
    password: str

    def validate(self):
        return self.policy.match(self.password)


def count_valid_passwords(passwords: List[Password]) -> int:
    is_valid = lambda password: password.validate()
    valid_passwords = list(filter(is_valid, passwords))
    return len(valid_passwords)


def load_input(filepath: Path) -> List[Password]:
    passwords: List[Password] = []
    for line in filepath.read_text().splitlines():
        policy_str, password = line.split(": ")
        min_count, policy_str = policy_str.split("-")
        max_count, character = policy_str.split(" ")
        policy = PasswordPolicy(int(min_count), int(max_count), character)
        passwords.append(Password(policy, password))
    return passwords


if __name__ == "__main__":
    filepath = Path("input.txt")
    input_ = load_input(filepath)
    print(count_valid_passwords(input_))