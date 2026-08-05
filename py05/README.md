# 🔮 py05 — Code Nexus

<p align="left">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Grade-100%2F100-brightgreen?style=for-the-badge" />
</p>

> Polymorphic Data Streams in the Digital Matrix. Builds on py01's OOP foundations to master abstract classes, method overriding, subtype polymorphism, and duck typing — all applied to a complete data processing pipeline.

---

## 📋 Summary

- [Exercises](#exercises)
- [Key Techniques](#key-techniques)
- [General Rules](#general-rules)
- [Concepts Learned](#concepts-learned)
- [Resources](#resources)

---

<a name="exercises"></a>
<details open><summary><h2>📂 Exercises</h2></summary>

| # | File | Description |
|---|------|-------------|
| 00 | `data_processor.py` | Abstract base class `DataProcessor` + three concrete subclasses: `NumericProcessor`, `TextProcessor`, `LogProcessor` |
| 01 | `data_stream.py` | `DataStream` class routes mixed-type streams to the correct registered processor using polymorphic dispatch |
| 02 | `data_pipeline.py` | Full pipeline — adds `ExportPlugin` via `Protocol` (duck typing) with CSV and JSON export plugins |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="key-techniques"></a>
<details open><summary><h2>🛠 Key Techniques</h2></summary>

- **`ABC` / `ABCMeta`** — `from abc import ABC, abstractmethod`; define abstract base classes that cannot be instantiated directly (ex00)
- **`@abstractmethod`** — decorator that forces every subclass to implement `validate()` and `ingest()` (ex00)
- **Method overriding** — each subclass provides its own `validate()` and `ingest()` while sharing `output()` from the parent (ex00)
- **`typing.Any`** — used in the abstract `validate(self, data: Any) -> bool` signature to accept any input type (ex00)
- **Subtype polymorphism** — `DataStream.process_stream()` calls `validate()` on each registered processor without knowing its concrete type (ex01)
- **`register_processor()`** — open/closed design: add new processors without modifying `DataStream` (ex01)
- **`Protocol`** — `from typing import Protocol`; defines a structural interface (`ExportPlugin`) for duck typing — no inheritance required (ex02)
- **Duck typing** — `CsvExportPlugin` and `JsonExportPlugin` are compatible with `ExportPlugin` simply by implementing `process_output()` (ex02)
- **`tuple[int, str]`** — typed return value of `output()`, used as the exchange format between processors and export plugins (ex02)
- **`import abc`, `import typing`** — only authorized imports throughout the module

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="general-rules"></a>
<details open><summary><h2>📐 General Rules</h2></summary>

- Python **3.10+** required
- Code must pass **`flake8`** linter standards
- All code must include comprehensive **type annotations** — checked with `mypy`
- Each exercise in its own file and directory (`ex0/` through `ex2/`)
- Authorized imports: **`abc`** and **`typing`** only
- All built-in functions and standard collections are authorized
- Handle exceptions to prevent data stream corruption — programs must **never crash**
- Each exercise builds on the previous — the architecture evolves progressively across all three files

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="concepts-learned"></a>
<details open><summary><h2>📚 Concepts Learned</h2></summary>

- The difference between **abstract classes** and **concrete classes** — and why you can't instantiate an ABC directly
- How `@abstractmethod` enforces a **contract** that all subclasses must honour
- The distinction between **method overriding** (changing behavior) and **method inheritance** (reusing behavior)
- **Subtype polymorphism** — writing code against a base type that works correctly for all subtypes (Liskov Substitution Principle)
- **Duck typing vs inheritance** — `Protocol` lets unrelated classes be compatible without sharing a common ancestor
- Why a **plugin system** based on `Protocol` is more flexible than a strict inheritance hierarchy
- How to design a system that is **open for extension** (add a new processor or export plugin) without modifying existing code

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="resources"></a>
<details open><summary><h2>🔗 Resources</h2></summary>

| Title | Author | Description |
|-------|--------|-------------|
| [Classes Abstratas em Python](https://youtube.com/shorts/a1MH_tc3OOk?si=5isBQrPA4TtF801r) | YouTube Short | Quick visual introduction to abstract classes and `@abstractmethod` in Python — when and why to use them. |
| [Classe Abstrata x Interface](https://pt.stackoverflow.com/questions/3603/classe-abstrata-x-interface) | Stack Overflow PT | Community discussion comparing abstract classes and interfaces in Python, covering `ABC`, `Protocol`, and duck typing. |
| [Protocol vs Abstract Base Class (ABC) em Python + SOLID Principles](https://www.youtube.com/watch?v=-pO-iwM2wBE&t=243s) | [Otávio Miranda](https://www.youtube.com/@otaviomiranda) | Covers the practical differences between `Protocol` and `ABC` in Python, when to choose each, and how they connect to the SOLID principles. |
| [Princípio da Substituição de Liskov](https://pt.wikipedia.org/wiki/Princ%C3%ADpio_da_substitui%C3%A7%C3%A3o_de_Liskov) | Wikipedia PT | Formal definition and explanation of the Liskov Substitution Principle — the theoretical foundation behind correct subtype polymorphism. |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<p align="left">
  Developed by <a href="https://github.com/jalves-de">Jonathan Alves</a>
</p>