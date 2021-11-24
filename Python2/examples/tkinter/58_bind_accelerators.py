#!/usr/bin/env python
# vim: set fileencoding=utf-8

import tkinter
from tkinter import ttk


def cmd_open():
    print("Open")


def cmd_save():
    print("Save")


def cmd_undo():
    print("Undo")


def cmd_help():
    print("Help")


root = tkinter.Tk()

menubar = tkinter.Menu(root)

filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", underline=0, accelerator="Ctrl+O",
                     command=cmd_open)
filemenu.add_command(label="Save", underline=0, accelerator="Ctrl+S",
                     command=cmd_save)
filemenu.add_separator()
filemenu.add_command(label="Exit", underline=1, accelerator="Ctrl+Q",
                     command=root.quit)
menubar.add_cascade(label="File", menu=filemenu, underline=0)

editmenu = tkinter.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", underline=0, accelerator="Ctrl+U",
                     command=cmd_undo)
editmenu.add_separator()
editmenu.add_command(label="Cut", underline=2, accelerator="Ctrl+X",
                     command=lambda: print("Cut"))
editmenu.add_command(label="Copy", underline=0, accelerator="Ctrl+C",
                     command=lambda: print("Copy"))
editmenu.add_command(label="Paste", underline=0, accelerator="Ctrl+V",
                     command=lambda: print("Paste"))
editmenu.add_command(label="Delete", underline=2,
                     command=lambda: print("Delete"))
editmenu.add_separator()
editmenu.add_command(label="Select All", underline=7, accelerator="Ctrl+A",
                     command=lambda: print("Select All"))
menubar.add_cascade(label="Edit", menu=editmenu, underline=0)

helpmenu = tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", underline=0, accelerator="F1",
                     command=cmd_help)
menubar.add_cascade(label="Help", menu=helpmenu, underline=0)

root.config(menu=menubar)

root.bind('<Control-o>', lambda event: cmd_open())
root.bind('<Control-s>', lambda event: cmd_save())
root.bind('<Control-u>', lambda event: cmd_undo())
root.bind('<F1>', lambda event: cmd_help())

root.mainloop()
