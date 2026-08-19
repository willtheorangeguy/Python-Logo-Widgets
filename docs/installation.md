# Python Logo Widgets — Installation

## Requirements

| | |
|---|---|
| Python | 3.x with Tkinter |
| Dependencies | None |

Tkinter is bundled on Windows and macOS. On Linux:

```bash
sudo apt install python3-tk        # Debian, Ubuntu
sudo dnf install python3-tkinter   # Fedora
```

## Install

```bash
pip install Python-Logo-Widgets
```

The images are packaged inside `python_logo_widgets/imgs/`, so there is nothing to copy
alongside and no path to configure.

## From source

```bash
git clone https://github.com/willtheorangeguy/Python-Logo-Widgets
cd Python-Logo-Widgets
pip install -e .
python -m python_logo_widgets
```

## Verify

```bash
python-logo-widgets
```

A window with the Python logo. If it opens empty, see [Troubleshooting](./troubleshooting.md) —
though the widget classes are written specifically to prevent the usual cause.

```python
from python_logo_widgets import LogoWidget, PoweredByLengthWidget, PoweredByWidthWidget
```

## Adding it to your project

```
python-logo-widgets
```

in your `requirements.txt` or `pyproject.toml` dependencies. It adds no transitive dependencies
of its own.

Note the licence position before you do: the code is GPL v3, which is a real obligation for
anything you link it into, and the images are PSF trademarks under separate terms. See
[FAQ](./faq.md).

## Uninstall

```bash
pip uninstall Python-Logo-Widgets
```

Nothing is written outside the package — no cache, no config, no data.
