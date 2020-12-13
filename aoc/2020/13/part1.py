from pathlib import Path
from typing import Iterable, Set, Tuple

def calc_overshoot(target:int, multiple: int) -> int:
    undershoot = target % multiple
    overshoot = multiple - undershoot
    return overshoot

def calc_earliest_bus(target: int, ids: Iterable[int]) -> Tuple[int, int]:
    overshoots = [(id, calc_overshoot(target, id)) for id in ids]
    min_id, min_overshoot = min(overshoots, key=lambda t: t[1])
    return min_id, target + min_overshoot

def load_input(filepath: Path) -> Tuple[int, Set[int]]:
    with filepath.open() as f:
        target = int(f.readline())
        buses = set((int(id) for id in f.readline().split(",") if id != "x"))
    return (target, buses)

if __name__ == "__main__":
    filepath = Path(__file__).parent / "input.txt"
    target, buses = load_input(filepath)
    bus, time = calc_earliest_bus(target, buses)
    print(bus, time, bus * (time - target))
