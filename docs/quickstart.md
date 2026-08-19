# Python Logo Widgets — Quickstart

## Install

```bash
pip install Python-Logo-Widgets
```

Nothing else — Tkinter ships with Python.

## Embed one

```python
import tkinter as tk
from python_logo_widgets import LogoWidget, PoweredByWidthWidget

root = tk.Tk()
root.title("My App")

LogoWidget(root, bg="white").pack(pady=10)
PoweredByWidthWidget(root).pack(side=tk.BOTTOM)

root.mainloop()
```

Each widget is a `tk.Frame`, so it behaves like any other container — `pack`, `grid`, or `place`
it wherever you like.

## The three widgets

| Class | Image | Typical use |
|---|---|---|
| `LogoWidget` | The Python logo | A splash or about screen |
| `PoweredByLengthWidget` | "Python Powered", tall | A sidebar |
| `PoweredByWidthWidget` | "Python Powered", wide | A footer |

## Background colour

```python
LogoWidget(root, bg="white")     # default is "black"
```

`bg` sets the background of the image label. The badges have transparent regions, so matching
`bg` to your window is usually what you want — the default black suits a dark window and looks
like a box on a light one.

Any other keyword arguments go to `tk.Frame`.

## See them

```bash
python-logo-widgets
python -m python_logo_widgets
```

## The older function API

```python
from python_logo_widgets._compat import logo_widget
logo_widget()      # opens its own window and blocks
```

Kept working for code written against the original release. New code should use the widget
classes — they embed, and these do not.

## Before you ship it

The images are PSF trademarks rather than GPL content. Using them to show your program is built
with Python is the intended use; see [FAQ](./faq.md) and
[`internal/known-issues.md`](./internal/known-issues.md).
