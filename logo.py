"""
Python Logo Widget
Copyright (C) 2016-2022 @willtheorangeguy

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

# Import Statements
from tkinter import *


def logo_widget():
    # Window Statements
    window = Tk()
    window.title("Python Logo Widget")  # Edit title as needed

    # Image Statements
    img = PhotoImage(file="imgs/logo.gif")  # Edit image as needed
    label = Label(window, image=img, bg="black")  # Edit border as needed

    # Pack Statements
    label.pack(side=BOTTOM)  # Edit pack as needed

    # Sustain Window
    window.mainloop()


if __name__ == "__main__":
    logo_widget()
