
from .dark_validator import validate_ingredients
# This will generate an error for the circular dependancy


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:

    # Parse ingredients
    # ----------------------------------------------------------------
    if ',' not in ingredients:
        return ("❌ Error Parameter: ingredients must have at least "
                "two ingredients separated by ', '\n")

    # Check allowed ingredients
    # ----------------------------------------------------------------
    validation_str = validate_ingredients(ingredients)
    if "INVALID" in validation_str:
        return (f"❌ Spell ✨ {spell_name} ✨ not recorded - "
                f"{validation_str}")
    else:
        return (f"✔️  Spell ✨ {spell_name} ✨ recorded - "
                f"{validation_str}")
