# Python Logo Widgets Usage

To install the Python Logo Widgets, you can use an executable package (Windows), install from the [Python Package Index](https://pypi.org/), import the widgets into your project, or hard code the widgets into your project.

## Executable Package

1. To run the executable package, download the latest `.zip` file from [GitHub Releases](https://github.com/willtheorangeguy/Python-Logo-Widgets/releases/latest) page.
2. Extract the `.zip` file using a program like [7-Zip](https://www.7-zip.org/).
3. _(Optional) Move the files to `C:\Program Files` and create a shortcut._
4. Double click on `main.exe`.
5. Enjoy the program!

## Python Package Index (`pip`)

1. Download and install [Python](https://www.python.org/downloads/).
2. Open a terminal and run the command: `pip install running-calculator`.
3. Open your code file, and navigate to the top of your code.
4. Add the respective `import` statement:
    * **Python Logo:** `from python-logo-widgets.logo import *`
    * **Python Powered Length:** `from python-logo-widgets.length import *`
    * **Python Powered Width:** `from python-logo-widgets.width import *`

5. Call each of the respective widgets:

    * **Python Logo:** `logo_widget()`
    * **Python Powered Length:** `length_widget()`
    * **Python Powered Width:** `width_widget()`

6. Save and run the file (`F5`).

## Import Modules

1. Copy the `logo.py`, `length.py`, `width.py` files, and `imgs` folder to your project.
2. Import each of the widgets (and `Tkinter`) into your project:

```python
# Import Statements
from tkinter import *
from logo import *
from length import *
from width import *
```

3. Call each of the respective widgets:

    * **Python Logo:** `logo_widget()`
    * **Python Powered Length:** `length_widget()`
    * **Python Powered Width:** `width_widget()`

4. Save and run the file (`F5`).

## Hard Code into Project

1. Create a `imgs` folder in the root directory of your program.
2. Copy the respective image from the Python Logo Widgets `imgs` folder to your program's `imgs` folder.
3. Open the your code file, and navigate to the top of the code.
4. Add the respective `import` statement:
    * **Python Logo:** `from logo import *`
    * **Python Powered Length:** `from length import *`
    * **Python Powered Width:** `from width import *`
5. Copy the respective function to the top of your code file, making it available everywhere else:
    * **Python Logo:**

    ```python
    def logo_widget():
        # Window Statements
        window = Tk()
        window.title("Python Logo Widget") # Edit title as needed

        # Image Statements
        img = PhotoImage(file = "imgs/logo.gif") # Edit image as needed
        label = Label(window, image = img, bg = "black") # Edit border as needed

        # Pack Statements
        label.pack(side = BOTTOM) # Edit pack as needed

        # Sustain Window
        window.mainloop()
    ```

    * **Python Powered Length:**

    ```python
    def length_widget():
        # Window Statements
        window = Tk()
        window.title("Python Powered Widget") # Edit title as needed

        # Image Statements
        img = PhotoImage(file = "imgs/length.gif") # Edit image as needed
        label = Label(window, image = img, bg = "black") # Edit border as needed

        # Pack Statements
        label.pack(side = BOTTOM) # Edit pack as needed

        # Sustain Window
        window.mainloop()
    ```

    * **Python Powered Width:**

    ```python
    def width_widget():
        # Window Statements
        window = Tk()
        window.title("Python Powered Widget") # Edit title as needed

        # Image Statements
        img = PhotoImage(file = "imgs/width.gif") # Edit image as needed
        label = Label(window, image = img, bg = "black") # Edit border as needed

        # Pack Statements
        label.pack(side = BOTTOM) # Edit pack as needed

        # Sustain Window
        window.mainloop()
    ```

6. Edit the `label.pack()` statement to pack it either at the `TOP`, `BOTTOM`, `LEFT` or `RIGHT` of your program window.
7. Call each of the respective widgets:

    * **Python Logo:** `logo_widget()`
    * **Python Powered Length:** `length_widget()`
    * **Python Powered Width:** `width_widget()`

8. Save and run the file (`F5`).
