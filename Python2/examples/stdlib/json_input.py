#!/usr/bin/env python3

import json

with open("test.json", "r") as fin:
    data = json.load(fin)
    print(data)
