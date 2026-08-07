
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    input_ingredients = ingredients.lower().split(", ")
    allowed_ingredients = dark_spell_allowed_ingredients()
    for item in input_ingredients:
        if item in allowed_ingredients:
            return (f"VALID ingredients: {ingredients.title()}\n")
    else:
        return (f"INVALID ingredients: {ingredients.title()}\n")
