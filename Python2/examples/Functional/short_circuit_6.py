#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zkrácené vyhodnocení logických operátorů."""


def x():
    print("x() called")
    return True


def y():
    print("y() called")
    return False


if x() and y():
    print("if branch")
else:
    print("else branch")
