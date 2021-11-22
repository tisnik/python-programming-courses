#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Čtení prvků z databáze."""

import shelve

with shelve.open("test") as db:
    print(db["x"])
    print(db["y"])
    print(db["z"])
