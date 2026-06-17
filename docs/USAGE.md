# Python Logo Widgets Usage

## Install via `pip`

```bash
pip install Python-Logo-Widgets
```

## Embed in Your Application

Import the widget classes and add them to your `tkinter` window:

```python
import tkinter as tk
from python_logo_widgets import LogoWidget, PoweredByLengthWidget, PoweredByWidthWidget

root = tk.Tk()
root.title("My Application")

# Add any combination of widgets
logo = LogoWidget(root, bg="white")
logo.pack(pady=10)

powered = PoweredByWidthWidget(root)
powered.pack(side=tk.BOTTOM)

root.mainloop()
```

### Available Widgets

| Widget Class | Image | Description |
|---|---|---|
| `LogoWidget` | `logo.gif` | The Python logo |
| `PoweredByLengthWidget` | `length.gif` | "Python Powered" tall badge |
| `PoweredByWidthWidget` | `width.gif` | "Python Powered" wide badge |

### Parameters

All widgets accept:

- **`parent`** — The parent `tkinter` widget (required).
- **`bg`** — Background color for the image label (default: `"black"`).
- **`**kwargs`** — Any additional keyword arguments are passed to `tk.Frame`.

### Layout

The widgets are `tkinter.Frame` subclasses, so you can use any geometry manager:

```python
# Using pack
LogoWidget(root).pack(side=tk.TOP, pady=5)

# Using grid
LogoWidget(root).grid(row=0, column=0, padx=10)

# Using place
LogoWidget(root).place(x=50, y=50)
```

## Standalone Demo

To see all three widgets in a demo window:

```bash
# Command line
python-logo-widgets

# As a module
python -m python_logo_widgets
```

## Legacy Standalone Functions

For backward compatibility, the old standalone functions are still available:

```python
from python_logo_widgets import logo_widget, length_widget, width_widget

# Each opens its own window with mainloop()
logo_widget()
```

These create their own `Tk()` root window and call `mainloop()`, so they cannot be embedded in an existing application.
