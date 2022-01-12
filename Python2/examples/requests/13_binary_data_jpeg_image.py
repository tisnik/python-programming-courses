#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests

# adresa s testovaci REST API sluzbou
URL = "https://httpbin.org/image/jpeg"

# poslani HTTP dotazu typu GET
response = requests.get(URL)

# precteni hlavicek
headers = response.headers

# vypis typu internetoveho media
print("Typ dat:", headers.get("content-type"))

# vypis delky dat predanych v tele
print("Delka dat:", headers.get("content-length"))

print(response.raw)

with open("test1.jpg", "wb") as fout:
    for block in response.iter_content(chunk_size=128):
        fout.write(block)
