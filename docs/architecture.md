# Python Logo Widgets — Architecture

Seventy lines of implementation, and two details that make it work.

```text
python_logo_widgets/
├── widgets.py    three tk.Frame subclasses
├── _compat.py    the original function API, wrapping the classes
├── _demo.py      the standalone demo
├── __main__.py   python -m entry
└── imgs/         logo.gif, length.gif, width.gif
```

## The widgets

All three are the same shape:

```python
class LogoWidget(tk.Frame):
    def __init__(self, parent, bg="black", **kwargs):
        super().__init__(parent, **kwargs)
        self._image = tk.PhotoImage(file=_load_image("logo.gif"))
        self._label = tk.Label(self, image=self._image, bg=bg)
        self._label.pack(fill=tk.BOTH, expand=True)
```

Subclassing `Frame` rather than exposing a function is what makes them **embeddable** — the
caller places them like any other widget, in any geometry manager, inside any container.

## Detail one: finding the images

```python
from importlib.resources import files

def _load_image(image_name):
    return str(files("python_logo_widgets.imgs").joinpath(image_name))
```

Resolved through the package, not by a path relative to the source file or the working directory.
That is why the widgets work identically from a source checkout, a wheel install, and someone
else's application — the three ways a bundled resource usually gets lost.

`imgs/__init__.py` exists to make the directory an importable package so `files()` can address it.

One limitation: `str()` on the result assumes the resource has a real filesystem path, which is
true for a normal pip install and not for a zipped package. `importlib.resources.as_file()` is
the supported idiom. See [`internal/known-issues.md`](./internal/known-issues.md).

## Detail two: keeping the images alive

```python
self._image = tk.PhotoImage(...)
```

Tkinter holds no Python reference to a `PhotoImage`. An image assigned only to a local would be
garbage-collected when `__init__` returns, and the label would render **blank with no error** —
the single most common Tkinter bug, and one that looks like a missing file.

Binding it to the instance ties the image's lifetime to the widget's, which is exactly right.

## `_compat.py`

The original API was three functions that each opened a window:

```python
def logo_widget():
    root = tk.Tk()
    root.title("Python Logo Widget")
    LogoWidget(root).pack()
    root.mainloop()
```

They are kept, implemented in terms of the new classes rather than duplicating them, so old code
keeps working and there is one implementation. Underscore-prefixed to signal they are not the
recommended API.

## `_demo.py` and `__main__.py`

The demo window shown by `python-logo-widgets` and `python -m python_logo_widgets`. Separate from
the library so importing the package opens nothing.

## Why GIF

Tkinter's `PhotoImage` reads GIF and PNG only. PNG would work; GIF is what is bundled. Anything
else — JPEG, SVG, WebP — needs Pillow, and a widget package that pulled in an imaging library to
show three static badges would not be worth depending on.

## What is not here

No scaling, no theming beyond `bg`, no state, no I/O. The package loads three images and draws
them, and its correctness is entirely in the two details above.
