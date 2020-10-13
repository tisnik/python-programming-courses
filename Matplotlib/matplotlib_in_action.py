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
x = np.linspace(0, 2*np.pi, 100)

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
x = np.linspace(0, 2*np.pi, 100)

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
x = np.linspace(0.01, 2*np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.cos(x)

# hodnoty na y-ové ose: třetí funkce
y3 = np.sin(x)/x

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
x = np.linspace(0, 2*np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.sin(3*x)/(x+1)

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
x = np.linspace(0.001, 2*np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(5*x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.sin(5*x)/(x+1/2)

# hodnoty na y-ové ose: třetí čtvrtá funkce
y3 = 1/(x+1/2)
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
x = np.linspace(0, 2*np.pi, 100)

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
x = np.linspace(0, 2*np.pi, 100)

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
plt.annotate("maximální hodnota sin(x)",
             xy=(np.pi/2, 1.0),
             xytext=(1, 1.3),
             arrowprops=dict(arrowstyle="->"))

# vložit druhý popisek do grafu
plt.annotate("minimální hodnota cos(x)",
             xy=(np.pi, -1.0),
             xytext=(2, -1.3),
             arrowprops=dict(arrowstyle="->"))

# zobrazení grafu
plt.show()

# --------------------------------------------

# ### Devátý demonstrační příklad:
# - základní polární graf

# úhel v polárním grafu
theta = np.linspace(0.01, 2*np.pi, 150)

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
theta = np.linspace(0.01, 2*np.pi, 150)

# první funkce: vzdálenost od středu
radius1 = theta

# druhá funkce: vzdálenost od středu
radius2 = 2*np.abs(theta-np.pi)

# třetí funkce: vzdálenost od středu
radius3 = 2*np.log(theta)

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
theta = np.linspace(0.01, 4*np.pi, 150)

# první funkce: vzdálenost od středu
radius1 = theta

# druhá funkce: vzdálenost od středu
radius2 = 3*np.abs(theta-2*np.pi)

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
x = np.linspace(0.2, 2*np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(5*x)/x
y2 = 1/x
y3 = -y2

# vykreslit průběh funkce
plt.plot(x, y2, color='red',  label='obalka sinc')
plt.plot(x, y3, color='red',  label='obalka sinc')
plt.plot(x, y,  color='blue', label='sinc(x)')

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sinc(x)")

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()
