#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Funkce vyššího řádu map."""

x = range(10)

print(x)

y = map(lambda value: value * 2, x)
print(list(y))
