# Changelog

## [v3.0.0](https://github.com/willtheorangeguy/Python-Logo-Widgets/releases/tag/v3.0.0)

### Changed

- Restructured into proper Python package (`python_logo_widgets/`)
- Widgets are now `tkinter.Frame` subclasses (`LogoWidget`, `PoweredByLengthWidget`, `PoweredByWidthWidget`) that can be embedded in any tkinter application
- Images bundled inside the package using `importlib.resources` — works reliably after `pip install`
- Consolidated packaging config to `pyproject.toml` only (removed `setup.py`, `setup.cfg`, `MANIFEST.in`)
- Fixed console entry point (`python-logo-widgets` command now works)
- Demo mode shows all three widgets in a single window instead of sequentially

### Added

- `bg` parameter on all widgets for customizable background color
- `demo()` function for launching the demo window
- Backward-compatible `logo_widget()`, `length_widget()`, `width_widget()` functions

### Removed

- Root-level `logo.py`, `length.py`, `width.py`, `main.py` standalone scripts (replaced by package)

## [v2.2.2](https://github.com/willtheorangeguy/Python-Logo-Widgets/releases/tag/v2.2.2)

### Changed

- Refactor PyPI package

## [v2.2.1](https://github.com/willtheorangeguy/Python-Logo-Widgets/releases/tag/v2.2.1)

### Changed

- Finalized PyPI package

## [v2.2.0](https://github.com/willtheorangeguy/Python-Logo-Widgets/releases/tag/v2.2.0)

### Added

- PyPI package

## [v2.1.0](https://github.com/willtheorangeguy/Python-Logo-Widgets/releases/tag/v2.1.0)

### Changed

- Update documentation
- Update legal notices

## [v2.0.0](https://github.com/willtheorangeguy/Python-Logo-Widgets/releases/tag/v2.0.0)

### Added

- `main.py` file

### Changed

- Added whitespace
- Updated `README.md`

## [v1.0](https://github.com/willtheorangeguy/Python-Logo-Widgets/releases/tag/v1.0)

### Added

- Program Code
