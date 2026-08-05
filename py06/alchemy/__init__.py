from .elements import create_air, create_earth
from .potions import healing_potion, strength_potion


heal = healing_potion
__all__ = ["create_air", "create_earth", "heal", "strength_potion"]
# this variable define which attributes is included when import * is called
