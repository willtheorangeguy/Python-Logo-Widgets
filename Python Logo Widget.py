"""
(C) 2016 - 2022. All rights reserved.
"""
#Import Statements
from tkinter import *

#Window Statements
window = Tk()
window.title("Python Logo Widget") # Edit title as needed

#Image Statements
img = PhotoImage(file = "pythonlogogif.gif") # Edit image as needed
label = Label(window, image = img, bg = "black") # Edit border as needed

# Pack Statements
label.pack(side = TOP) # Edit pack as needed

window.mainloop()
