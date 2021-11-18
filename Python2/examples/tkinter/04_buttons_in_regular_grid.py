#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import tkinter
from tkinter import ttk

import sys

root = tkinter.Tk()

button1 = ttk.Button(root, text="First button")
button2 = ttk.Button(root, text="Second button")
button3 = ttk.Button(root, text="Third button")
button4 = ttk.Button(root, text="Fourth button")

button1.grid(column=1, row=1)
button2.grid(column=2, row=1)
button3.grid(column=1, row=2)
button4.grid(column=2, row=2)

root.mainloop()
