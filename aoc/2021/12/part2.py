from __future__ import annotations

from part1 import load_input


def find_routes(
    paths: dict[str, set[str]],
    current: str = None,
    visited: list = None,
    second_small_used: bool = False,
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
        elif second_small_used and option == option.lower() and option in visited:
            continue
        else:
            if option == option.lower() and option in visited:
                new_second_small_used = True
            else:
                new_second_small_used = second_small_used
            new_visited = visited.copy()
            new_visited.append(option)
            routes.extend(
                find_routes(paths, option, new_visited, new_second_small_used)
            )

    return routes


if __name__ == "__main__":
    map_ = load_input()
    routes = find_routes(map_)
    print(len(routes))
