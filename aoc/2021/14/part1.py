from __future__ import annotations

from typing import DefaultDict


def _step(template: list[str], recipes: dict[tuple[str, str], str]) -> list[str]:
    last = template[0]
    new_template = [last]
    for item in template[1:]:
        pair = (last, item)
        if pair in recipes:
            new_template.append(recipes[pair])
        new_template.append(item)
        last = item
    return new_template


def step(
    template: list[str], recipes: dict[tuple[str, str], str], steps: int
) -> list[str]:
    for _ in range(steps):
        template = _step(template, recipes)
    return template


def frequencies(items: list[str]) -> dict[str, int]:
    d: dict[str, int] = DefaultDict(lambda: 0)
    for item in items:
        d[item] += 1
    return d


def load_input(
    filepath: str = "input.txt",
) -> tuple[list[str], dict[tuple[str, str], str]]:
    with open(filepath) as f:
        template_str, lines = f.read().split("\n\n")
    template = list(template_str)
    recipes = {}
    for line in lines.splitlines():
        input_str, _, output = line.split(" ")
        recipes[tuple(input_str)] = output
    return template, recipes


if __name__ == "__main__":
    template, recipes = load_input()
    output = step(template, recipes, 10)
    freqs = frequencies(output)
    answer = max(freqs.values()) - min(freqs.values())
    print(answer)
