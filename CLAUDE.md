# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python Logo Widgets is a Tkinter-based library that displays official Python logo/branding images in GUI windows. It exposes three standalone widget functions and a demo launcher. The package can be used as a library (imported into other Tkinter apps), run directly as a CLI, or executed as a Python module.

## Commands

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run tests:**
```bash
pytest
```

**Run a single test:**
```bash
pytest tests/test_main.py::test_widgets
```

**Lint all Python files:**
```bash
pylint $(git ls-files '*.py')
```

**Run the demo (all three widgets sequentially):**
```bash
python main.py
```

**Run as a module:**
```bash
python -m python_logo_widgets
```

## Architecture

The library is flat — all source lives at the repo root, with no sub-packages.

- **`logo.py`**, **`length.py`**, **`width.py`** — one public function each (`logo_widget()`, `length_widget()`, `width_widget()`). Each creates a `Tk()` window, loads the corresponding GIF from `imgs/`, attaches it via a `Label`, and enters `mainloop()`. Because `mainloop()` blocks, calling all three sequentially (as `main.py` does) means each window must be closed before the next opens.
- **`main.py`** — `widgets()` calls all three functions in sequence. This is the entry point for the CLI (`python-logo-widgets` console script) and the module runner.
- **`__main__.py`** — enables `python -m python_logo_widgets`; imports and calls `widgets()` from `main.py`.
- **`__init__.py`** — minimal PyPI package init; `__all__` is intentionally empty.
- **`imgs/`** — contains `logo.gif`, `length.gif`, `width.gif`. These paths are referenced relative to the working directory (not the file location), so widgets must be invoked from the repo root.
- **`tests/`** — pytest suite. Tests mock the three widget functions to avoid launching real Tkinter windows during CI.

## Coding Conventions

- **4-space indentation**, no tabs.
- Every function and logical block should be commented (the existing style uses section header comments like `# Import Statements`, `# Window Statements`, `# Image Statements`, `# Pack Statements`).
- `pylint: disable=locally-disabled, invalid-name, import-error` is used at the top of every source file — maintain this.
- New widget files should follow the exact structure of the existing widget files (`logo.py`, `length.py`, `width.py`).
- Tests live in `tests/` and use `unittest.mock.patch` to avoid real Tkinter windows. Tests must manipulate `sys.path` to import modules from the repo root (see existing pattern in `tests/test_main.py`).
- Version is maintained in both `pyproject.toml` and `setup.py`/`setup.cfg` — keep all three in sync when bumping.
- Code formatting is enforced by **Black** (configured via `.deepsource.toml`).
