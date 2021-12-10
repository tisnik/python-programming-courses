#!/usr/bin/env python
# vim: set fileencoding=utf-8

import tkinter

import sys

root = tkinter.Tk()

radio_var = tkinter.StringVar()

radio1 = tkinter.Radiobutton(root, variable=radio_var, value="Assembler",
                             text="Assembler")

radio2 = tkinter.Radiobutton(root, variable=radio_var, value="Basic",
                             text="Basic")

radio3 = tkinter.Radiobutton(root, variable=radio_var, value="Brainfuck",
                             text="Brainfuck")

radio4 = tkinter.Radiobutton(root, variable=radio_var, value="C",
                             text="C")

radio5 = tkinter.Radiobutton(root, variable=radio_var, value="Python",
                             text="Python")

showButton = tkinter.Button(root, text="Show var",
                            command=lambda: print(radio_var.get()))

quitButton = tkinter.Button(root, text="Exit", background='#ff8080',
                            command=exit)

radio1.grid(column=1, row=1, sticky="w")
radio2.grid(column=1, row=2, sticky="w")
radio3.grid(column=1, row=3, sticky="w")
radio4.grid(column=1, row=4, sticky="w")
radio5.grid(column=1, row=5, sticky="w")

showButton.grid(column=2, row=6, sticky="we", padx=6, pady=6)
quitButton.grid(column=2, row=7, sticky="we", padx=6, pady=6)

root.mainloop()