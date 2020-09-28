# coding: utf-8

"""Ukázky použití knihovny Matplotlib při tvorbě různých typů grafů."""

# # Knihovna Matplotlib
# ![matplotlib_logo.png](matplotlib_logo.png)
# ### Autor Pavel Tišnovský, Red Hat
# ### Email ptisnovs@redhat.com

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

# ### Druhý demonstrační příklad:
# - vykreslení a uložení grafu do různých typů souborů

plt.savefig("sinus.png")
plt.savefig("sinus.pdf")
plt.savefig("sinus.eps")
plt.savefig("sinus.ps")
plt.savefig("sinus.svg")

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
