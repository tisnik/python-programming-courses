#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import tkinter
from tkinter import ttk

import sys

root = tkinter.Tk()

label = ttk.Label(root, text="Hello world!")
button = ttk.Button(root, text="Close window", command=lambda: sys.exit(0))

label.pack()
button.pack()

root.mainloop()
