from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re
from typing import Dict, Set

# Type alias to make type hints more obvious
BagType = str


@dataclass
class BagNetwork:
    """
    Records what colour and quantity of bags each bag must contain.
    Also contains a reverse link of what bags each bag can be held in.
    """
    must_contain: Dict[BagType, Dict[BagType, int]] = field(default_factory=dict)
    contained_by: Dict[BagType, Set[BagType]] = field(default_factory=dict)

    @staticmethod
    def from_file(filepath: Path) -> BagNetwork:
        bag_network = BagNetwork()
        req_list = filepath.read_text().splitlines()
        for req in req_list:
            # format = <outer> bags contain {quantity <inner> bag(s)}.
            outer, inners_str = req.split(" bags contain ")
            if inners_str == "no other bags.":
                bag_network.add(outer, None, 0)
            else:
                bags_pattern = r"(\d+.+?) bag"
                matches = re.findall(bags_pattern, inners_str)
                for inner in matches:
                    quantity, colour = inner.split(" ", 1)
                    bag_network.add(outer, colour, int(quantity))
        return bag_network

    def add(self, outer: BagType, inner: BagType, quantity: int) -> None:
        """
        Add a requirement to the network
        """
        if self.must_contain.get(outer) is None:
            self.must_contain[outer] = {}
        if inner:
            self.must_contain[outer][inner] = quantity
        if self.contained_by.get(inner) is None:
            self.contained_by[inner] = set()
        self.contained_by[inner].add(outer)

    def remove(self, outer: BagType, inner: BagType) -> None:
        """
        Remove a requirement from the network
        """
        raise NotImplementedError

    def count_can_contain_all(self, inner: BagType) -> int:
        """
        Return a count of how many bag types can contain the given bag
        directly or indirectly.
        """
        can_contain = self.contained_by.get(inner, set()).copy()
        to_check = self.contained_by.get(inner, set()).copy()
        checked = {inner}
        while to_check:
            item = to_check.pop()
            if item in checked:
                continue
            else:
                can_contain.update(self.contained_by.get(item, set()))
                to_check.update(self.contained_by.get(item, set()))
                checked.add(item)
        return len(can_contain)


if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    network = BagNetwork.from_file(filepath)
    print(network.count_can_contain_all("shiny gold"))
