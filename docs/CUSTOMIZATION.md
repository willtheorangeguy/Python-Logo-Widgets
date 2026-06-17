# Python Logo Widgets Customization

## Change Background Color

Pass the `bg` parameter when creating a widget:

```python
from python_logo_widgets import LogoWidget

# White background
LogoWidget(root, bg="white").pack()

# Custom hex color
LogoWidget(root, bg="#2b2b2b").pack()
```

## Pass Additional Frame Options

All extra keyword arguments are passed through to `tk.Frame`:

```python
LogoWidget(root, bg="white", padx=10, pady=10, relief="raised", borderwidth=2).pack()
```

## Change Image

To use a custom image, subclass the widget and override the image path:

```python
import tkinter as tk
from python_logo_widgets.widgets import _load_image

class CustomLogoWidget(tk.Frame):
    def __init__(self, parent, bg="black", **kwargs):
        super().__init__(parent, **kwargs)
        self._image = tk.PhotoImage(file="path/to/your/image.gif")
        self._label = tk.Label(self, image=self._image, bg=bg)
        self._label.pack(fill=tk.BOTH, expand=True)
```

**Note:** `tkinter.PhotoImage` supports `.gif` and `.png` formats.
