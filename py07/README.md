# 🃏 py07 — DataDeck

<p align="left">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Grade-100%2F100-brightgreen?style=for-the-badge" />
</p>

> Abstract Card Architecture. Builds on Python OOP foundations to apply three classic design patterns — Abstract Factory, Mixin/Capability, and Strategy — through a modular creature card game system structured as Python packages.

---

## 📋 Summary

- [Exercises](#exercises)
- [Architecture](#architecture)
- [Key Techniques](#key-techniques)
- [General Rules](#general-rules)
- [Concepts Learned](#concepts-learned)
- [Resources](#resources)

---

<a name="exercises"></a>
<details open><summary><h2>📂 Exercises</h2></summary>

| # | Package | Test Script | Description |
|---|---------|-------------|-------------|
| 00 | `ex0/` | `battle.py` | **Abstract Factory** — `Creature` ABC + `FlameFactory` and `AquaFactory`; base and evolved creatures per family |
| 01 | `ex1/` | `capacitor.py` | **Capabilities / Mixins** — `HealCapability` and `TransformCapability` ABCs; multiple inheritance with `Sproutling`, `Bloomelle`, `Shiftling`, `Morphagon` |
| 02 | `ex2/` | `tournament.py` | **Strategy Pattern** — `BattleStrategy` ABC + `NormalStrategy`, `AggressiveStrategy`, `DefensiveStrategy`; round-robin tournament |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="architecture"></a>
<details open><summary><h2>🗺 Architecture</h2></summary>

```
repo root/
├── battle.py         ← tests ex0 package
├── capacitor.py      ← tests ex1 package
├── tournament.py     ← tests ex2 package
├── ex0/
│   ├── __init__.py   ← exposes only factories (not concrete creatures)
│   └── creatures.py  ← Creature ABC, Flameling, Pyrodon, Aquabub, Torragon,
│                        FlameFactory, AquaFactory
├── ex1/
│   ├── __init__.py   ← exposes only factories and capability ABCs
│   └── creatures.py  ← ex0 + HealCapability, TransformCapability,
│                        Sproutling, Bloomelle, Shiftling, Morphagon,
│                        HealingCreatureFactory, TransformCreatureFactory
└── ex2/
    ├── __init__.py   ← exposes factories, strategies, and ABCs
    └── creatures.py  ← ex1 + BattleStrategy, NormalStrategy,
                         AggressiveStrategy, DefensiveStrategy
```

> Each package only exposes **factories** — concrete creature classes are never imported directly by test scripts.

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="key-techniques"></a>
<details open><summary><h2>🛠 Key Techniques</h2></summary>

- **Abstract Factory pattern** — `CreatureFactory` ABC with `create_base()` and `create_evolved()`; each concrete factory encapsulates a creature family (ex00)
- **`@abstractmethod`** — enforces `attack()` on all `Creature` subclasses and `act()`/`is_valid()` on all strategies (ex00, ex02)
- **Multiple inheritance** — `Sproutling(Creature, HealCapability)` and `Shiftling(Creature, TransformCapability)` combine two independent ABCs (ex01)
- **Capability / Mixin ABCs** — `HealCapability` and `TransformCapability` are standalone ABCs with no dependency on `Creature`, keeping them reusable (ex01)
- **`isinstance()` checks** — used in test scripts and strategies to safely branch on runtime type (`isinstance(creature, TransformCapability)`) (ex01, ex02)
- **Strategy pattern** — `BattleStrategy` ABC decouples the tournament logic from creature-specific behavior; each strategy knows what it requires via `is_valid()` (ex02)
- **Exception handling in strategies** — `AggressiveStrategy.act()` and `DefensiveStrategy.act()` raise a descriptive exception when given an incompatible creature; `tournament.py` catches it with `try/except/finally` (ex02)
- **Python packages** — each exercise is a proper package with `__init__.py` controlling public API surface; test scripts import only from the package, not from internal modules (ex00–ex02)
- **`super().__init__()`** — used correctly in all multiple-inheritance chains to ensure MRO is respected (ex01)
- **Type hints** — all methods fully annotated; `mypy`-compatible throughout

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="general-rules"></a>
<details open><summary><h2>📐 General Rules</h2></summary>

- Python **3.10+** required
- Code must pass **`flake8`** linter standards
- All code must include comprehensive **type annotations** — checked with `mypy`
- Each exercise is a **Python package** — a `__init__.py` is mandatory inside each `ex*/` folder
- Test scripts (`battle.py`, `capacitor.py`, `tournament.py`) live at the **repo root**
- Packages must only **expose factories** — concrete creature classes are not part of the public API
- Authorized imports: **`abc`** and **`typing`** only; no external libraries
- `eval()` and `exec()` are forbidden

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="concepts-learned"></a>
<details open><summary><h2>📚 Concepts Learned</h2></summary>

- The **Abstract Factory pattern** — a factory that produces families of related objects without exposing their concrete classes
- Why **packages with controlled `__init__.py`** enforce encapsulation at the module level, the same way `private` does in other languages
- How **multiple inheritance** enables Mixins/Capabilities — adding orthogonal behavior to a class without polluting its main hierarchy
- The **Strategy pattern** — separating *what an object does* from *how it does it*, making behavior swappable at runtime
- How `is_valid()` and `act()` together form a **guard + command** interface that keeps the tournament loop clean and strategy-agnostic
- Why **`try/except/finally`** in `tournament.py` is the right place to handle strategy mismatches — the tournament continues cleanly even when a battle aborts
- The difference between **design-time contracts** (ABCs) and **runtime checks** (`isinstance`) — and when each is appropriate

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="resources"></a>
<details open><summary><h2>🔗 Resources</h2></summary>

| Title | Author | Description |
|-------|--------|-------------|
| [Python Abstract Factory Pattern Explained \| Object Creation Made Easy](https://youtu.be/Uwci2zPgiLY?si=SO6UDJnJvZNS-B_o) | [campbelltech](https://www.youtube.com/@campbelltech) | Clear walkthrough of the Abstract Factory pattern in Python — how to define factory interfaces and use them to create families of related objects without coupling to concrete classes. |
| [Python Mixins Explained in 3 Min \*Must-Know!\*](https://www.youtube.com/watch?v=GhUfsGyxOTU) | [Coding with David](https://www.youtube.com/@codingwith_david) | Quick and practical introduction to Mixins in Python — how to use multiple inheritance to add reusable capabilities to a class without modifying its main hierarchy. |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<p align="left">
  Developed by <a href="https://github.com/jalves-de">Jonathan Alves</a>
</p>
