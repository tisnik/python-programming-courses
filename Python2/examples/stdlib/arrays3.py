#!/usr/bin/env python3

"""Základní způsob použití modulu `array` - zápis polí do souboru."""

from array import array

a1 = array("l")
a2 = array("u", "hello \u2567")
a3 = array("l", [1, 2, 3, 4, 5])
a4 = array("d", [1.0, 2.0, 3.14])

with open("a1", "wb") as fout:
    a1.tofile(fout)

with open("a2", "wb") as fout:
    a2.tofile(fout)

with open("a3", "wb") as fout:
    a3.tofile(fout)

with open("a4", "wb") as fout:
    a4.tofile(fout)
