from pathlib import Path
from typing import Dict, List, NamedTuple, Set, Tuple

from toolz import concat, frequencies


class FoodEntry(NamedTuple):
    ingredients: Set[str]
    allergens: Set[str]


def find_allergen_candidates(foods: List[FoodEntry]) -> Dict[str, Set[str]]:
    # Return dict of allergen: Set[candidate ingredients]
    allergen_candidates = {}
    for food in foods:
        allergens = food.allergens
        for allergen in allergens:
            if allergen not in allergen_candidates:
                allergen_candidates[allergen] = food.ingredients
            else:
                allergen_candidates[allergen] = allergen_candidates[allergen].intersection(food.ingredients)
    return allergen_candidates


def find_non_allergens(foods: List[FoodEntry]) -> Set[str]:
    allergen_candidates = find_allergen_candidates(foods)
    all_ingredients = set(concat(map(lambda x: x.ingredients, foods)))
    return all_ingredients - set(concat(allergen_candidates.values()))


def count_ingredient_occurances(foods: List[FoodEntry], ingredients: List[str]) -> int:
    freqs = frequencies(concat(map(lambda x: x.ingredients, foods)))
    return sum((count for ingredient, count in freqs.items() if ingredient in ingredients))


def load_input(filepath: Path) -> List[FoodEntry]:
    def split_line(line: str) -> Tuple[Set[str], Set[str]]:
        ingredients_list, allergens_list = line.split(" (contains ")
        ingredients = set(ingredients_list.split())
        allergens = set(allergens_list[:-1].split(", "))
        return FoodEntry(ingredients, allergens)
    return [
        split_line(line)
        for line in filepath.read_text().splitlines()
    ]


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
    allergen_candidates = find_allergen_candidates(strs)
    non_allergens = find_non_allergens(strs)
    occurances = count_ingredient_occurances(strs, non_allergens)
    end = datetime.now()
    time = (end - start).total_seconds()
    print(time)
    print(allergen_candidates)
    print(non_allergens)
    print(occurances)
