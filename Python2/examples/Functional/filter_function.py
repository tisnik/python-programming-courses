#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Funkce vyššího řádu filter."""

x = range(20)

print(x)

y = filter(lambda value: value % 3 == 0, x)
print(list(y))
