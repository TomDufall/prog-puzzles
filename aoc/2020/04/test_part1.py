from pathlib import Path
import pytest

from part1 import NorthPoleId, Passport, PassportList


class TestPassport:
    def test_init_success(self):
        fields = {
            "birth_year": "1234",
            "issue_year": "2015",
            "expiration_year": "2025",
            "height": "182cm",
            "hair_colour": "#fffffd",
            "eye_colour": "gry",
            "passport_id": "123456789",
            "country_id": "uk",
        }
        Passport(**fields)

    def test_init_fail(self):
        fields = {
            "birth_year": "1234",
            "issue_year": "2015",
            "expiration_year": "2025",
            "height": "182cm",
            "hair_colour": "#fffffd",
            "eye_colour": "gry",
            "passport_id": "123456789",
            # no country_id
        }
        with pytest.raises(TypeError):
            Passport(**fields)


class TestNorthPoleId:
    def test_init_success(self):
        fields = {
            "birth_year": "1234",
            "issue_year": "2015",
            "expiration_year": "2025",
            "height": "182cm",
            "hair_colour": "#fffffd",
            "eye_colour": "gry",
            "passport_id": "123456789",
            # no country_id - not required
        }
        NorthPoleId(**fields)

    def test_init_fail(self):
        fields = {
            "birth_year": "1234",
            "issue_year": "2015",
            "expiration_year": "2025",
            # no height - required
            "hair_colour": "#fffffd",
            "eye_colour": "gry",
            "passport_id": "123456789",
            # no country_id - not required
        }
        with pytest.raises(TypeError):
            NorthPoleId(**fields)


class TestPassportList:
    def test_from_bath(self):
        filepath = Path(__file__).parent / "sample_input.txt"
        passports = PassportList.from_batch(filepath)
        assert len(passports.passports) == 2
        expected = [
            Passport(
                birth_year="1937",
                issue_year="2017",
                expiration_year="2020",
                height="183cm",
                hair_colour="#fffffd",
                eye_colour="gry",
                passport_id="860033327",
                country_id="147",
            ),
            NorthPoleId(
                birth_year="1931",
                issue_year="2013",
                expiration_year="2024",
                height="179cm",
                hair_colour="#ae17e1",
                eye_colour="brn",
                passport_id="760753108",
                country_id="NorthPole",
            ),
        ]
        assert passports.passports == expected
