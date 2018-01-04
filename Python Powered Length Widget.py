"""
(C) 2016 willtheorangeguy. All rights reserved.
"""
#Import Statements
from tkinter import *

#Window Statements
window = Tk()
window.title("Python Powered Widget") # Edit title as needed

#Image Statements
img = PhotoImage(file = "pythonpoweredlengthgif.gif") # Edit image as needed
label = Label(window, image = img, bg = "black") # Edit border as needed

# Pack Statements
label.pack(side = TOP) # Edit pack as needed

window.mainloop()

                  
