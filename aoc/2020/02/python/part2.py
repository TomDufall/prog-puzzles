from abc import ABC
from dataclasses import dataclass
from operator import xor
from pathlib import Path
from typing import List


class PasswordPolicy(ABC):
    def match(self, password: str) -> bool:
        return NotImplemented


@dataclass
class UpdatedPasswordPolicy(PasswordPolicy):
    # 1-indexed
    index_1: int
    index_2: int
    character: str

    def match(self, password: str) -> bool:
        """
        Check if the given password matches the policy.
        A password matches if exactly one of characters at self.index_1 and
        self.index_2 of the password (1-indexed) match self.character.
        :param password:
        :return: Whether or not the password is valid
        """
        match_1 = password[self.index_1 - 1] == self.character
        match_2 = password[self.index_2 - 1] == self.character
        return xor(match_1, match_2)


@dataclass
class Password:
    """
    Password stores a password and its validation policy.
    It can be used to check the validity of the password.
    """
    policy: PasswordPolicy
    password: str

    def validate(self) -> bool:
        """
        Check if the password complies with the password policy.
        :return: Whether or not the password is valid
        """
        return self.policy.match(self.password)


def count_valid_passwords(passwords: List[Password]) -> int:
    """
    For a list of passwords, count the number which meet their password policy.
    :param passwords:
    :return: Count of valid passwords
    """
    valid_passwords = list(filter(
        lambda password: password.validate(),
        passwords
    ))
    return len(valid_passwords)


def load_input_new_format(filepath: Path) -> List[Password]:
    """
    Load a filepath to a list of passwords including updated-format
    password policies.
    :param filepath: File location
    :return: List of passwords
    """
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
