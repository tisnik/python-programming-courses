#!/usr/bin/env python3

"""Základní způsob použití modulu `array` - čtení polí ze souboru."""

from array import array

a1 = array("l")
a2 = array("u")
a3 = array("l")
a4 = array("d")


with open("a1", "rb") as fin:
    a1.fromfile(fin, 0)

with open("a2", "rb") as fin:
    a2.fromfile(fin, 5)

with open("a3", "rb") as fin:
    a3.fromfile(fin, 5)

with open("a4", "rb") as fin:
    a4.fromfile(fin, 3)

print(a1)
print(a2)
print(a3)
print(a4)

print(a1.buffer_info()[1] * a1.itemsize)
print(a2.buffer_info()[1] * a2.itemsize)
print(a3.buffer_info()[1] * a3.itemsize)
print(a4.buffer_info()[1] * a4.itemsize)
