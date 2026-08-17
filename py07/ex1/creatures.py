#! /usr/bin/env python3

from abc import ABC, abstractmethod
from ex0 import Creature, CreatureFactory


# ============================== Abstract Class ===============================
#   Abstract class is like a contract with the major skeleton for sub classes
# -----------------------------------------------------------------------------

class HealCapability(ABC):  # also add methods in classes - Protocol/Mixins
    @abstractmethod
    def heal(self, target: str = "") -> str:
        ...


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...


# ============================= Concrete Classes ==============================
#         Concrete classes unlike the abstract ones can be instanciated
# -----------------------------------------------------------------------------

# Concrete Creatures with new Capabilities (Multiple Heritage)
# -----------------------------------------------------------------------------

class Sproutling(Creature, HealCapability):
    def __init__(self, name: str = "Sproutling"):
        super().__init__(name=name, element_type="Grass")

    def attack(self) -> str:
        return (f"{self.name} uses Vine Whip 🍃 !")

    def heal(self, target: str = "") -> str:
        if target:
            return (f"{self.name} heals {target} for a small amount 💫")
        return (f"{self.name} heals itself for a small amount 💫")


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str = "Bloomelle"):
        super().__init__(name=name, element_type="Grass/Fairy")

    def attack(self) -> str:
        return (f"{self.name} uses Petal Dance 🌹 !")

    def heal(self, target: str = "") -> str:
        if target:
            return (f"{self.name} heals {target} for a large amount 🌟")
        return (f"{self.name} heals itself and others for a large amount 🌟")


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str = "Shiftling"):
        super().__init__(name=name, element_type="Normal")
        self.is_transformed = False

    def attack(self) -> str:
        if self.is_transformed is True:
            return (f"{self.name} performs a boosted strike ⚡ !")
        return (f"{self.name} uses Power Punch 👊 !")

    def transform(self) -> str:
        if self.is_transformed is True:
            return (f"{self.name} it's already transformed!")
        self.is_transformed = True
        return (f"{self.name} shifts into a sharper form!")

    def revert(self) -> str:
        if self.is_transformed is False:
            return (f"{self.name} it's on normal evolution state!")
        self.is_transformed = False
        return (f"{self.name} returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str = "Morphagon"):
        super().__init__(name=name, element_type="Normal/Dragon")
        self.is_transformed = False

    def attack(self) -> str:
        if self.is_transformed is True:
            return (f"{self.name} unleashes a devastating morph strike 🐉 !")
        return (f"{self.name} uses Dragon Tail 🦎 !")

    def transform(self) -> str:
        if self.is_transformed is True:
            return (f"{self.name} it's already transformed!")
        self.is_transformed = True
        return (f"{self.name} morphs into a dragonic battle form!")

    def revert(self) -> str:
        if self.is_transformed is False:
            return (f"{self.name} it's on normal evolution state!")
        self.is_transformed = False
        return (f"{self.name} stabilizes its form.")


# Concrete Factories
# -----------------------------------------------------------------------------

class HealingCreatureFactory(CreatureFactory):
    def create_base(self, name: str = "") -> Creature:
        if name:
            return Sproutling(name=name)
        return Sproutling()

    def create_evolved(self, name: str = "") -> Creature:
        if name:
            return Bloomelle(name=name)
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self, name: str = "") -> Creature:
        if name:
            return Shiftling(name=name)
        return Shiftling()

    def create_evolved(self, name: str = "") -> Creature:
        if name:
            return Morphagon(name=name)
        return Morphagon()
