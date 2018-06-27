#!/usr/bin/env python
# encoding=utf-8

calls = 0


def ackermann(m, n):
    """Rekurzivní výpočet Ackermannovy funkce."""
    global calls
    calls += 1
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(3, 4))
