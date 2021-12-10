#!/usr/bin/env python
# vim: set fileencoding=utf-8

import tkinter
from tkinter import ttk


def test():
    print("Test!")


root = tkinter.Tk()

menubar = tkinter.Menu(root)

image_names = [
    "document-open",
    "document-save",
    "application-exit",
    "edit-undo",
    "edit-cut",
    "edit-copy",
    "edit-paste",
    "edit-delete",
    "edit-select-all"]

images = {}
for image_name in image_names:
    images[image_name] = tkinter.PhotoImage(file="icons/%s.gif" % image_name)

filemenu = tkinter.Menu(menubar, tearoff=0)

filemenu.add_command(label="Open", underline=0, image=images["document-open"],
                     compound="left")

filemenu.add_command(label="Save", underline=0, image=images["document-save"],
                     compound="left")

filemenu.add_separator()

filemenu.add_command(label="Exit", underline=1,
                     image=images["application-exit"], compound="left",
                     command=root.quit)

menubar.add_cascade(label="File", menu=filemenu, underline=0)


editmenu = tkinter.Menu(menubar, tearoff=0)

editmenu.add_command(label="Undo", underline=0, image=images["edit-undo"],
                     compound="left")

editmenu.add_separator()

editmenu.add_command(label="Cut", underline=2, image=images["edit-cut"],
                     compound="left")

editmenu.add_command(label="Copy", underline=0, image=images["edit-copy"],
                     compound="left")

editmenu.add_command(label="Paste", underline=0, image=images["edit-paste"],
                     compound="left")

editmenu.add_command(label="Delete", underline=2, image=images["edit-delete"],
                     compound="left")

editmenu.add_separator()

editmenu.add_command(label="Select All", underline=7,
                     image=images["edit-select-all"], compound="left")

menubar.add_cascade(label="Edit", menu=editmenu, underline=0)


colors = ("white", "yellow", "orange", "red", "magenta",
          "blue", "cyan", "green")
colormenu = tkinter.Menu(menubar, tearoff=0)

for color in colors:
    colormenu.add_command(label=color, background=color)

menubar.add_cascade(label="Colors", menu=colormenu, underline=0)

helpmenu = tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=test, underline=0)
menubar.add_cascade(label="Help", menu=helpmenu, underline=0)

root.config(menu=menubar)

root.mainloop()