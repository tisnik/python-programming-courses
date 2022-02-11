# coding: utf-8

"""Ukázky použití knihovny Matplotlib při tvorbě různých typů grafů."""

# # Knihovna Matplotlib
# ![matplotlib_logo.png](matplotlib_logo.png)
# ### Autor Pavel Tišnovský, Red Hat
# ### Email ptisnovs@redhat.com

# ## Knihovna NumPy
# - numerické výpočty
# - typ N-dimenzionální pole a matice
# - neobsahuje přímou podporu pro tvorbu grafů

# ## Knihovna Matplotlib
# - zaměřena explicitně na tvorbu grafů
# - právě vzájemnou kombinací obou knihoven NumPy+matplotlib lze relativně
# snadno dosáhnout velmi pěkných výsledků plně porovnatelných s výsledky
# vytvořenými komerčními balíky.

# ## Možnosti knihovny Matplotlib
# - grafy funkcí typu y = f(x)
# - parametrické zadání 2D průběhu x, y = f(t)
# - grafy funkcí typu z = f(x,y)
# - parametrické zadání 3D průběhu x, y, z = f(t)

# ## Zobrazení grafů
# - na obrazovce
# - do plochy Jupyter Notebooku
# - do rastrových obrázků
# - do vektorových kreseb
# - do PDF

# --------------------------------------------

# ## Praktická část

# Nejprve je nutné naimportovat všechny potřebné funkce a konstanty z balíčku `matplotlib`

# Používají se následující varianty importu
#
# `import matplotlib`
#
# `import matplotlib as plt`
#
# `from matplotlib import *`
#
# `from matplotlib import array, linspace`

# Pro potřeby prezentace naimportujeme všechny funkce a konstanty z knihovny `matplotlib.pyplot`
import matplotlib.pyplot as plt

# Taktéž budeme potřebovat některé funkce z knihovny `numpy`
import numpy as np

# Základní kontrola, jestli se import podařil
import sys

if "matplotlib" not in sys.modules:
    raise Exception("Modul matplotlib nebyl naimportován")
if "numpy" not in sys.modules:
    raise Exception("Modul numpy nebyl naimportován")


# ## Ukázky základních typů grafů

# --------------------------------------------

# ### První demonstrační příklad:
# - vykreslení průběhu funkce sin

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(x)

# vykreslit průběh funkce
plt.plot(x, y)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x)")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Druhý demonstrační příklad:
# - vykreslení a uložení grafu do různých typů souborů

plt.savefig("sinus.png")
plt.savefig("sinus.pdf")
plt.savefig("sinus.eps")
plt.savefig("sinus.ps")
plt.savefig("sinus.svg")

# --------------------------------------------

# ### Třetí demonstrační příklad:
# - vykreslení průběhů funkcí sin a cos do jediného grafu

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.cos(x)

# vykreslit průběh obou funkcí
plt.plot(x, y1, x, y2)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a cos(x)")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Čtvrtý demonstrační příklad:
# - vykreslení průběhů funkcí sin a cos a sinc do jediného grafu
# - změna stylu vykreslování průběhů funkcí

