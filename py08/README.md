# 💊 py08 — The Matrix

<p align="left">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Grade-100%2F100-brightgreen?style=for-the-badge" />
</p>

> Welcome to the Real World of Data Engineering. First contact with the Python ecosystem beyond the language itself: virtual environments, package management with pip and Poetry, external libraries (NumPy, Pandas, Matplotlib), and secure configuration with environment variables and `.env` files.

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

| # | File(s) | Description |
|---|---------|-------------|
| 00 | `construct.py` | Detect virtual environment using `sys.base_prefix` vs `sys.prefix`; display environment info and setup instructions |
| 01 | `loading.py`, `requirements.txt`, `pyproject.toml` | Data analysis pipeline with NumPy, Pandas, and Matplotlib; safe import handling; pip vs Poetry comparison |
| 02 | `oracle.py`, `.env.example`, `.gitignore` | Secure config loading with `python-dotenv`; `os.getenv()` with fallbacks; dev/production mode switching |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="key-techniques"></a>
<details open><summary><h2>🛠 Key Techniques</h2></summary>

- **`sys.prefix` vs `sys.base_prefix`** — comparing these two values detects whether a virtual environment is active (`base_prefix != prefix` means inside a venv) (ex00)
- **`os.environ["VIRTUAL_ENV"]`** — environment variable set automatically when a venv is activated; holds the full path to the environment (ex00)
- **`site.getsitepackages()`** — returns the list of directories where packages are installed in the current environment (ex00)
- **`python -m venv`** — creates a virtual environment; `source .../activate` activates it on Unix (ex00)
- **`try/except ImportError`** — safe import pattern for external libraries; extracts the missing package name and prints installation instructions before calling `sys.exit(1)` (ex01)
- **`importlib.metadata`** — reads installed package metadata (name, version) at runtime without importing the package itself (ex01)
- **`requirements.txt`** — pip dependency file; installed with `pip install -r requirements.txt` (ex01)
- **`pyproject.toml`** — Poetry project file; defines dependencies declaratively; installed with `poetry install` (ex01)
- **NumPy** — generates simulated matrix data with `np.random.normal()`; `np.random.seed()` for reproducibility (ex01)
- **Pandas** — creates `DataFrame` from dataset; `resample()` for monthly aggregation; `strftime()` for date formatting (ex01)
- **Matplotlib** — plots time-series chart with `plt.plot()`; exports to PNG with `plt.savefig()` (ex01)
- **`python-dotenv`** — `load_dotenv()` reads a `.env` file and injects variables into `os.environ` (ex02)
- **`os.getenv(key, default)`** — reads environment variables with optional fallback; safer than `os.environ[key]` for optional variables (ex02)
- **`.env.example`** — template file committed to version control showing required variables without real values (ex02)
- **`.gitignore`** — excludes `.env` and `venv/` from version control to prevent secrets and large files from being committed (ex02)

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="general-rules"></a>
<details open><summary><h2>📐 General Rules</h2></summary>

- Python **3.10+** required
- Code must pass **`flake8`** linter standards (exception: `# type: ignore` on external imports is allowed)
- All code must include comprehensive **type annotations** — checked with `mypy`
- Each exercise in its own directory (`ex0/` through `ex2/`)
- Programs must be tested in multiple environments: with/without venv, with/without dependencies
- **Never commit** the `.env` file or the virtual environment folder to the repository
- NumPy must be the **data source** in ex01 — hardcoded lists or `range()` are not allowed

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="concepts-learned"></a>
<details open><summary><h2>📚 Concepts Learned</h2></summary>

- Why **virtual environments** exist — isolating dependencies per project prevents version conflicts across projects and protects the global Python installation
- The difference between **pip** (simple, universal) and **Poetry** (lockfile, dependency resolution, project packaging) — and when each is the right tool
- How Python resolves **`sys.prefix`** and **`sys.base_prefix`** to know where it is running from
- The **safe import pattern** — catching `ImportError` at the top of a script to give a helpful message instead of a traceback
- Why **secrets never belong in code** — using `.env` files with `.gitignore` and `.env.example` keeps credentials out of version control while keeping the project reproducible
- The **variable lookup order** for `os.getenv()`: shell-injected variables override `.env` file values, which override code defaults — useful for switching dev/production without changing code
- How `importlib.metadata` allows **runtime introspection** of installed packages without importing them

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="resources"></a>
<details open><summary><h2>🔗 Resources</h2></summary>

