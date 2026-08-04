# 🗃️ py04 — Data Archivist

<p align="left">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Grade-100%2F100-brightgreen?style=for-the-badge" />
</p>

> Digital Preservation in the Cyber Archives. Builds on py00–py03 to master Python's file I/O system: reading, writing, stream management via `sys.stdin/stdout/stderr`, and safe resource handling with the `with` statement.

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
| 00 | `ft_ancient_text.py` | Read a file from CLI and display its contents — handle `FileNotFoundError` and `PermissionError` |
| 01 | `ft_archive_creation.py` | Extend ex00 — transform file content and write to a new file based on user input |
| 02 | `ft_stream_management.py` | Extend ex01 — route errors to `sys.stderr`, read user input via `sys.stdin` without `input()` |
| 03 | `ft_vault_security.py` | `with` statement — `secure_archive()` function returns `(bool, str)` for safe read/write operations |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="key-techniques"></a>
<details open><summary><h2>🛠 Key Techniques</h2></summary>

- **`open()`** — open files for reading (`r`) or writing (`w`); returns a file object of type `typing.IO` (ex00)
- **`io.read()`** — read the full contents of an open file into a string (ex00)
- **`io.write()`** — write a string to an open file (ex01)
- **`io.close()`** — explicitly close a file handle to free resources (ex00, ex01)
- **`input()`** — prompt user for a filename to save to (ex01)
- **`sys.stdin`** — read user input from the standard input stream without `input()` (ex02)
- **`sys.stdout`** — standard output stream (ex02)
- **`sys.stderr`** — write error messages to the error stream separately from normal output (ex02)
- **`io.flush()`** — force-flush a stream buffer to ensure output is written immediately (ex02)
- **`with` statement** — context manager that guarantees file closure even if an exception occurs (ex03)
- **`typing.IO`** — type hint for file objects returned by `open()` (ex00–ex02)
- **Type hints** — all functions annotated with `mypy`-compatible types
- **`flake8`** — PEP8 linting enforced throughout the module

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="general-rules"></a>
<details open><summary><h2>📐 General Rules</h2></summary>

- Python **3.10+** required
- Code must pass **`flake8`** linter standards
- All functions and methods must include **type hints** — checked with `mypy`
- Each exercise in its own file and directory (`ex0/` through `ex3/`)
- Handle exceptions gracefully — programs must **never crash**
- The `with` statement is only authorized from **ex03** onwards — do not use it in earlier exercises
- Each exercise builds directly on the previous one — the file-handling code evolves progressively

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="concepts-learned"></a>
<details open><summary><h2>📚 Concepts Learned</h2></summary>

- How Python's **file object** (`typing.IO`) works — open, read, write, close lifecycle
- The difference between **standard streams**: `stdin`, `stdout`, and `stderr`, and when to use each
- Why separating **error output** from normal output matters in real systems and pipelines
- How the **`with` statement** (context manager) eliminates the need to manually call `close()` and prevents resource leaks
- Building a **reusable utility function** (`secure_archive`) that returns structured results `(bool, str)` instead of raising exceptions directly
- Progressively **refactoring** the same program across exercises — each step adds robustness

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="resources"></a>
<details open><summary><h2>🔗 Resources</h2></summary>

| Title | Author | Description |
|-------|--------|-------------|
| [Python - Biblioteca Padrão - Módulo I/O](https://www.youtube.com/watch?v=WlSSdZ-JPxc) | [CÓDIGO FLUENTE](https://www.youtube.com/@codigofluente) | A walkthrough of Python's standard I/O module: opening files, reading and writing, working with streams, and handling file-related exceptions. |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<p align="left">
  Developed by <a href="https://github.com/jalves-de">Jonathan Alves</a>
</p>