# hodnoty na x-ové ose
x = np.linspace(0.01, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.cos(x)

# hodnoty na y-ové ose: třetí funkce
y3 = np.sin(x) / x

# vykreslit průběh všech tří funkcí
# se změnou stylu vykreslování
plt.plot(x, y1, "b-", label="sin")
plt.plot(x, y2, "r.", label="cos")
plt.plot(x, y3, "g--", label="sinc")

# přidání legendy
plt.legend(loc="lower left")

# popis os
plt.xlabel("x")
plt.ylabel("sin(x), cos(x) a sinc(x)")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Pátý demonstrační příklad:
# - vykreslení průběhů funkcí sin a sinc do jediného grafu s vyplněním plochy pod průběhu

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.sin(3 * x) / (x + 1)

# vykreslit průběh obou funkcí
# se změnou stylu vykreslování
plt.fill(x, y1, "red", x, y2, "yellow", alpha=0.3)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a sinc(3x)")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Šestý demonstrační příklad:
# - vykreslení průběhů čtyř různých funkcí do jediného grafu s vyplněním plochy pod průběhu
# - kombinace různých stylů vykreslení

# hodnoty na x-ové ose
x = np.linspace(0.001, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(5 * x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.sin(5 * x) / (x + 1 / 2)

# hodnoty na y-ové ose: třetí čtvrtá funkce
y3 = 1 / (x + 1 / 2)
y4 = -y3

# vykreslit průběh obou funkcí
# se změnou stylu vykreslování
plt.fill(x, y1, "yellow", alpha=0.3, label="sin x")
plt.fill(x, y2, "r.", alpha=1.0, label="sinc 5x")
plt.plot(x, y3, "g--", label="obalka sinc")
plt.plot(x, y4, "g--", label="obalka sinc")

# přidání legendy
plt.legend(loc="upper right")

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a sinc(3x)")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Sedmý demonstrační příklad:
# - vykreslení průběhů funkcí sin a cos
# - nastavení mřížky
# - nastavení rozsahů na obou osách

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.cos(x)

# vykreslit průběh obou funkcí
# se změnou stylu vykreslování
plt.plot(x, y1, "b-", label="sin")
plt.plot(x, y2, "r-", label="cos")

# přidání legendy
plt.legend(loc="lower left")

# nastavení rozsahů na obou osách
plt.axis([-1, 8, -1.5, 1.5])

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a cos(x)")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Osmý demonstrační příklad:
# - vykreslení průběhů funkcí sin a cos
# - nastavení mřížky
# - nastavení rozsahů na obou osách
# - přidání popisku přímo do grafu

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.cos(x)

# vykreslit průběh obou funkcí
# se změnou stylu vykreslování
plt.plot(x, y1, "b-", label="sin")
plt.plot(x, y2, "r-", label="cos")

# přidání legendy
plt.legend(loc="lower left")

# nastavení rozsahů na obou osách
plt.axis([-1, 8, -1.5, 1.5])

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a cos(x)")

# vložit první popisek do grafu
plt.annotate(
    "maximální hodnota sin(x)",
    xy=(np.pi / 2, 1.0),
    xytext=(1, 1.3),
    arrowprops=dict(arrowstyle="->"),
)

# vložit druhý popisek do grafu
plt.annotate(
    "minimální hodnota cos(x)",
    xy=(np.pi, -1.0),
    xytext=(2, -1.3),
    arrowprops=dict(arrowstyle="->"),
)

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Devátý demonstrační příklad:
# - základní polární graf

# úhel v polárním grafu
theta = np.linspace(0.01, 2 * np.pi, 150)

# vzdálenost od středu
radius = np.log(theta)

ax = plt.subplot(111, projection="polar")

# vykreslit průběh funkce
# v polárním grafu
ax.plot(theta, radius)

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Desátý demonstrační příklad:
# - vykreslení průběhů několika funkcí
# - do polárního grafu

# úhel v polárním grafu
theta = np.linspace(0.01, 2 * np.pi, 150)

# první funkce: vzdálenost od středu
radius1 = theta

# druhá funkce: vzdálenost od středu
radius2 = 2 * np.abs(theta - np.pi)

# třetí funkce: vzdálenost od středu
radius3 = 2 * np.log(theta)

ax = plt.subplot(111, projection="polar")

# vykreslit průběh první funkce
# v polárním grafu
ax.plot(theta, radius1, "r.", label="f1")

# vykreslit průběh druhé funkce
# v polárním grafu
ax.plot(theta, radius2, "g", label="f2")

# vykreslit průběh třetí funkce
# v polárním grafu
ax.plot(theta, radius3, "b--", label="f3")

# přidání legendy
plt.legend(loc="lower left")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Jedenáctý demonstrační příklad:
# - vykreslení průběhů několika funkcí
# - do polárního grafu

# úhel v polárním grafu
theta = np.linspace(0.01, 4 * np.pi, 150)

# první funkce: vzdálenost od středu
radius1 = theta

# druhá funkce: vzdálenost od středu
radius2 = 3 * np.abs(theta - 2 * np.pi)

ax = plt.subplot(111, projection="polar")

# vykreslit průběh první funkce
# v polárním grafu
ax.plot(theta, radius2, "b", label="f1")

# vykreslit průběh druhé funkce
# v polárním grafu
ax.fill(theta, radius1, "yellow", alpha=0.3, label="f1")

# přidání legendy
plt.legend(loc="lower left")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Dvanáctý demonstrační příklad:
# - vykreslení průběhu funkce sinc
# - při vykreslování se jednotlivé body spojí úsečkami

# hodnoty na x-ové ose
x = np.linspace(0.2, 2 * np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(5 * x) / x
y2 = 1 / x
y3 = -y2

# vykreslit průběh funkce
plt.plot(x, y2, color="red", label="obalka sinc")
plt.plot(x, y3, color="red", label="obalka sinc")
plt.plot(x, y, color="blue", label="sinc(x)")

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sinc(x)")

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Třináctý demonstrační příklad:
# - vykreslení průběhu funkce sinc
# - při vykreslování se použijí "schodky"

# hodnoty na x-ové ose
x = np.linspace(0.2, 2 * np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(5 * x) / x
y2 = 1 / x
y3 = -y2

# vykreslit průběh funkce
plt.plot(x, y2, color="red", label="obalka sinc", drawstyle="default")
plt.plot(x, y3, color="red", label="obalka sinc", drawstyle="default")
plt.plot(x, y, color="blue", label="sinc(x)", drawstyle="steps")

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sinc(x)")

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Čtrnáctý demonstrační příklad:
# - jednoduchý sloupcový graf

# historické ceny ropy
cena_ropy = [
    46.68,
    44.68,
    46.90,
    47.15,
    44.59,
    44.00,
    44.63,
    45.92,
    44.15,
    45.94,
    46.05,
    46.75,
    46.25,
    45.41,
    49.20,
    45.22,
    42.56,
    38.60,
    39.31,
    38.24,
    40.45,
    41.32,
    40.80,
    42.62,
    41.87,
    42.50,
    42.23,
    43.30,
    43.08,
    44.96,
    43.87,
    44.66,
    45.15,
    47.12,
    48.52,
    48.79,
    47.98,
    47.39,
    48.14,
    48.45,
]

# počet prvků
N = len(cena_ropy)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 1.00

# sloupcový graf
plt.bar(indexes, cena_ropy, width, color="yellow", edgecolor="black", label="Cena ropy")

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Patnáctý demonstrační příklad:
# - sloupcový graf se dvěma skupinami sloupců

# první pole hodnot
vals1 = [10, 15, 20, 12, 14, 8]

# druhé pole hodnot
vals2 = [19, 18, 6, 11, 6, 14]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# sloupcový graf se dvěma skupinami sloupců
plt.bar(indexes, vals1, width, color="gray", edgecolor="black", label="CPU#1")
# posunuté sloupce
plt.bar(indexes + width, vals2, width, color="red", edgecolor="black", label="CPU#2")

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Šestnáctý demonstrační příklad:
# - jednoduchý histogram

# náhodné hodnoty
y = np.random.normal(0, 0.1, 10000)

plt.hist(y, bins=30, range=None, density=True)

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Sedmnáctý demonstrační příklad:
# - koláčový graf

# musíme naimportovat ještě jeden balíček
from matplotlib import font_manager as fm  # noqa: E402

# make a square figure and axes
fig = plt.figure(1, figsize=(6, 6), dpi=50)
ax = fig.add_axes([0.16, 0.16, 0.68, 0.68])

plt.title("Scripting languages")
ax.title.set_fontsize(30)

# popisky jednotlivých výřezů
labels = ["Perl", "Python", "Ruby"]

# šířky jednotlivých výřezů
fracs = [90, 150, 70]

# vytvoření koláčového grafu
ax.pie(fracs, labels=labels, autopct="%1.1f%%", shadow=True)

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Osmnáctý demonstrační příklad:
# - změna stylu koláčových grafů

# make a square figure and axes
fig = plt.figure(1, figsize=(6, 6), dpi=50)
ax = fig.add_axes([0.16, 0.16, 0.68, 0.68])

plt.title("Scripting languages")
ax.title.set_fontsize(30)

# popisky jednotlivých výřezů
labels = ["Perl", "Python", "Ruby"]

# šířky jednotlivých výřezů
fracs = [90, 150, 70]

# vytáhnutí výřezů
explode = (0.0, 0.0, 0.15)

# barvy
colors = ("yellow", "#60ff60", "red")

# vytvoření koláčového grafu
patches, texts, autotexts = ax.pie(
    fracs, explode=explode, colors=colors, labels=labels, autopct="%1.1f%%", shadow=True
)

# změna stylu písma
proptease = fm.FontProperties()
proptease.set_size("xx-large")
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Devatenáctý demonstrační příklad:
# - sloupcový graf se dvěma skupinami sloupců
#   a se zobrazením odchylek

# první pole hodnot a pole odchylek
vals1 = [10, 15, 20, 12, 14, 8]
delta1 = [1, 2, 3, 4, 5, 0]

# druhé pole hodnot a pole odchylek
vals2 = [19, 18, 6, 11, 6, 14]
delta2 = [4, 2, 3, 2, 2, 4]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# sloupcový graf se dvěma skupinami sloupců
plt.bar(
    indexes, vals1, width, color="gray", edgecolor="black", label="CPU#1", yerr=delta1
)

# posunuté sloupce
plt.bar(
    indexes + width,
    vals2,
    width,
    color="red",
    edgecolor="black",
    label="CPU#2",
    yerr=delta2,
)

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Dvacátý demonstrační příklad:
# - sloupcový graf se dvěma skupinami sloupců
#   a se zobrazením odchylek

# první pole hodnot a pole odchylek
vals1 = [10, 15, 20, 12, 14, 8]
delta1 = [1, 2, 3, 4, 5, 0]

# druhé pole hodnot a pole odchylek
vals2 = [19, 18, 6, 11, 6, 14]
delta2 = [4, 2, 3, 2, 2, 4]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# sloupcový graf se dvěma skupinami sloupců
plt.bar(
    indexes,
    vals1,
    width,
    color="gray",
    edgecolor="black",
    label="CPU#1",
    yerr=delta1,
    error_kw=dict(elinewidth=2, ecolor="red"),
)

# posunuté sloupce
plt.bar(
    indexes + width,
    vals2,
    width,
    color="red",
    edgecolor="black",
    label="CPU#2",
    yerr=delta2,
    error_kw=dict(elinewidth=2, ecolor="black"),
)

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Dvacátý první demonstrační příklad:
# - zobrazení kontur funkce typu z=f(x,y)

# import dvou dalších potřebných knihoven
import matplotlib.cm as cm  # noqa: E402
import matplotlib.mlab as mlab  # noqa: E402


delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R1 = np.sqrt(X * X + Y * Y)

# vzdálenost od bodu [3,3]
R2 = np.sqrt((X - 3) * (X - 3) + (Y - 3) * (Y - 3))

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R1) - np.cos(R2)

# povolení zobrazení mřížky
plt.grid(True)

# vytvoření grafu s konturami funkce z=f(x,y)
plt.contour(X, Y, Z)

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Dvacátý druhý demonstrační příklad:
# - zobrazení kontur funkce typu z=f(x,y)
# - zobrazení hodnot u jednotlivých "vrstevnic"

# hustota mřížky
delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R1 = np.sqrt(X * X + Y * Y)

# vzdálenost od bodu [3,3]
R2 = np.sqrt((X - 3) * (X - 3) + (Y - 3) * (Y - 3))

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R1) - np.cos(R2)

# povolení zobrazení mřížky
plt.grid(True)

# vytvoření grafu s konturami funkce z=f(x,y)
CS = plt.contour(X, Y, Z)

# popisky "vrstevnic"
plt.clabel(CS, inline=1, fontsize=10)

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Dvacátý třetí demonstrační příklad:
# - zobrazení kontur funkce typu z=f(x,y)
# - zobrazení hodnot u jednotlivých "vrstevnic"
# - přidání legendy

# hustota mřížky
delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R1 = np.sqrt(X * X + Y * Y)

# vzdálenost od bodu [3,3]
R2 = np.sqrt((X - 3) * (X - 3) + (Y - 3) * (Y - 3))

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R1) - np.cos(R2)

# povolení zobrazení mřížky
plt.grid(True)

# vytvoření grafu s konturami funkce z=f(x,y)
CS = plt.contour(X, Y, Z)

# přidání legendy (colorbar)
CB = plt.colorbar(CS, shrink=0.7, extend="both")

# popisky "vrstevnic"
plt.clabel(CS, inline=1, fontsize=10)

# zobrazení grafu
plt.show()

# --------------------------------------------
