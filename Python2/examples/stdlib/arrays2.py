#!/usr/bin/env python3

"""Základní způsob použití modulu `array` - celočíselné typy."""

from array import array

input_data = [i for i in range(0, 10)]

a1 = array('b', input_data)
a2 = array('B', input_data)
a3 = array('h', input_data)
a4 = array('H', input_data)
a5 = array('i', input_data)
a6 = array('I', input_data)
a7 = array('l', input_data)
a8 = array('L', input_data)

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)
print(a8)

print(a1.buffer_info()[1]*a1.itemsize)
print(a2.buffer_info()[1]*a2.itemsize)
print(a3.buffer_info()[1]*a3.itemsize)
print(a4.buffer_info()[1]*a4.itemsize)
print(a5.buffer_info()[1]*a5.itemsize)
print(a6.buffer_info()[1]*a6.itemsize)
print(a7.buffer_info()[1]*a7.itemsize)
print(a8.buffer_info()[1]*a8.itemsize)
