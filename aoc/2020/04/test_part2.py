import pytest

from part2 import Passport


class TestPassport:
    def test_init_success(self):
        fields = {
            "birth_year": "1980",
            "issue_year": "2012",
            "expiration_year": "2030",
            "height": "74in",
            "hair_colour": "#623a2f",
            "eye_colour": "grn",
            "passport_id": "087499704",
            "country_id": "129",
        }
        Passport(**fields)

    def test_init_fail(self):
        fields = {
            "birth_year": "1926",
            "issue_year": "2018",
            "expiration_year": "1972",  # expired
            "height": "170",  # no units
            "hair_colour": "#18171d",
            "eye_colour": "amb",
            "passport_id": "186cm",  # invalid format
            "country_id": "100",
        }
        with pytest.raises(Exception):
            Passport(**fields)
