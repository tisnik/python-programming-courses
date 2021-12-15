#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Funkce vyššího řádu reduce."""

from functools import reduce

x = range(1, 11)

print(x)

y = reduce(lambda a, b: a * b, x)
print(y)
