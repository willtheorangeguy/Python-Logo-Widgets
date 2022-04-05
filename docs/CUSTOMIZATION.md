# Python Logo Widgets Customization

You can easily update and customize the Python Logo Widgets. This will require a [text editor](https://code.visualstudio.com/).

Use the following table to see which files are necessary to support each widget:

|        | Python Logo | Python Powered Length | Python Powered Width |
|--------|-------------|-----------------------|----------------------|
|Image|`pythonlogogif`|`pythonpoweredlengthgif`|`pythonpoweredwidthgif`|
|File|`logo_widget` |`python_powered_length_widget`|`python_powered_width_widget`|
|Function|`logo()` |`python_powered_length()`|`python_powered_width()`|

## Change the Window Title

1. Open the respective Python file.
2. Navigate to the line beginning with `window.title`.
3. Edit the text between the `" "` with the new window title.
4. Save and run the program (`F5`).

## Change Image

1. Download the image (with the author's permission), **as a `.gif` file.**
2. Save the image to the `logos` folder in your program's root directory.
3. Open the respective Python file.
4. Navigate to the line beginning with `img`.
5. Edit the text between the `file = " "` with the new path to the image.
6. Save and run the program (`F5`).

## Change Image Style

1. Open the respective Python file.
2. Navigate to the line beginning with `label`.
3. Edit the text between the `bg = " "` with a different image background color.
4. _Optional:_ Add other customization options found in the [Python `Tkinter` docs](https://docs.python.org/3/library/tkinter.html#).
5. Save and run the program (`F5`).
