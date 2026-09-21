# Python Logo Widgets — Development

## Setup

```bash
git clone https://github.com/willtheorangeguy/Python-Logo-Widgets
cd Python-Logo-Widgets
pip install -e .
pytest
```

No runtime dependencies; `requirements.txt` holds the tooling.

## Layout

| File | Responsibility |
|---|---|
| `widgets.py` | The three `Frame` subclasses |
| `_compat.py` | The original function API, wrapping the classes |
| `_demo.py` | The demo window |
| `__main__.py` | `python -m` entry |
| `imgs/` | The three GIFs, plus an `__init__.py` so `importlib.resources` can address them |

## Tests

```bash
pytest
pytest tests/test_widgets.py -v
```

`test_widgets.py` covers the widget classes; `test_compat.py` the legacy functions.

Tkinter tests need a display. On a headless Linux runner:

```bash
xvfb-run -a pytest
```

## Conventions

- **Resources through `importlib.resources`**, never a path relative to `__file__` or the working
  directory. It is what makes the package work from a wheel, a checkout, and inside someone
  else's application.
- **Bind every `PhotoImage` to the instance.** Tkinter keeps no reference of its own, and a
  collected image renders blank with no error.
- **`_compat` wraps the classes**, never duplicates them. One implementation.
- **No runtime dependencies.** Pillow would buy scaling and other formats and is still not worth
  being the first dependency of a package that draws three static images.
- **GPL header on every module** — required by the licence.

## Adding a widget

Add the GIF to `imgs/`, add a class following the existing three, export it from `__init__.py`,
and add a test. The shape is deliberate; keep it.

Before adding an image, note the trademark position on the ones already here — see
[`internal/known-issues.md`](./internal/known-issues.md).

## The `str(files(...))` limitation

`_load_image` returns `str(files(...).joinpath(name))`, which assumes a real filesystem path.
That holds for pip installs and not for a zipped package. `importlib.resources.as_file()` is the
supported idiom and would need the path used inside a context manager. Same known-issues file.

## Licence

GPL v3 for the code. The images are PSF trademarks under separate terms — contributions of code
are GPL; contributions of trademarked artwork are a different question entirely.

## Recording defects

Bugs found while working here go in [`internal/known-issues.md`](./internal/known-issues.md)
rather than being fixed in passing, unless fixing them is the job you are on.
