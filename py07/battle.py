#! /usr/bin/env python3

from ex0 import FlameFactory, AquaFactory, CreatureFactory


flame_factory = FlameFactory()
aqua_factory = AquaFactory()


def test_factory(factory: CreatureFactory) -> None:
    print(f"\n>>>>>>>>> Testing {factory.__class__.__name__} <<<<<<<<<")
    creature_base = factory.create_base()
    creature_evolved = factory.create_evolved()
    print(f"{creature_base.describe()}")
    print(f"{creature_base.attack()}")
    print(f"{creature_evolved.describe()}")
    print(f"{creature_evolved.attack()}")


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("\n>>>>>>>>>>> Testing battle <<<<<<<<<<<<")
    creature_base1 = factory1.create_base("Charmander")
    creature_base2 = factory2.create_base("Squirtle")
    print(f"{creature_base1.describe()}")
    print("⚔️")
    print(f"{creature_base2.describe()}")
    print("\n💥 FIIIIIIIIIGHT! 💥\n")
    print(f"{creature_base1.attack()}")
    print(f"{creature_base2.attack()}")


if __name__ == "__main__":
    test_factory(flame_factory)
    test_factory(aqua_factory)
    battle(flame_factory, aqua_factory)
