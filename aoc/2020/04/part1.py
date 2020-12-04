from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


SHORT_TO_LONG = {
    "byr": "birth_year",
    "iyr": "issue_year",
    "eyr": "expiration_year",
    "hgt": "height",
    "hcl": "hair_colour",
    "ecl": "eye_colour",
    "pid": "passport_id",
    "cid": "country_id",
}
LONG_TO_SHORT = {val: key for key,val in SHORT_TO_LONG.items()}


@dataclass
class Passport:
    birth_year: str
    issue_year: str
    expiration_year: str
    height: str
    hair_colour: str
    eye_colour: str
    passport_id: str
    country_id: str


@dataclass
class NorthPoleId(Passport):
    country_id: str = "NorthPole"


@dataclass
class PassportList:
    passports: Passport

    @staticmethod
    def from_batch(filepath: Path) -> PassportList:
        entries = filepath.read_text().split("\n\n")
        passports = []
        field_pattern = r"[\S^:]+:[\S^:]+" # key:value
        for entry in entries:
            field_strings = re.findall(field_pattern,entry)
            fields = {
                SHORT_TO_LONG[key]: value
                for key, value
                in map(lambda x: x.split(":"), field_strings)
            }
            try:
                passports.append(Passport(**fields))
            except TypeError as e:
                if str(e) == "__init__() missing 1 required positional argument: 'country_id'":
                    # I'm sure they won't mind, I am fixing their system, after all
                    passports.append(NorthPoleId(**fields))
                else:
                    # Invalid passport, ignore
                    pass
        return PassportList(passports)

    def to_batch(self, filepath: Path) -> None:
        pass


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    passports = PassportList.from_batch(filepath)
    print(len(passports.passports))
