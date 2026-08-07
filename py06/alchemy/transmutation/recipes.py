from elements import create_fire  # Absolute import
from ..elements import create_air  # Relative import
from ..potions import strength_potion  # Relative import


def lead_to_gold() -> str:
    return (f"🪙  Recipe transmuting Lead to Gold 🪙: \n"
            f"Brew [{create_air()}] and [{strength_potion()}]"
            f" mixed with [{create_fire()}]")
