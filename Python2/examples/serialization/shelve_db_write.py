#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zápis prvků do databáze."""

import shelve

with shelve.open("test") as db:
    db["x"] = "Hello"
    db["y"] = "world"
    db["z"] = [1, 2, 3, 4]
