#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import tkinter

import sys

root = tkinter.Tk()

button1 = tkinter.Button(root, background='yellow', text="1st btn",
                         command=lambda: sys.exit(0))
button2 = tkinter.Button(root, background='#ff8080', text="Second button",
                         command=lambda: sys.exit(0))
button3 = tkinter.Button(root, text="Third button",
                         command=lambda: sys.exit(0))
button4 = tkinter.Button(root, text="This is fourth button, the last one",
                         command=lambda: sys.exit(0))

button3.configure(background='#8080ff')
button4['background'] = '#80ff80'

button1.grid(column=1, row=1, sticky="we")
button2.grid(column=2, row=1, sticky="we")
button3.grid(column=1, row=2, sticky="we")
button4.grid(column=2, row=2, sticky="we")

root.mainloop()
