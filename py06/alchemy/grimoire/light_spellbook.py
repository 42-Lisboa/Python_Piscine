# 2nd import option
# from . import light_validator

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:

    # Parse ingredients
    # ----------------------------------------------------------------
    if ',' not in ingredients:
        return ("❌ Error Parameter: ingredients must have at least "
                "two ingredients separated by ', '\n")

    # Check allowed ingredients
    # ----------------------------------------------------------------
    from .light_validator import validate_ingredients
    # python only reads this import when the function is called
    # breaking the circular dependancy

    validation_str = validate_ingredients(ingredients)
    # validation_str = light_validator.validate_ingredients(ingredients)
    if "INVALID" in validation_str:
        return (f"❌ Spell ✨ {spell_name} ✨ not recorded - "
                f"{validation_str}")
    else:
        return (f"✔️  Spell ✨ {spell_name} ✨ recorded - "
                f"{validation_str}")


"""
-----------------------------------------------------------------------
Circular import: light_spellbook <-> light_validator
-----------------------------------------------------------------------
Both modules need each other (spellbook calls validate_ingredients,
validator calls light_spell_allowed_ingredients), which creates a
cycle if both use imports at the top of their files.

Comparison of ways to solve it:

1) Lazy import (used here)
   How:         import inside the function, only runs when called
   Robustness:  Good
   Clarity:     import hidden inside the function
   When to use: quick fix, no redesign needed

2) Import the module, not the name
   How:         `from . import module`, then `module.function()`
   Robustness:  Medium
   Clarity:     slightly better
   When to use: when the cycle is "almost" resolvable, i.e. the
                attribute is accessed later, not at import time

3) Extract shared dependency
   How:         move shared data/logic to a separate module
                (e.g. constants.py) that both modules import from
   Robustness:  Best
   Clarity:     Best
   When to use: the real fix, breaks the cycle for good, usually
                the right long-term solution

4) Merge the modules
   How:         combine both files into one
   Robustness:  Best
   Clarity:     depends on the resulting file
   When to use: if the split never made sense in the first place
-----------------------------------------------------------------------
"""
