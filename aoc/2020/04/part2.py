from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import List


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
LONG_TO_SHORT = {val: key for key, val in SHORT_TO_LONG.items()}

HAIR_REGEX = "#[0-9a-f]{6}"
VALID_EYE_COLOURS = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
PASSPORT_ID_REGEX = r"\d{9}"


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

    def __post_init__(self):
        if not self.validate():
            raise ValueError("Invalid passport")

    def validate(self) -> bool:
        """
        Check that the value of each field matches the field restrictions.
        :return: Whether validation is successful
        """
        if len(self.birth_year) != 4 or not 1920 <= int(self.birth_year) <= 2002:
            raise ValueError("Birth year out of bounds")
        elif len(self.issue_year) != 4 or not 2010 <= int(self.issue_year) <= 2020:
            raise ValueError("Issue year out of bounds")
        elif len(self.expiration_year) != 4 or not 2020 <= int(self.expiration_year) <= 2030:
            raise ValueError("Expiration year out of bounds")
        if self.height.endswith("cm"):
            if not 150 <= float(self.height[:-2]) <= 193:
                raise ValueError("Height out of bounds")
        elif self.height.endswith("in"):
            if not 59 <= float(self.height[:-2]) <= 76:
                raise ValueError("Height out of bounds")
        else:
            raise ValueError("Unrecognised height units")
        if not re.fullmatch(HAIR_REGEX, self.hair_colour):
            raise ValueError("Unrecognised hair colour")
        elif self.eye_colour not in VALID_EYE_COLOURS:
            raise ValueError("Eye colour not recognised")
        elif not re.fullmatch(PASSPORT_ID_REGEX, self.passport_id):
            raise ValueError("Passport ID invalid")
        return True


@dataclass
class NorthPoleId(Passport):
    country_id: str = "NorthPole"


@dataclass
class PassportList:
    passports: List[Passport]

    @staticmethod
    def from_batch(filepath: Path) -> PassportList:
        entries = filepath.read_text().split("\n\n")
        passports = []
        field_pattern = r"[\S^:]+:[\S^:]+"  # key:value
        for entry in entries:
            field_strings = re.findall(field_pattern, entry)
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
                    try:
                        passports.append(NorthPoleId(**fields))
                    except ValueError:
                        continue
            except ValueError:
                # Invalid passport, ignore
                continue
        return PassportList(passports)


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    passports = PassportList.from_batch(filepath)
    print(len(passports.passports))
