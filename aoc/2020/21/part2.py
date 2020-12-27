from pathlib import Path
from typing import Dict, List

from part1 import FoodEntry, find_allergen_candidates, load_input


def resolve_allergens(foods: List[FoodEntry]) -> Dict[str, str]:
    # return dict of {allergen: name}
    allergen_candidates = find_allergen_candidates(foods)
    answers = {}
    while allergen_candidates:
        updated = False
        for allergen, candidates in allergen_candidates.items():
            if len(candidates) == 0:
                raise ValueError("Allergen with no candidates")
            elif len(candidates) == 1:
                candidate = next(iter(candidates))
                answers[allergen] = candidate
                del allergen_candidates[allergen]
                for allergen_2 in allergen_candidates:
                    allergen_candidates[allergen_2].discard(candidate)
                updated = True
                break
        if not updated:
            raise NotImplementedError
    return answers


if __name__ == "__main__":
    SAMPLE_INPUT = [
        FoodEntry({"mxmxvkd", "kfcds", "sqjhc", "nhms"}, {"dairy", "fish"}),
        FoodEntry({"trh", "fvjkl", "sbzzf", "mxmxvkd"}, {"dairy"}),
        FoodEntry({"sqjhc", "fvjkl"}, {"soy"}),
        FoodEntry({"sqjhc", "mxmxvkd", "sbzzf"}, {"fish"}),
    ]

    from datetime import datetime
    start = datetime.now()
    filepath = Path(__file__).parent / "input.txt"
    strs = load_input(filepath)
    # strs = SAMPLE_INPUT
    allergens = resolve_allergens(strs)
    answer = ",".join(
        map(
            lambda x: x[1],
            sorted(list(allergens.items()), key=lambda x: x[0])
        )
    )
    end = datetime.now()
    time = (end - start).total_seconds()
    print(time)
    print(allergens)
    print(answer)