| Title | Author | Description |
|-------|--------|-------------|
| [Python Virtual Environments - Full Tutorial for Beginners](https://www.youtube.com/watch?v=Y21OR1OPC9A) | [Tech With Tim](https://www.youtube.com/@TechWithTim) | Complete beginner-friendly guide to creating, activating, and using Python virtual environments with `venv`. |
| [The Complete Guide to Python Virtual Environments!](https://www.youtube.com/watch?v=KxvKCSwlUv8) | [teclado](https://www.youtube.com/@tecladocode) | In-depth walkthrough of virtual environments, covering best practices, `requirements.txt`, and common pitfalls. |
| [A Deep Dive into How Python Virtual Environments Work](https://www.youtube.com/watch?v=dy3svq9CbNo) | [Ian Wootten](https://www.youtube.com/@IanWootten) | Explains the internals of venvs — how `sys.prefix`, `sys.base_prefix`, and path manipulation work under the hood. |
| [sys.prefix — Python Docs PT](https://docs.python.org/pt-br/3/library/sys.html#sys.prefix) | [Python.org](https://docs.python.org) | Official documentation for `sys.prefix` and `sys.base_prefix` — the key variables used to detect an active virtual environment. |
| [Why I choose Poetry over venv](https://medium.com/@deepakcoder80/why-i-choose-poetry-over-venv-for-managing-python-dependencies-95cd7eb50223) | Medium | Practical comparison of Poetry vs plain venv for dependency management — lockfiles, reproducibility, and project packaging. |
| [Poetry - Python dependency management](https://python-poetry.org/) | [python-poetry.org](https://python-poetry.org/) | Official Poetry documentation — reference for `pyproject.toml`, `poetry install`, `poetry add`, and environment management. |
| [Te ensino TUDO sobre Pandas para análise de dados](https://www.youtube.com/watch?v=1JpYOqvDJNU) | [Asimov Academy](https://www.youtube.com/@AsimovAcademy) | Full Pandas tutorial for data analysis — DataFrames, filtering, grouping, and data manipulation. |
| [O que é Numpy](https://www.youtube.com/watch?v=4Krky5DKv4M&t=255s) | [Roberto J. Oliveira](https://www.youtube.com/@robertojoliveira) | Introduction to NumPy — what it is, why it's faster than Python lists, and core array operations. |
| [Biblioteca NumPy - Introdução e criação de arrays](https://www.youtube.com/watch?v=LidaJMcVmu4) | [Bóson Treinamentos](https://www.youtube.com/@bosontreinamentos) | Hands-on introduction to NumPy arrays, data types, and random number generation. |
| [Introdução aos gráficos com Matplotlib](https://www.youtube.com/watch?v=iQOExGgu1Ow) | [Bóson Treinamentos](https://www.youtube.com/@bosontreinamentos) | Introduction to Matplotlib's pyplot interface — line charts, labels, formatting, and saving figures. |
| [Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html) | [Matplotlib.org](https://matplotlib.org) | Official pyplot tutorial — reference for `plt.plot()`, `plt.title()`, `plt.savefig()`, and chart customization. |
| [importlib.metadata — Python Docs PT](https://docs.python.org/pt-br/3/library/importlib.metadata.html) | [Python.org](https://docs.python.org) | Official documentation for `importlib.metadata` — accessing installed package versions and entry points at runtime. |
| [Python Dotenv - Variáveis de Ambiente Eficientes no Python](https://youtu.be/G27vGWfhpQA?si=yjwrFrY0uQMdIS65) | [Hashtag Programação](https://www.youtube.com/@HashtagProgramacao) | Practical tutorial on `python-dotenv` — loading `.env` files, `load_dotenv()`, and secure configuration management. |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<p align="left">
  Developed by <a href="https://github.com/jalves-de">Jonathan Alves</a>
</p>
