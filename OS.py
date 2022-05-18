from tkinter import *
import os

def shutdown ():
    return os.system ("sudo shutdown -h now")

def restart ():
    return os.system ("sudo shutdown -r now")

def sleep ():
    return os.system ("sudo shutdown -s now")

root = Tk ()
root.configure (background="#B0C4DE")
root.title ("MacOS")
root.resizable (width=False, height=False)

Button (root, text="Shutdown", command=shutdown).grid (row=0, column=0)
Button (root, text="Restart", command=restart).grid (row=1, column=0)
Button (root, text="Sleep", command=sleep).grid (row=2, column=0)

root.mainloop ()
