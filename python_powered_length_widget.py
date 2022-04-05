"""
Python Powered Length Widget
(C) 2016 - 2022. All rights reserved.
"""
# Import Statements
from tkinter import *

def python_powered_length():
    # Window Statements
    window = Tk()
    window.title("Python Powered Widget") # Edit title as needed

    # Image Statements
    img = PhotoImage(file = "logos/pythonpoweredlengthgif.gif") # Edit image as needed
    label = Label(window, image = img, bg = "black") # Edit border as needed

    # Pack Statements
    label.pack(side = TOP) # Edit pack as needed

    # Sustain Window
    window.mainloop()

if __name__ == "__main__":
    python_powered_length()
