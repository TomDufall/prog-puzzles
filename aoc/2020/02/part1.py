from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class PasswordPolicy:
    min_count: int
    max_count: int
    character: str

    def match(self, password: str) -> bool:
        """
        Check if the given password matches the policy.
        A password matches if it contains between self.min_count and
        self.match_count (inclusive) occurrences of self.character.
        :param password: Password to test
        :return: Whether or not the password is valid
        """
        count = password.count(self.character)
        return self.min_count <= count <= self.max_count


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


def load_input(filepath: Path) -> List[Password]:
    """
    Load a filepath to a list of passwords including password policies.
    :param filepath: File location
    :return: List of passwords
    """
    passwords: List[Password] = []
    for line in filepath.read_text().splitlines():
        policy_str, password = line.split(": ")
        min_count, policy_str = policy_str.split("-")
        max_count, character = policy_str.split(" ")
        policy = PasswordPolicy(int(min_count), int(max_count), character)
        passwords.append(Password(policy, password))
    return passwords


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    input_ = load_input(filepath)
    print(count_valid_passwords(input_))
