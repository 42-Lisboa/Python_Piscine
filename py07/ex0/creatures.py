#! /usr/bin/env python3

from abc import ABC, abstractmethod


# ============================== Abstract Class ===============================
#   Abstract class is like a contract with the major skeleton for sub classes
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
