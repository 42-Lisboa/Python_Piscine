from elements import create_fire  # Absolute import
from ..elements import create_air  # Relative import
from ..potions import strength_potion  # Relative import


def lead_to_gold() -> str:
    return (f"🪙  Recipe transmuting Lead to Gold 🪙: \n"
            f"Brew [{create_air()}] and [{strength_potion()}]"
            f" mixed with [{create_fire()}]")


# Alchemist's Note on Pathways:
"""
This module demonstrates the perfect balance between absolute and relative
imports. Relative pathways (like '..elements') are used to gather ingredients
from within our own 'alchemy' package, keeping our internal structure modular,
self-contained, and safe to rename or move. However, to pull the Fire element
from outside the package (the project root) and sub-package (transmutation)
environment, we must use an absolute pathway ('elements'), because Python
strictly forbids relative imports from escaping the top-level package boundary.
"""
