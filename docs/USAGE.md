# Python Logo Widgets Usage

To install the Python Logo Widgets, you can either use an executable package (Windows), import the modules into your project or hard-code them into your project (Windows, macOS, Linux). This will require a [text editor](https://code.visualstudio.com/).

Use the following table to see which files are necessary to support each widget:

|        | Python Logo | Python Powered Length | Python Powered Width |
|--------|-------------|-----------------------|----------------------|
|Image|`pythonlogogif`|`pythonpoweredlengthgif`|`pythonpoweredwidthgif`|
|File|`logo_widget` |`python_powered_length_widget`|`python_powered_width_widget`|
|Function|`logo()` |`python_powered_length()`|`python_powered_width()`|

## Executable Package

1. To run the executable package, download the latest `.zip` file from [GitHub Releases](https://github.com/willtheorangeguy/Python-Logo-Widgets/releases/latest) page.
2. Extract the `.zip` file using a program like [7-Zip](https://www.7-zip.org/).
3. _(Optional) Move the files to `C:\Program Files` and create a shortcut._
4. Double click on `main.exe`.
5. Enjoy the program!

## Import Modules

1. Copy the `logo_widget.py`, `python_powered_length_widget.py`, `python_powered_width_widget.py` files, and `logos` folder to your project.
2. Import each of the widgets (and `Tkinter`) into your project:

```python
# Import Statements
from tkinter import *
from logo_widget import *
from python_powered_length_widget import *
from python_powered_width_widget import *
```

3. Call each of the respective widgets:

| Python Logo | Python Powered Length | Python Powered Width |
|-------------|-----------------------|----------------------|
|`logo()` |`python_powered_length()`|`python_powered_width()`|

4. Save and run the file (`F5`).

## Hard Code into Project

1. Create a `logo` folder in the root directory of your program.
2. Copy the respective image from the Python Logo Widgets `logo` folder to your program `logo` folder.
3. Open the your code file, and navigate to the top of the code.
4. Add the respective `import` statement:
    * **Python Logo:** `from logo_widget import *`
    * **Python Powered Length:** `from python_powered_length_widget import *`
    * **Python Powered Width:** `from python_powered_width_widget import *`
5. Copy the respective function to the top of your code file, making it available everywhere else:
    * **Python Logo:**

    ```python
    def logo():
        # Image Statements
        img = PhotoImage(file = "logos/pythonlogogif.gif") # Edit image as needed
        label = Label(window, image = img, bg = "black") # Edit border as needed

        # Pack Statements
        label.pack(side = TOP) # Edit pack as needed
    ```

    * **Python Powered Length:**

    ```python
    def python_powered_length():
        # Image Statements
        img = PhotoImage(file = "logos/pythonpoweredlengthgif.gif") # Edit image as needed
        label = Label(window, image = img, bg = "black") # Edit border as needed

        # Pack Statements
        label.pack(side = TOP) # Edit pack as needed
    ```

    * **Python Powered Width:**

    ```python
    def python_powered_width():
        # Image Statements
        img = PhotoImage(file = "logos/pythonpoweredwidthgif.gif") # Edit image as needed
        label = Label(window, image = img, bg = "black") # Edit border as needed

        # Pack Statements
        label.pack(side = TOP) # Edit pack as needed
    ```

6. Edit the `label.pack()` statement to pack it either at the `TOP`, `BOTTOM`, `LEFT` or `RIGHT` of your program window.
7. Save and run your program (`F5`).