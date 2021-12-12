from __future__ import annotations

from collections import defaultdict
from typing import DefaultDict


def find_routes(
    paths: dict[str, set[str]], current: str = None, visited: list = None
) -> list[list[str]]:
    routes = []
    if visited is None:
        visited = []
    else:
        visited = visited.copy()
    if current is None:
        current = "start"
        visited.append("start")

    for option in paths[current]:
        if option == "end":
            new_visited = visited.copy()
            new_visited.append("end")
            routes.append(new_visited)
        elif option == "start":
            continue
        elif option == option.lower() and option in visited:
            continue
        else:
            new_visited = visited.copy()
            new_visited.append(option)
            routes.extend(find_routes(paths, option, new_visited))

    return routes


def load_input(filepath: str = "input.txt") -> dict[str, set[str]]:
    """
    Load input file and return a bi-directional dictionary of paths
    """
    paths: DefaultDict[str, set[str]] = defaultdict(lambda: set())
    with open(filepath) as f:
        for line in f.read().splitlines():
            start, end = line.split("-")
            paths[start].add(end)
            paths[end].add(start)
    return dict(paths)


if __name__ == "__main__":
    map_ = load_input()
    routes = find_routes(map_)
    print(len(routes))
