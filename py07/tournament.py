#! /usr/bin/env python3

from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, \
    DefensiveStrategy, BattleStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print(">> Tournament Starts <<")
    print(f"{len(opponents)} opponents involved")

    # Comprehension list of tuples with all instantiated creatures
    fighters = [(factory.create_base(), strat) for factory, strat in opponents]
    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            creature1, strategy1 = fighters[i]
            creature2, strategy2 = fighters[j]
            print("\n----------------------------------------------")
            print("* Battle *")
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" 💥 FIIIIIIIIIGHT! 💥")
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except Exception as e:
                print(f"❌ Battle error, aborting tournament: {e}")
            finally:
                print("----------------------------------------------")


def main() -> None:
    norm = NormalStrategy()
    aggress = AggressiveStrategy()
    defen = DefensiveStrategy()

    print("\n🧾 TOURNAMENT 0 (basic) 🧾")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(FlameFactory(), norm),
            (HealingCreatureFactory(), defen)])

    print("\n🧾 TOURNAMENT 1 (error) 🧾")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(FlameFactory(), aggress),
            (HealingCreatureFactory(), defen)])

    print("\n🧾 TOURNAMENT 2 (multiple) 🧾")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(AquaFactory(), norm),
            (HealingCreatureFactory(), defen),
            (TransformCreatureFactory(), aggress)])


if __name__ == "__main__":
    main()
