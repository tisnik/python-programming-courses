#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# omezení hodnot
df["Ratings"] = df["Ratings"].combine(10, min)

# omezení hodnot
df["Ratings"] = df["Ratings"].combine(2, max)

# datový rámec zobrazíme
print(df)
print()

# podrobnější informace o datovém rámci
print(df.dtypes)
print()

# více podrobnějších informací o datovém rámci
print(df.info())
print()
