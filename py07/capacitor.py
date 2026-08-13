#! /usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory, \
    HealCapability, TransformCapability


heal_factory = HealingCreatureFactory()
transform_factory = TransformCreatureFactory()


def test_heal_factory(factory: HealingCreatureFactory) -> None:
    print(f"\n>>>>>>>>> Testing {factory.__class__.__name__} <<<<<<<<<")
    print(" Base:")
    creature_base = factory.create_base()
    print(f"{creature_base.describe()}")
    print(f"{creature_base.attack()}")
    if isinstance(creature_base, HealCapability):
        print(f"{creature_base.heal()}")
    print(" Evolved:")
    creature_evolved = factory.create_evolved()
    print(f"{creature_evolved.describe()}")
    print(f"{creature_evolved.attack()}")
    if isinstance(creature_evolved, HealCapability):
        print(f"{creature_evolved.heal()}")


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    print(f"\n>>>>>>>>> Testing {factory.__class__.__name__} <<<<<<<<<")
    print(" Base:")
    creature_base = factory.create_base()
    print(f"{creature_base.describe()}")
    print(f"{creature_base.attack()}")
    if isinstance(creature_base, TransformCapability):
        print(f"{creature_base.transform()}")
        print(f"{creature_base.attack()}")
        print(f"{creature_base.revert()}")
    print(" Evolved:")
    creature_evolved = factory.create_evolved()
    print(f"{creature_evolved.describe()}")
    print(f"{creature_evolved.attack()}")
    if isinstance(creature_evolved, TransformCapability):
        print(f"{creature_evolved.transform()}")
        print(f"{creature_evolved.attack()}")
        print(f"{creature_evolved.revert()}")


if __name__ == "__main__":
    test_heal_factory(heal_factory)
    test_transform_factory(transform_factory)
