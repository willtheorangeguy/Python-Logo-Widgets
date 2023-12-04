"""
Python Logo Widget Samples
Copyright (C) 2016-2023 @willtheorangeguy

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
# pylint: disable=locally-disabled, invalid-name, import-error

# Import Statements
from length import length_widget
from logo import logo_widget
from width import width_widget


def widgets():
    """Load All Widgets"""
    logo_widget()
    length_widget()
    width_widget()


if __name__ == "__main__":
    widgets()
