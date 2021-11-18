#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import tkinter
from tkinter import ttk

import sys


def exit():
    sys.exit(0)


root = tkinter.Tk()

style = ttk.Style()
style.configure('Yellow.TButton', background='yellow')
style.configure('Red.TButton', background='#ff8080')
style.configure('Blue.TButton', background='#8080ff')
style.configure('Green.TButton', background='#80ff80')

button1 = ttk.Button(root, text="1st btn", style='Yellow.TButton',
                     command=exit)
button2 = ttk.Button(root, text="Second button", style='Red.TButton',
                     command=exit)
button3 = ttk.Button(root, text="Third button",
                     command=exit)
button4 = ttk.Button(root, text="This is fourth button, the last one",
                     command=exit)

button3.configure(style='Green.TButton')

button4["style"] = 'Blue.TButton'

button1.grid(column=1, row=1, sticky="we")
button2.grid(column=2, row=1, sticky="we")
button3.grid(column=1, row=2, sticky="we")
button4.grid(column=2, row=2, sticky="we")

root.mainloop()
