"""Demo launcher showing all three widgets in a single window."""

import tkinter as tk

from .widgets import LogoWidget, PoweredByLengthWidget, PoweredByWidthWidget


def demo():
    """Launch a demo window showing all three Python logo widgets."""
    root = tk.Tk()
    root.title("Python Logo Widgets - Demo")

    LogoWidget(root).pack(pady=5)
    PoweredByLengthWidget(root).pack(pady=5)
    PoweredByWidthWidget(root).pack(pady=5)

    root.mainloop()
