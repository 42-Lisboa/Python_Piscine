# 🔮 py06 — The Codex: Mastering Python's Import Mysteries

<p align="left">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Grade-100%2F100-brightgreen?style=for-the-badge" />
</p>

> The Alchemist's Laboratory. Four sacred mysteries of Python imports: package initialization with `__init__.py`, calling code across nested modules, absolute vs relative import paths, and breaking (and triggering) circular dependencies.

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

### Part I — The Alembic

| # | File | Description |
|---|------|-------------|
| 00 | `ft_alembic_0.py` | `import elements` — direct access to root `elements.py`, calls `create_fire()` |
| 01 | `ft_alembic_1.py` | `from elements import ...` — direct access to root `elements.py`, calls `create_water()` |
| 02 | `ft_alembic_2.py` | `import alchemy.elements` — direct access to `alchemy/elements.py`, calls `create_earth()` |
| 03 | `ft_alembic_3.py` | `from alchemy.elements import ...` — direct access to `alchemy/elements.py`, calls `create_air()` |
| 04 | `ft_alembic_4.py` | `import alchemy` — package-level access via `alchemy/__init__.py`; calling the non-exposed `create_earth()` raises `AttributeError` on purpose |
| 05 | `ft_alembic_5.py` | `from alchemy import ...` — package-level access via `alchemy/__init__.py`, calls `create_air()` |

### Part II — Distillation

| # | File | Description |
|---|------|-------------|
| 00 | `ft_distillation_0.py` | `from alchemy.potions import ...` — direct access to `alchemy/potions.py`, brews `strength_potion()` and `healing_potion()` |
| 01 | `ft_distillation_1.py` | `import alchemy` — package-level access, brews `strength_potion()` and the aliased `heal()` (package-level alias exposed via `__init__.py`) |

### Part III — The Great Transmutation

| # | File | Description |
|---|------|-------------|
| 00 | `ft_transmutation_0.py` | `import alchemy.transmutation.recipes` — direct access to `recipes.py`, calls `lead_to_gold()` |
| 01 | `ft_transmutation_1.py` | `import alchemy.transmutation` — access via the `transmutation` subpackage, calls `lead_to_gold()` |
| 02 | `ft_transmutation_2.py` | `import alchemy` — access via the top-level `alchemy` package, calls `lead_to_gold()` |

### Part IV — Avoid the Explosion

| # | File | Description |
|---|------|-------------|
| — | `alchemy/grimoire/light_spellbook.py` / `light_validator.py` | Light magic: `light_spell_allowed_ingredients()`, `light_spell_record()`, `validate_ingredients()` — mutual dependency resolved with a **lazy (deferred) import** |
| — | `alchemy/grimoire/dark_spellbook.py` / `dark_validator.py` | Dark magic: same logic duplicated on purpose, but both imports stay at the top of the file — reproduces the circular import crash |
| 00 | `ft_kaboom_0.py` | Accesses `grimoire` directly and records a light spell flawlessly — no explosion |
| 01 | `ft_kaboom_1.py` | Accesses `dark_spellbook.py` directly and triggers an uncaught `ImportError` from the circular dependency |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="key-techniques"></a>
<details open><summary><h2>🛠 Key Techniques</h2></summary>

