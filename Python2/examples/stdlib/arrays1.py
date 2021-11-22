#!/usr/bin/env python3

"""Základní způsob použití modulu `array`."""

from array import array

a1 = array('l')
a2 = array('u', 'hello \u2567')
a3 = array('l', [1, 2, 3, 4, 5])
a4 = array('d', [1.0, 2.0, 3.14])

print(a1)
print(a2)
print(a3)
print(a4)

a3[3] = -1
print(a3)
