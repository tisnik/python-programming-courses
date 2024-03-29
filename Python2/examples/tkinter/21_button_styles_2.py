#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import tkinter
from tkinter import ttk

import sys


def exit():
    sys.exit(0)


root = tkinter.Tk()

style = ttk.Style()
style.configure("Red.TButton", background="#ff8080")

buttonStyles = ("sunken", "solid", "flat", "groove", "raised", "ridge")

buttons = (
    tkinter.Button(root, text=buttonStyle, relief=buttonStyle)
    for buttonStyle in buttonStyles
)

quitButton = ttk.Button(root, text="Exit", style="Red.TButton", command=exit)

for i, button in enumerate(buttons):
    button.grid(column=1, row=i, sticky="we")

quitButton.grid(column=2, row=6, sticky="we")

root.mainloop()
