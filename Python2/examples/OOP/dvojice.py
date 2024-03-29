#!/usr/bin/env python


class Dvojice:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "Dvojice: {} {}".format(self.x, self.y)

    def __add__(self, other):
        return Dvojice(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y


d1 = Dvojice(10, 10)
d2 = Dvojice(1, 2)

print(d1)
print(d2)

d3 = d1 + d2
d3 = d1.__add__(d2)
d3 = Dvojice.__add__(d1, d2)

d4 = Dvojice(11, 12)
print(d3)
print(d4)
print(d3 == d4)
