# 🎮 py03 — Mastering Python Collections

<p align="left">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Grade-100%2F100-brightgreen?style=for-the-badge" />
</p>

> Data Engineering for Game Analytics. This module introduces Python's core collection types—lists, tuples, sets, dictionaries, generators, and comprehensions—while building efficient data processing systems inspired by game development. :contentReference[oaicite:0]{index=0}

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
| 00 | `ft_command_quest.py` | Command-line arguments (`sys.argv`) and basic list manipulation |
| 01 | `ft_score_analytics.py` | Lists, data validation, statistics, and exception handling |
| 02 | `ft_coordinate_system.py` | Tuples, user input validation, and 3D distance calculations |
| 03 | `ft_achievement_tracker.py` | Sets, uniqueness, unions, intersections, and differences |
| 04 | `ft_inventory_system.py` | Dictionaries, inventory management, and key/value operations |
| 05 | `ft_data_stream.py` | Generators, `yield`, lazy evaluation, and event streams |
| 06 | `ft_data_alchemist.py` | List and dictionary comprehensions for efficient data transformation |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="key-techniques"></a>
<details open><summary><h2>🛠 Key Techniques</h2></summary>

- **Lists (`list`)** — ordered, mutable collections for storing and processing data (ex00, ex01)
- **Command-line arguments (`sys.argv`)** — processing external program input (ex00, ex01, ex04)
- **List statistics** — `sum()`, `max()`, `min()`, averages, and ranges (ex01)
- **Tuples (`tuple`)** — immutable structures for fixed datasets such as coordinates (ex02)
- **Sets (`set`)** — unique collections supporting unions, intersections, and differences (ex03)
- **Dictionaries (`dict`)** — key-value mappings for structured data storage (ex04)
- **Dictionary methods** — `.keys()`, `.values()`, `.update()` and iteration (ex04)
- **Generators (`yield`)** — lazy data generation with minimal memory usage (ex05)
- **`next()`** — manual generator iteration (ex05)
- **List comprehensions** — concise filtering and transformations (ex06)
- **Dictionary comprehensions** — efficient dictionary creation and filtering (ex06)
- **Collection processing** — choosing the right data structure for performance and readability
- **Type hints** — fully compatible with `mypy`
- **`flake8`** — PEP8 style enforced throughout the project

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="general-rules"></a>
<details open><summary><h2>📐 General Rules</h2></summary>

- Python **3.10+** required
- Code must pass **`flake8`** linting
- All functions and methods must include **type hints** validated with `mypy`
- Each exercise must be implemented in its own directory (`ex0/` through `ex6/`)
- Programs should **gracefully handle invalid input** whenever applicable
- **No file I/O** — all processing must occur in memory or through command-line arguments
- Demonstrate both **basic operations** and **advanced collection techniques**
- Use the appropriate collection type (`list`, `tuple`, `set`, `dict`) according to its strengths

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="concepts-learned"></a>
<details open><summary><h2>📚 Concepts Learned</h2></summary>

- How to select the appropriate Python collection based on the problem being solved
- The differences between **mutable** and **immutable** data structures
- Why **sets** provide efficient uniqueness checks and mathematical operations
- How **dictionaries** enable fast key-based lookups and structured storage
- How **generators** drastically reduce memory consumption through lazy evaluation
- How **comprehensions** make data transformation cleaner, faster, and more Pythonic
- Best practices for processing collections while maintaining readable and efficient code
- Why choosing the correct data structure directly impacts performance and scalability

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="resources"></a>
<details open><summary><h2>🔗 Resources</h2></summary>

| Title | Author | Description |
|-------|--------|-------------|
| [Dicas de Fatiamento ou Slicing](https://www.youtube.com/watch?v=kw88FTqG8Wo) | [HashLDash](https://www.youtube.com/@11Wills11) | Practical guide to Python slicing, covering strings, lists, step values, negative indexing, and common use cases. |
| [Python Lists, Sets, and Tuples Explained](https://www.youtube.com/watch?v=gOMW_n2-2Mw) | [Bro Code](https://www.youtube.com/@BroCodez) | Clear explanation of Python's primary collection types, including their characteristics, performance, and when to use each one. |
| [List Comprehensions como você nunca viu!](https://www.youtube.com/watch?v=O6vyUeDteRA) | [HashLDash](https://www.youtube.com/@11Wills11) | Deep dive into list comprehensions, demonstrating filtering, transformations, nested comprehensions, and Pythonic coding techniques. |
| [Geradores em Python: Como usar Yield para economizar memória e processamento](https://www.youtube.com/watch?v=YQAe1Z_R5RE) | [Programador Aventureiro](https://www.youtube.com/@ProgramadorAventureiro) | Explains generators and the `yield` keyword, showing how lazy evaluation improves performance and memory efficiency. |
| [Built-in Types — Python Documentation](https://docs.python.org/3/library/stdtypes.html) | [Python.org](https://docs.python.org) | Official documentation covering lists, tuples, sets, dictionaries, strings, and their methods. |
| [Data Structures — Python Tutorial](https://docs.python.org/3/tutorial/datastructures.html) | [Python.org](https://docs.python.org) | Official Python tutorial on lists, comprehensions, dictionaries, tuples, sets, looping techniques, and best practices. |
| [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html) | [Python.org](https://docs.python.org) | Official guide covering generators, iterators, lazy evaluation, and functional programming concepts in Python. |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<p align="left">
  Developed by <a href="https://github.com/jalves-de">Jonathan Alves</a>
</p>