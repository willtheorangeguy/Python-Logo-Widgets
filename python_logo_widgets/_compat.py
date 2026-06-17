"""
Backward-compatible wrapper functions.

These recreate the original standalone-window behavior
for users who called logo_widget(), length_widget(), width_widget().
"""

import tkinter as tk

from .widgets import LogoWidget, PoweredByLengthWidget, PoweredByWidthWidget


def logo_widget():
    """Display the Python logo in a standalone window."""
    root = tk.Tk()
    root.title("Python Logo Widget")
    LogoWidget(root).pack()
    root.mainloop()


def length_widget():
    """Display the Python Powered (tall) logo in a standalone window."""
    root = tk.Tk()
    root.title("Python Powered Widget")
    PoweredByLengthWidget(root).pack()
    root.mainloop()


def width_widget():
    """Display the Python Powered (wide) logo in a standalone window."""
    root = tk.Tk()
    root.title("Python Powered Widget")
    PoweredByWidthWidget(root).pack()
    root.mainloop()
