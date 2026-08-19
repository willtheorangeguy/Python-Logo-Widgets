# Python Logo Widgets — API

## Widget classes

All three subclass `tkinter.Frame` and share a signature.

```python
LogoWidget(parent, bg="black", **kwargs)
PoweredByLengthWidget(parent, bg="black", **kwargs)
PoweredByWidthWidget(parent, bg="black", **kwargs)
```

| Parameter | Meaning |
|---|---|
| `parent` | The parent Tkinter widget |
| `bg` | Background of the inner image label; default `"black"` |
| `**kwargs` | Forwarded to `tk.Frame` |

| Class | Image |
|---|---|
| `LogoWidget` | The Python logo |
| `PoweredByLengthWidget` | "Python Powered", tall |
| `PoweredByWidthWidget` | "Python Powered", wide |

Being `Frame` subclasses, they support the full widget protocol:

```python
w = LogoWidget(root, bg="white")
w.pack(side=tk.LEFT, padx=8)
w.grid(row=0, column=1)
w.destroy()
```

### Instance attributes

| Attribute | What |
|---|---|
| `_image` | The `PhotoImage`. Private, but the reference that keeps the image alive |
| `_label` | The `Label` holding it |

Underscore-prefixed and not part of the supported API. Reassigning `_image` without also updating
`_label` leaves the widget showing the old image or nothing.

## Compatibility functions

```python
from python_logo_widgets._compat import logo_widget, length_widget, width_widget

logo_widget()      # opens a window, blocks until closed
```

The original API. Each creates its own `Tk()` root, packs the corresponding widget, and calls
`mainloop()` — so they **block** and cannot be embedded.

Kept for code written against the first release; implemented in terms of the widget classes, so
there is one implementation. New code should use the classes.

## Entry points

```bash
python-logo-widgets              # console script
python -m python_logo_widgets    # module
```

Both run the demo in `_demo.py`.

## Imports

```python
from python_logo_widgets import LogoWidget, PoweredByLengthWidget, PoweredByWidthWidget
```

Importing the package opens no window and loads no image — `PhotoImage` construction happens in
each widget's `__init__`, which requires a live Tk root. Instantiating one before `tk.Tk()` exists
raises.

## Images

Resolved with `importlib.resources.files("python_logo_widgets.imgs")`, so they are found however
the package is installed. GIF, because Tkinter reads GIF and PNG only.

They are PSF trademarks rather than GPL content — see [FAQ](./faq.md) and
[`internal/known-issues.md`](./internal/known-issues.md).
