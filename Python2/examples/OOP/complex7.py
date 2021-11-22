#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Metoda __repr__."""


class Complex:
    """Třída představující komplexní čísla."""

    def __init__(self, real=0, imag=0):
        """Konstruktor."""
        self._real = real
        self._imag = imag

    def __str__(self):
        return "{r} + {i}j".format(r=self._real, i=self._imag)

    def __repr__(self):
        return "Complex({r}, {i})".format(r=self._real, i=self._imag)

    def __eq__(self, other):
        return self._real == other._real and self._imag == other._imag

    def __add__(self, other):
        r = self._real + other._real
        i = self._imag + other._imag
        return Complex(r, i)

    def __iadd__(self, other):
        self._real += other._real
        self._imag += other._imag
        return self

    def __neg__(self):
        r = self._real
        i = self._imag
        return Complex(-r, -i)


c1 = Complex(1, 2)
c2 = Complex(10, 20)

c3 = c1 + c2
print(c3)

print(c3)

print(c3.__repr__())
