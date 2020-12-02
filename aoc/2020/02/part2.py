from abc import ABC
from dataclasses import dataclass
from operator import xor
from pathlib import Path
from typing import List


class PasswordPolicy(ABC):
    def match(self, password: str):
        return NotImplemented


@dataclass
class OriginalPasswordPolicy(PasswordPolicy):
    min_count: int
    max_count: int
    character: str

    def match(self, password: str):
        occurances = password.count(self.character)
        return occurances >= self.min_count and occurances <= self.max_count


@dataclass
class UpdatedPasswordPolicy(PasswordPolicy):
    # 1-indexed
    index_1: int
    index_2: int
    character: str

    def match(self, password: str):
        match_1 = password[self.index_1 - 1] == self.character
        match_2 = password[self.index_2 - 1] == self.character
        return xor(match_1, match_2)


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


def load_input_old_format(filepath: Path) -> List[Password]:
    passwords: List[Password] = []
    for line in filepath.read_text().splitlines():
        policy_str, password = line.split(": ")
        min_count, policy_str = policy_str.split("-")
        max_count, character = policy_str.split(" ")
        policy = OriginalPasswordPolicy(int(min_count), int(max_count), character)
        passwords.append(Password(policy, password))
    return passwords


def load_input_new_format(filepath: Path) -> List[Password]:
    passwords: List[Password] = []
    for line in filepath.read_text().splitlines():
        policy_str, password = line.split(": ")
        index_1, policy_str = policy_str.split("-")
        index_2, character = policy_str.split(" ")
        policy = UpdatedPasswordPolicy(int(index_1), int(index_2), character)
        passwords.append(Password(policy, password))
    return passwords


if __name__ == "__main__":
    filepath = Path("input.txt")
    input_ = load_input_new_format(filepath)
    print(count_valid_passwords(input_))
