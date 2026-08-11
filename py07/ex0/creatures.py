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
        return (f"{self.name} is a {self.element_type} type Creature")


# ============================= Concrete Classes ==============================
#         Concrete classes unlike the abstract ones can be instanciated
# -----------------------------------------------------------------------------

class Flameling(Creature):
    def __init__(self):
        super().__init__()

    def attack(self) -> str:
        return (f"{self.__class__.__name__} uses Ember ☄️ !")


class Pyrodon(Creature):
    def __init__(self):
        super().__init__()

    def attack(self) -> str:
        return (f"{self.__class__.__name__} uses Flash Bomb 💥 !")


class Aquabub(Creature):
    def __init__(self):
        super().__init__()

    def attack(self) -> str:
        return (f"{self.__class__.__name__} uses Water Gun 🔫 !")


class Torragon(Creature):
    def __init__(self):
        super().__init__()

    def attack(self) -> str:
        return (f"{self.__class__.__name__} uses Bubbles Trap 🫧 !")