- **`import module`** — imports the whole module object; members are accessed via `module.function()` (ex `ft_alembic_0`, `ft_alembic_2`, `ft_transmutation_0/1/2`)
- **`from module import name`** — imports a specific name directly into the current namespace (ex `ft_alembic_1`, `ft_alembic_3`, `ft_distillation_0`)
- **`__init__.py`** — the file that turns a plain folder into an importable package; controls what is exposed at the package level (`alchemy/__init__.py`, `alchemy/grimoire/__init__.py`, `alchemy/transmutation/__init__.py`)
- **Partial package exposure** — `__init__.py` can re-export only selected functions (`create_air`, `heal` as an alias for `healing_potion`), so unexposed functions like `create_earth` raise `AttributeError` when accessed through the package
- **Absolute imports** — `from alchemy.elements import create_air`, full path from the project root, unambiguous and stable regardless of which file does the importing
- **Relative imports** — `from .elements import create_air` / `from . import light_validator`, path relative to the current package (`.` = same package), only valid inside a package, never in a script run directly
- **Circular import detection** — two modules importing each other at the top level causes `ImportError: cannot import name '...' from partially initialized module '...'`, because Python starts executing a module top-to-bottom and registers it in `sys.modules` before it finishes loading
- **Lazy (deferred) import** — `from .light_validator import validate_ingredients` placed *inside* the function body instead of the top of the file; the import only runs when the function is called, by which point both modules have finished loading — breaks the cycle without any redesign
- **`sys.modules` caching** — the mechanism that makes `import module` (module-level import) more resilient to partial circular loading than `from module import name` (name-level import), since it only needs the module object to *exist*, not to be fully populated yet
- **`ImportError` vs `AttributeError`** — `ImportError` from an unresolved/circular import at load time, `AttributeError` from accessing a name that a package's `__init__.py` never exposed

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="general-rules"></a>
<details open><summary><h2>📐 General Rules</h2></summary>

- Python **3.10+** required
- Code must pass **`flake8`** linter standards
- All code must include comprehensive **type annotations** — checked with `mypy`
- All standard classes, collections, and built-in functions are authorized, except `eval()` and `exec()`
- **Only** imports of modules and files created within this project are allowed
- It is **forbidden** to modify `sys.path`
- All functions stay simple and return strings — the focus is on import mechanics, not logic
- Expected file tree:
```
.
|-- alchemy
|   |-- __init__.py
|   |-- elements.py
|   |-- grimoire
|   |   |-- __init__.py
|   |   |-- dark_spellbook.py
|   |   |-- dark_validator.py
|   |   |-- light_spellbook.py
|   |   `-- light_validator.py
|   |-- potions.py
|   `-- transmutation
|       |-- __init__.py
|       `-- recipes.py
|-- elements.py
|-- ft_alembic_0.py ... ft_alembic_5.py
|-- ft_distillation_0.py, ft_distillation_1.py
|-- ft_kaboom_0.py, ft_kaboom_1.py
`-- ft_transmutation_0.py ... ft_transmutation_2.py
```

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="concepts-learned"></a>
<details open><summary><h2>📚 Concepts Learned</h2></summary>

- How **`__init__.py`** turns a directory into a package, and how it can selectively expose (or hide) functions at the package level
- The practical difference between **`import module`** and **`from module import name`**, and how each behaves differently when a module is only partially loaded
- When to use **absolute imports** (clarity, stability, works from anywhere) vs **relative imports** (convenience inside a package, but invalid the moment the file is run directly as a script)
- Why running a package file directly with `python3 file.py` breaks relative imports — the file becomes `__main__` with no parent package
- The exact mechanics of a **circular import**: how Python registers a module in `sys.modules` before it finishes executing, and why a name-level import (`from x import y`) can fail on a partially initialized module while a module-level import (`import x`) can survive it
- Multiple strategies to resolve circular dependencies, and their trade-offs: **lazy import**, **module-level import instead of name-level**, **extracting the shared dependency into a third module**, and **merging the modules**
- How to deliberately reproduce a circular import crash (`dark_spellbook`/`dark_validator`) as a diagnostic tool, contrasted with the working fix (`light_spellbook`/`light_validator`)

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="resources"></a>
<details open><summary><h2>🔗 Resources</h2></summary>

| Title | Author | Description |
|-------|--------|-------------|
| [Domine o Módulo OS em Python: Caminhos Relativos e Absolutos \| FileNotFoundError](https://www.youtube.com/watch?v=vHe4vvzDuMA) | [Programação Dinâmica](https://www.youtube.com/@pgdinamica) | Explains relative vs absolute paths in Python using the `os` module, and how path resolution mistakes lead to `FileNotFoundError` — directly relevant to understanding how Python resolves import paths. |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<p align="left">
  Developed by <a href="https://github.com/jalves-de">Jonathan Alves</a>
</p>