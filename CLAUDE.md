# CLAUDE.md

## Project Overview

Python Logo Widgets is a lightweight Python package providing Tkinter Frame widgets that display Python branding images (logo and "Python Powered" badges). Version 3.0.0. Licensed under GPLv3.

## Repository Structure

```
python_logo_widgets/       # Main package
  widgets.py               # Core widget classes: LogoWidget, PoweredByLengthWidget, PoweredByWidthWidget
  _demo.py                 # Demo window launcher
  _compat.py               # Legacy compatibility functions (v2 API)
  __init__.py              # Public API exports, __version__
  __main__.py              # python -m entry point
  imgs/                    # Bundled GIF images (logo.gif, length.gif, width.gif)
tests/
  test_widgets.py          # Widget unit tests (mocked tkinter)
  test_compat.py           # Backward compatibility tests
docs/                      # Usage, customization, legal docs
.github/workflows/         # CI/CD pipelines
```

## Development Commands

```bash
# Install in development mode
pip install -e .

# Run tests
pytest

# Run the demo
python -m python_logo_widgets
# or: python main.py

# Lint (CI uses this)
pip install pylint
pylint python_logo_widgets/
```

## Code Conventions

- **Python 3.9+** minimum, stdlib only (tkinter, importlib.resources)
- **4-space indentation**, no tabs
- **Formatter**: Black
- **Linter**: pylint (runs on every push in CI)
- **Docstrings**: Google-style with Args/Returns sections
- **Comments**: Project convention is heavy commenting on functions and code blocks
- **Versioning**: Semantic versioning; version defined in `__init__.py` and `pyproject.toml`

## Architecture

All widgets inherit from `tk.Frame` and accept `parent` and optional `bg` (default `"black"`) parameters. Images are loaded via `importlib.resources.files()` from the bundled `imgs` subpackage. PhotoImage references are stored on `self._image` to prevent garbage collection.

## CI/CD

- **pytest.yml** — runs tests on Python 3.x on push and PR
- **pylint.yml** — linting on Python 3.9 on push
- **codeql.yml** — security scanning on push to master + weekly
- **gitleaks.yml** — secret detection on push and PR
- **push-to-pypi.yml** — publishes to PyPI on release or manual trigger

## Testing

Tests use `unittest.mock` to patch tkinter so no display server is needed. Run with `pytest`. Test dependencies are in `requirements.txt`.

## Key Files to Know

- `pyproject.toml` — build config, metadata, entry point (`python-logo-widgets` console script)
- `python_logo_widgets/__init__.py` — public API surface and version
- `python_logo_widgets/widgets.py` — all widget implementations (~70 lines)
- `CHANGELOG.md` — version history
- `CONTRIBUTING.md` — contribution guidelines (GitHub Flow, PR templates)
