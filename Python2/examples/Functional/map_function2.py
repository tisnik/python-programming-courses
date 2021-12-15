#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Funkce vyššího řádu map."""


def inc(x):
    return x + 1


x = range(10)

print(x)

y = map(inc, x)
print(list(y))
