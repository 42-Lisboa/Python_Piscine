from .elements import create_air
from .potions import healing_potion, strength_potion
from .transmutation import lead_to_gold


heal = healing_potion
__all__ = [
    "create_air",
    "heal",
    "strength_potion",
    "lead_to_gold"
    ]
# __all__ defines which attributes is included when import * is called
