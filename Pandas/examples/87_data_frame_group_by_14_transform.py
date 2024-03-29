#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

# přečtení zdrojových dat s jejich konverzí do datového rámce
df = pandas.read_csv("denni_kurz2.txt", sep="|", skiprows=0)

# převod číselných hodnot
df["kurz"] = pandas.to_numeric(df["kurz"].str.replace(",", "."), errors="coerce")

df["datum"] = pandas.to_datetime(df["datum"])

# datový rámec zobrazíme
print(df)
print()

# rozdělení do skupin podle data
gb = df.groupby(["kód"])

# nový sloupec
df["rozdíl"] = gb["kurz"].transform(lambda x: x.max() - x.min())

print(df[0:10])
print()
print(df[33:43])
