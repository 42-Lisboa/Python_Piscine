
from .light_spellbook import light_spell_allowed_ingredients
# 2nd import option
# from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    input_ingredients = ingredients.lower().split(", ")
    allowed_ingredients = light_spell_allowed_ingredients()
    # allowed_ingredients = light_spellbook.light_spell_allowed_ingredients()
    for item in input_ingredients:
        if item in allowed_ingredients:
            return (f"VALID ingredients: {ingredients.title()}\n")
    else:
        return (f"INVALID ingredients: {ingredients.title()}\n")
