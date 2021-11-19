#!/usr/bin/env python3

import json

data = {
        "x": 42,
        "y": [1, 2, 3, 4],
        "z": (1, 2, 3, 4),
        "w": "foobar"
        }

with open("test.json", "w") as fout:
    json.dump(data, fout)
