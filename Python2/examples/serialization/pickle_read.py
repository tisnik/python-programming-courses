#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Deserializce hodnot ze souboru."""

import pickle

with open("test", "rb") as fin:
    data = pickle.load(fin)
    print(data)
