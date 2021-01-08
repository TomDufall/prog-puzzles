from pathlib import Path

from part1 import BagNetwork


class TestBagNetwork:
    def test_from_file_must_contain(self):
        filepath = Path(__file__).parent / "sample_input_1.txt"
        expected = {
            "light red": {
                "bright white": 1,
                "muted yellow": 2,
            },
            "dark orange": {
                "bright white": 3,
                "muted yellow": 4,
            },
            "bright white": {
                "shiny gold": 1,
            },
            "muted yellow": {
                "shiny gold": 2,
                "faded blue": 9,
            },
            "shiny gold": {
                "dark olive": 1,
                "vibrant plum": 2,
            },
            "dark olive": {
                "faded blue": 3,
                "dotted black": 4,
            },
            "vibrant plum": {
                "faded blue": 5,
                "dotted black": 6,
            },
            "faded blue": {},
            "dotted black": {},
        }
        bag_network = BagNetwork.from_file(filepath)
        assert bag_network.must_contain == expected

    def test_from_file_contained_by(self):
        filepath = Path(__file__).parent / "sample_input_1.txt"
        expected = {
            "bright white": {
                "light red", "dark orange",
            },
            "muted yellow": {
                "light red", "dark orange",
            },
            "shiny gold": {
                "bright white", "muted yellow",
            },
            "dark olive": {
                "shiny gold",
            },
            "vibrant plum": {
                "shiny gold",
            },
            "faded blue": {
                "muted yellow", "dark olive", "vibrant plum",
            },
            "dotted black": {
                "dark olive", "vibrant plum",
            },
            None: {
                "faded blue", "dotted black",
            }
        }
        bag_network = BagNetwork.from_file(filepath)
        assert bag_network.contained_by == expected

    def test_can_contain_all(self):
        filepath = Path(__file__).parent / "sample_input_1.txt"
        bag_network = BagNetwork.from_file(filepath)
        assert bag_network.count_can_contain_all("shiny gold") == 4
