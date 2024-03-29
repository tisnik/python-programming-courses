#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import tkinter
from tkinter import ttk

import sys

root = tkinter.Tk()

style = ttk.Style()
style.theme_use("alt")
style.configure("Red.TButton", background="#ff8080")

value = tkinter.StringVar()

entry = ttk.Entry(root, textvariable=value)
entry.insert(0, "xyzzy")

showButton = ttk.Button(root, text="Show var", command=lambda: print(value.get()))

quitButton = ttk.Button(root, text="Exit", style="Red.TButton", command=exit)

entry.grid(column=1, row=1, sticky="we", padx=6, pady=6)
showButton.grid(column=1, row=2, sticky="we", padx=6, pady=6)
quitButton.grid(column=1, row=3, sticky="we", padx=6, pady=6)

root.mainloop()
