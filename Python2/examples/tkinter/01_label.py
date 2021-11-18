#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import tkinter
from tkinter import ttk

root = tkinter.Tk()

label = ttk.Label(root, text="Hello world!")

label.pack()

root.mainloop()
