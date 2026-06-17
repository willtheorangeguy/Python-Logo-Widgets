"""Python Logo Widgets - Tkinter widgets displaying Python logos."""

from .widgets import LogoWidget, PoweredByLengthWidget, PoweredByWidthWidget
from ._compat import logo_widget, length_widget, width_widget
from ._demo import demo

__all__ = [
    "LogoWidget",
    "PoweredByLengthWidget",
    "PoweredByWidthWidget",
    "logo_widget",
    "length_widget",
    "width_widget",
    "demo",
]

__version__ = "3.0.0"
