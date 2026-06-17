"""
Python Logo Widgets
Copyright (C) 2016-2024 @willtheorangeguy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import tkinter as tk
from importlib.resources import files


def _load_image(image_name):
    """Return the filesystem path to a bundled image file."""
    return str(files("python_logo_widgets.imgs").joinpath(image_name))


class LogoWidget(tk.Frame):
    """A Frame widget displaying the Python logo.

    Args:
        parent: The parent tkinter widget.
        bg: Background color for the image label. Defaults to "black".
        **kwargs: Additional keyword arguments passed to tk.Frame.
    """

    def __init__(self, parent, bg="black", **kwargs):
        super().__init__(parent, **kwargs)
        self._image = tk.PhotoImage(file=_load_image("logo.gif"))
        self._label = tk.Label(self, image=self._image, bg=bg)
        self._label.pack(fill=tk.BOTH, expand=True)


class PoweredByLengthWidget(tk.Frame):
    """A Frame widget displaying the 'Python Powered' logo (tall variant).

    Args:
        parent: The parent tkinter widget.
        bg: Background color for the image label. Defaults to "black".
        **kwargs: Additional keyword arguments passed to tk.Frame.
    """

    def __init__(self, parent, bg="black", **kwargs):
        super().__init__(parent, **kwargs)
        self._image = tk.PhotoImage(file=_load_image("length.gif"))
        self._label = tk.Label(self, image=self._image, bg=bg)
        self._label.pack(fill=tk.BOTH, expand=True)


class PoweredByWidthWidget(tk.Frame):
    """A Frame widget displaying the 'Python Powered' logo (wide variant).

    Args:
        parent: The parent tkinter widget.
        bg: Background color for the image label. Defaults to "black".
        **kwargs: Additional keyword arguments passed to tk.Frame.
    """

    def __init__(self, parent, bg="black", **kwargs):
        super().__init__(parent, **kwargs)
        self._image = tk.PhotoImage(file=_load_image("width.gif"))
        self._label = tk.Label(self, image=self._image, bg=bg)
        self._label.pack(fill=tk.BOTH, expand=True)
