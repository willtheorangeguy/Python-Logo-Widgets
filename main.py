"""
Python Logo Widget Samples
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
from logo import *
from length import *
from width import *

def main():
    logo_widget()
    length_widget()
    width_widget()

if __name__ == "__main__":
    main()

# For PyInstaller
import sys

if getattr(sys, 'frozen', False):
    image = PhotoImage(file=os.path.join(sys._MEIPASS, "imgs/logo.gif"))
    image = PhotoImage(file=os.path.join(sys._MEIPASS, "imgs/length.gif"))
    image = PhotoImage(file=os.path.join(sys._MEIPASS, "imgs/width.gif"))
else:
    image = PhotoImage(file="imgs/logo.gif")
    image = PhotoImage(file="imgs/length.gif")
    image = PhotoImage(file="imgs/width.gif")
