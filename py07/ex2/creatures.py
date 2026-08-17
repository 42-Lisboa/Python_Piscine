#! /usr/bin/env python3

from abc import ABC, abstractmethod


# ============================== Abstract Class ===============================
#   Abstract class is like a contract with the major skeleton for sub classes
# -----------------------------------------------------------------------------

# Abstract Creatures
# -----------------------------------------------------------------------------

class Creature(ABC):
    def __init__(self, name: str, element_type: str):
        self.name = name
        self.element_type = element_type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return (f"{self.name} is a {self.element_type} type creature")


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self, name: str = "") -> Creature:
        ...

    @abstractmethod
    def create_evolved(self, name: str = "") -> Creature:
        ...


# Abstract Capabilities
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

# Concrete Creatures
# -----------------------------------------------------------------------------

class Flameling(Creature):
    def __init__(self, name: str = "Flameling"):
        super().__init__(name=name, element_type="Fire")

    def attack(self) -> str:
        return (f"{self.name} uses Ember ☄️ !")


class Pyrodon(Creature):
    def __init__(self, name: str = "Pyrodon"):
        super().__init__(name=name, element_type="Fire")

    def attack(self) -> str:
        return (f"{self.name} uses Flash Bomb 💥 !")


class Aquabub(Creature):
    def __init__(self, name: str = "Aquabub"):
        super().__init__(name=name, element_type="Water")

    def attack(self) -> str:
        return (f"{self.name} uses Water Gun 🔫 !")


class Torragon(Creature):
    def __init__(self, name: str = "Torragon"):
        super().__init__(name=name, element_type="Water")

    def attack(self) -> str:
        return (f"{self.name} uses Bubbles Trap 🫧 !")


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

class FlameFactory(CreatureFactory):
    def create_base(self, name: str = "") -> Creature:
        if name:
            return Flameling(name=name)
        return Flameling()

    def create_evolved(self, name: str = "") -> Creature:
        if name:
            return Pyrodon(name=name)
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self, name: str = "") -> Creature:
        if name:
            return Aquabub(name=name)
        return Aquabub()

    def create_evolved(self, name: str = "") -> Creature:
        if name:
            return Torragon(name=name)
        return Torragon()


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
