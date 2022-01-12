#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Serializce hodnot do souboru."""

import pickle

data = {"x": "Hello", "y": "world", "z": [1, 2, 3, 4], "w": (1, 2, 3, 4)}

with open("test", "wb") as fout:
    pickle.dump(data, fout)
