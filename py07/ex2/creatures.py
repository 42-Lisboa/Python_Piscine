#! /usr/bin/env python3

from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import HealCapability, TransformCapability


# ============================== Abstract Class ===============================
#   Abstract class is like a contract with the major skeleton for sub classes
# -----------------------------------------------------------------------------

# Abstract Strategy
# -----------------------------------------------------------------------------

class BattleStrategy(ABC):
    # check if creature can use the selected strategy
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    # command creature to act in the arena
    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...


# ============================= Concrete Classes ==============================
#         Concrete classes unlike the abstract ones can be instanciated
# -----------------------------------------------------------------------------

# Concrete Strategies
# -----------------------------------------------------------------------------

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        print(f"{creature.attack()}")


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if isinstance(creature, TransformCapability):
            print(f"{creature.transform()}")
            print(f"{creature.attack()}")
            print(f"{creature.revert()}")
        else:
            raise Exception(f"Invalid Creature '{creature.name}' for this "
                            f"{self.__class__.__name__}")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if isinstance(creature, HealCapability):
            print(f"{creature.attack()}")
            print(f"{creature.heal()}")
        else:
            raise Exception(f"Invalid Creature {creature.name} for this "
                            f"{self.__class__.__name__}")
