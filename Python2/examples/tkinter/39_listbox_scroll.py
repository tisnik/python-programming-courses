#!/usr/bin/env python
# vim: set fileencoding=utf-8

import tkinter
from tkinter import ttk

import sys

root = tkinter.Tk()

scrollbar = tkinter.Scrollbar(root)

langs = (
    "Assembler",
    "Basic",
    "Brainfuck",
    "C",
    "C++",
    "Java",
    "Julia",
    "Perl",
    "Python",
)

listbox = tkinter.Listbox(root, height=4)


for lang in langs:
    listbox.insert(tkinter.END, lang)


def on_listbox_select(event):
    index = listbox.curselection()[0]
    global langs
    print(langs[index])


listbox.bind("<<ListboxSelect>>", on_listbox_select)

quitButton = ttk.Button(root, text="Exit", command=exit)

listbox.grid(column=1, row=1, sticky="nswe")
scrollbar.grid(column=2, row=1, sticky="ns")
quitButton.grid(column=1, row=2)

root.mainloop()
