#!/usr/bin/env python
# encoding=utf-8

seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

g1 = list(item for item in seznam)

g2 = list(item*2 for item in seznam)

g3 = list(item for item in seznam if item % 3 == 0)

print(seznam)
print(g1)
print(g2)
print(g3)
