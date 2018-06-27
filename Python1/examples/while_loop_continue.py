#!/usr/bin/env python3
# vim: set fileencoding=utf-8

x = 1

while True:
    if x > 1000:
        break
    x *= 2
    if x < 100:
        continue
    print(x)
