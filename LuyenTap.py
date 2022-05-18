from tkinter import *
from tkinter.ttk import *

root = Tk ()
root.title ("First program")

label = Label (root, text = "Hello World!").pack ()

button = Button (root, text="OK").pack ()

text = Text (root).pack ()





root.mainloop ()