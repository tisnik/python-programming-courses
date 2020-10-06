# coding: utf-8

"""Ukázky použití knihovny NumPy."""

# # Knihovna NumPy
# ![numpy_logo.png](numpy_logo.png)
# ### Autor Pavel Tišnovský, Red Hat
# ### Email ptisnovs@redhat.com

# # Obsah přednášky
# 1. Programovací jazyk Python
# 1. Knihovna NumPy
# 1. Skalární datové typy
# 1. Datová struktura ndarray
# 1. Tvar (shape) n-dimenzionálního pole
# 1. Konstruktory datové struktury ndarray
#     - numpy.array
#     - numpy.zeros
#     - numpy.ones
#     - numpy.eye
#     - numpy.arange
#     - numpy.linspace
#     - numpy.geomspace
#     - numpy.logspace
# 1. Základní operace s n-dimenzionálními poli
#     - přetypování prvků v poli
#     - zjištění tvaru pole
#     - změna tvaru pole
#     - výběr prvků v poli
#     - slicing
# 1. Další operace s n-dimenzionálními poli
#     - operátory
#     - násobení matic
#     - determinant
#     - inverzní matice
#     - filtrace
# 1. Využití matic
#     - vyřešení systému lineárních rovnic
# 1. Další podbalíčky, které nalezneme v knihovně ndarray
# 1. Odkazy na další informační zdroje

# # Programovací jazyk Python
# ![python.png](python.png)

# - Dnes jeden z nejpopulárnějších programovacích jazyků
#     - viz například TIOBE programming community index
#         - <https://www.tiobe.com/tiobe-index/>
#     - Popř. statistika dostupná na OpenHubu
#         - <https://www.openhub.net/languages/compare>
# - Dostupnost na většině platforem
#     - na některých MCU jako MicroPython
# - P̶y̶t̶h̶o̶n̶ ̶2̶ Python 3
#     - všechny ukázky pro Python 3.6+

# ## Programovací jazyk Python
# - Typické použití Pythonu
#     - Nástroje a utility ovládané z příkazového řádku
#     - Aplikace s grafickým uživatelským rozhraním
#     - Client-server
#         - serverová část (Flask, Django, CherryPy, ...)
#         - klient (Brython, spíše technologické demo)
#     - Numerické výpočty, symbolické výpočty
#         - NumPy
#         - SciPy
#         - Matplotlib
#     - Moderní způsoby využití Pythonu
#         - AI
#         - Machine Learning (Deep Learning)
#         - PyTorch
#         - Big data
#     - Tzv. „glue“ jazyk
#     - Vestavitelný interpret Pythonu

# ## Knihovna NumPy
# - Výslovnosti
#     - [nəmpᴧɪ]
#     - [nəmpi]
# - Historie
#     - matrix package
#     - Numeric
#     - NumPy
# - Podpora pro n-dimenzionální pole
#     - + nové funkce
#     - + nové (přetížené) operátory
# - Kooperace s dalšími knihovnami a frameworky
#     - SciPy
#     - Matplotlib
#     - OpenCV

# ## Skalární datové typy
# - <https://docs.scipy.org/doc/numpy/user/basics.types.html>
# ```
# ╔════════════╤═══════════════════════════╤═══════════════════════════════╗
# ║ Formát     │ Popis                     │ Rozsah                        ║
# ╟────────────┼───────────────────────────┼───────────────────────────────╢
# ║ bool       │ uloženo po bajtech        │  True/False                   ║
# ╟────────────┼───────────────────────────┼───────────────────────────────╢
# ║ int8       │ celočíselný se znaménkem  │ -128..127                     ║
# ║ int16      │ celočíselný se znaménkem  │ -32768..32767                 ║
# ║ int32      │ celočíselný se znaménkem  │ -2147483648..2147483647       ║
# ║ int64      │ celočíselný se znaménkem  │ -9223372036854775808..        ║
# ║            │                           │  9223372036854775807          ║
# ╟────────────┼───────────────────────────┼───────────────────────────────╢
# ║ uint8      │ celočíselný bez znaménka  │  0..255                       ║
# ║ uint16     │ celočíselný bez znaménka  │  0..65535                     ║
# ║ uint32     │ celočíselný bez znaménka  │  0..4294967295                ║
# ║ uint64     │ celočíselný bez znaménka  │  0..18446744073709551615      ║
# ╟────────────┼───────────────────────────┼───────────────────────────────╢
# ║ float16    │ plovoucí řádová čárka     │  poloviční přesnost (half)    ║
# ║ float32    │ plovoucí řádová čárka     │  jednoduchá přesnost (single) ║
# ║ float64    │ plovoucí řádová čárka     │  dvojitá přesnost (double)    ║
# ╟────────────┼───────────────────────────┼───────────────────────────────╢
# ║ complex64  │ komplexní číslo (dvojice) │  2×float32                    ║
# ║ complex128 │ komplexní číslo (dvojice) │  2×float64                    ║
# ╚════════════╧═══════════════════════════╧═══════════════════════════════╝
# ```

# ## Kódy skalárních datových typů
# - jednoznakové kódy je možné použít namísto jména typu
# ```
# ╔════════════╤══════╗
# ║  Formát    │ Kód  ║
# ╟────────────┼──────╢
# ║ formát     │ kód  ║
# ║ bool       │ '?'  ║
# ║ int8       │ 'b'  ║
# ║ int16      │ 'h'  ║
# ║ int32      │ 'i'  ║
# ║ int64      │ 'l'  ║
# ║ uint8      │ 'B'  ║
# ║ uint16     │ 'H'  ║
# ║ uint32     │ 'I'  ║
# ║ uint64     │ 'L'  ║
# ║ float16    │ 'e'  ║
# ║ float32    │ 'f'  ║
# ║ float64    │ 'd'  ║
# ║ complex64  │ 'F'  ║
# ║ complex128 │ 'D'  ║
# ╚════════════╧══════╝
# ```

# ## Datový typ single
# ```
# Celkový počet bitů (bytů):   32 (4)
# Bitů pro znaménko:            1
# Bitů pro exponent:            8
# Bitů pro mantisu:            23
# ```

# ## Datový typ double
# ```
# Celkový počet bitů (bytů):   64 (8)
# Bitů pro znaménko:            1
# Bitů pro exponent:           11
# Bitů pro mantisu:            52
# ```

# ## Datový typ float16
# ```
# Celkový počet bitů (bytů):   16 (2)
# Bitů pro znaménko:            1
# Bitů pro exponent:            5
# Bitů pro mantisu:            10
# BIAS (offset exponentu):     15
# Přesnost:                    5-6 číslic
# Maximální hodnota:           65504
# Minimální hodnota:          -65504
# Nejmenší kladná nenulová hodnota:      5,960×10⁻⁸
# Nejmenší kladná normalizovaná hodnota: 6,104×10⁻⁵
# ```

# ## N-dimenzionální pole
# ![numpy_arrays.png](numpy_arrays.png)

# ## Datová struktura ndarray
# - Představuje obecné n-dimenzionální pole
# - Interní způsob uložení dat zcela odlišný od Pythonovských seznamů či n-tic
#     - „pohled“ na kontinuální blok hodnot
# - Homogenní datová struktura
#     - menší flexibilita
#     - menší paměťové nároky
#     - vyšší výpočetní rychlost díky použití nativního kódu
#     - obecně lepší využití cache a rychlejší přístup k prvkům
# - Základní strukturovaný datový typ knihovny NumPy
# - Volitelný počet dimenzí
#     - vektory
#     - matice
#     - pole s větším počtem dimenzí
# - Volitelný typ prvků
# - Volitelné uspořádání prvků
#     - podle zvyklostí jazyka Fortran
#     - podle zvyklostí jazyka C

# ## Tvar (shape) n-dimenzionálního pole
# - Popisuje organizaci a uspořádání prvků v poli
#     - n-tice obsahující rozměry pole v jednotlivých dimenzích
# - Příklady tvarů
#     - `(10,)` - vektor s deseti prvky
#     - `(2, 3)` - dvourozměrná matice se dvěma řádky a třemi sloupci
#     - `(2, 3, 4)` - trojrozměrné pole
# - Tvar je možné zjistit
#     - atribut „shape“
#     - funkce `numpy.shape()`
# - Tvar je možné změnit
#     - funkce `numpy.reshape()`

# ## Konstrukce n-dimenzionálních polí
# - Několik typů konstruktorů
#     - `numpy.array()`
#     - `numpy.zeros()`
#     - `numpy.ones()`
#     - `numpy.full()`
#     - `numpy.eye()`
#     - `numpy.arange()`
#     - `numpy.linspace()`
#     - `numpy.geomspace()`
#     - `numpy.logspace()`
# - Konverzní funkce
#     - `numpy.matrix()`

# ## Konstruktor numpy.array
# - parametry
# `array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)`

# ## Order
# ```
# ╔═════════╤════════════════════════════════════╗
# ║ Hodnota │ Význam                             ║
# ╟─────────┼────────────────────────────────────╢
# ║ 'C'     │ prvky jsou interně uspořádány jako ║
# ║         │ v programovacím jazyku C           ║
# ║         │                                    ║
# ║ 'F'     │ prvky jsou interně uspořádány jako ║
# ║         │ v programovacím jazyku Fortran     ║
# ║         │                                    ║
# ║ 'A'     │ ponecháme na implementaci, který   ║
# ║         │ způsob uspořádání interně zvolit   ║
# ╚═════════╧════════════════════════════════════╝
# ```

# ## Order - rozdíl v uspořádání
# - 2D matice tak, jak ji vidí uživatel (logická struktura)
# ```
# | 1 2 3 |
# | 4 5 6 |
# | 7 8 9 |
# ```

# - Uložení v operační paměti
# ```
# 1 2 3 4 5 6 7 8 9 - 'C'
# 1 4 7 2 5 8 3 6 9 - 'F'
# ```

# --------------------------------------------

# ## Praktická část

# Nejprve je nutné naimportovat všechny potřebné funkce a konstanty z balíčku `numpy`

# Používají se následující varianty importu
#
# `import numpy`
#
# `import numpy as np`
#
# `from numpy import *`
#
# `from numpy import array, linspace`

# Pro potřeby prezentace naimportujeme všechny funkce a konstanty přímo do našeho jmenného prostoru
from numpy import *

# Základní kontrola, jestli se import podařil
import sys
if "numpy" not in sys.modules:
    raise Exception("Modul numpy nebyl naimportován")

# ## Příklady použití funkce `numpy.array()`

# ### Nejprve pro jistotu zjistíme, jestli je funkce `array` volatelná
if "array" not in globals():
    raise Exception("Symbol array neexistuje")
if not callable(array):
    raise Exception("Nelze volat funkci array")

# ### Vytvoření pole ze seznamu
a = array([1, 2, 3, 4])

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Vytvoření pole z generátoru `range`

# konstrukce pole
a = array(range(10))

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Explicitní specifikace typu všech prvků pole
# (interně se provádí přetypování)

# konstrukce pole
a = array(range(10), dtype=float)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Explicitní specifikace uspořádání prvků pole
# (nemá velký význam pro 1D pole=vektory)

# konstrukce pole
a = array(range(10), order='C')

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Explicitní specifikace uspořádání prvků pole
# (nemá velký význam pro 1D pole=vektory)

# konstrukce pole
a = array(range(10), order='F')

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Vytvoření dvourozměrné matice
# konstrukce pole
a = array([[1, 2, 3], [4, 5, 6]])

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ## Konstruktor `numpy.zeros`
# - Vektor nebo matice s nulovými prvky
# - Poměrně častý požadavek v praxi
#     - opět lze zvolit interní uspořádání prvků
# ### Volání konstruktoru numpy.zeros
# `zeros(shape, dtype=float, order='C')`

# ## Příklady použití funkce `numpy.zeros()`

# ### Nejprve pro jistotu zjistíme, jestli je funkce `zeros` volatelná
if "zeros" not in globals():
    raise Exception("Symbol zeros neexistuje")
if not callable(zeros):
    raise Exception("Nelze volat funkci zeros")

# ### Jednorozměrný vektor s jediným prvkem

# konstrukce pole
a = zeros(1)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Jednorozměrný vektor s deseti prvky

# konstrukce pole
a = zeros(10)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Matice o velikosti 5x5 prvků, každý prvek je typu float

# konstrukce pole
a = zeros((5, 5))

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Matice o velikosti 5x5 prvků, každý prvek je typu int

# konstrukce pole
a = zeros((5, 5), dtype=int)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Použití komplexních čísel

# konstrukce pole
a = zeros((2, 2), dtype=complex)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ## Konstruktor `numpy.ones`
# - Vektor či matice s prvky nastavenými na jedničku
# - (nejedná se o jednotkovou matici!)
#     - viz konstruktor numpy.eye
# ### Volání konstruktoru numpy.ones
# `ones(shape, dtype=None, order='C')`

# ## Příklady použití funkce `numpy.ones()`

# ### Nejprve pro jistotu zjistíme, jestli je funkce `ones` volatelná
if "ones" not in globals():
    raise Exception("Symbol ones neexistuje")
if not callable(zeros):
    raise Exception("Nelze volat funkci ones")

# ### Jednorozměrný vektor s deseti prvky

# konstrukce pole
a = ones(10)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Matice se třemi řádky a čtyřmi sloupci

# konstrukce pole
a = ones((3, 4))

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Matice se třemi řádky a čtyřmi sloupci s explicitní specifikací typu prvků

# konstrukce pole
a = ones((3, 4), dtype=int)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Trojrozměrné pole s prvky typu `int`

# konstrukce pole
a = ones((3, 4, 5), dtype=int)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Trojrozměrné pole s prvky typu `int`

# konstrukce pole
a = ones((5, 4, 3), dtype=int)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Komplexní jednotka
# zde může být použití typu komplexní číslo možná poněkud překvapující ovšem stále platí, že 1=1+0j

# konstrukce pole
a = ones((3, 2), dtype=complex)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ## Konstruktor numpy.eye
# - Vytvoří se jednotková matice
# - Uvádí se její velikost
# - Lze ovšem vytvořit i nečtvercovou matici

# ## Příklady použití funkce `numpy.eye()`

# ### Nejprve pro jistotu zjistíme, jestli je funkce `eye` volatelná
if "eye" not in globals():
    raise Exception("Symbol eye neexistuje")
if not callable(eye):
    raise Exception("Nelze volat funkci eye")

# ### Matice 1x1 prvek

# konstrukce pole
a = eye(1)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Matice 5x5 prvků

# konstrukce pole
a = eye(5)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Matice 2x10 prvků

# konstrukce pole
a = eye(2, 10)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ## Funkce numpy.arange
# - Array+range
# - Podobné jako xrange/range
#     - ovšem návratovou hodnotou je ndarray

# ## Příklady použití funkce `numpy.arange()`

# ### Nejprve pro jistotu zjistíme, jestli je funkce `arange` volatelná
if "arange" not in globals():
    raise Exception("Symbol arange neexistuje")
if not callable(arange):
    raise Exception("Nelze volat funkci arange")

# ### Zavolání s jediným parametrem
# při použití jednoho parametru má tento parametr význam hodnoty „stop“
# vytvoří se vektor s prvky od 0 do „stop“ (kromě)

# konstrukce pole
a = arange(10)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Specifikace hodnot „start“ (včetně) a „stop“ (kromě)

# konstrukce pole
a = arange(10, 20)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Třetí nepovinný parametr určuje krok použitý při generování prvků vektoru

# konstrukce pole
a = arange(10, 20, 2)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)
   
# ### Krok může být samozřejmě záporný

# konstrukce pole
a = arange(20, 10, -2)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Použití komplexních čísel
# Nemusíme zůstat pouze u celých čísel, protože pracovat je možné i s hodnotami typu `float` a `complex`

# konstrukce pole
a = arange(0,5, 0.1)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Použití komplexních čísel

# konstrukce pole
a = arange(0+0j, 10+10j, 2+0j)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ## Funkce numpy.linspace()
# - Při znalosti první a poslední hodnoty ve vektoru
# - Zadává se
#     - počáteční hodnota
#     - koncová hodnota
#     - počet prvků vektoru (implicitně 50 prvků)

# ## Příklady použití funkce `numpy.linspace()`

# ### Nejprve pro jistotu zjistíme, jestli je funkce `linspace` volatelná
if "linspace" not in globals():
    raise Exception("Symbol linspace neexistuje")
if not callable(linspace):
    raise Exception("Nelze volat funkci linspace")

# ### Implicitní počet prvků
# pokud se nespecifikuje počet prvků, bude se předpokládat, že výsledný
# vektor má mít padesát prvků

# konstrukce pole
a = linspace(0, 1)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Explicitní určení počtu prvků
# zde explicitně specifikujeme, že výsledný vektor má mít deset prvků
# (tím, že se začíná od nuly, získáme krok 0.11111111...)

# konstrukce pole
a = linspace(0, 1, 10)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Explicitní určení počtu prvků
# zde explicitně specifikujeme, že výsledný vektor má mít jedenáct prvků

# konstrukce pole
a = linspace(0, 1, 11)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Sekvence hodnot samozřejmě může i klesat

# konstrukce pole
a = linspace(1, 0, 11)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Použít je možné i komplexní čísla

# konstrukce pole
a = linspace(0+0j, 1+0j, 10)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Použít je možné i komplexní čísla

# konstrukce pole
a = linspace(0+0j, 0+1j, 10)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ### Další možnost použití komplexních čísel

# konstrukce pole
a = linspace(0+0j, 1+1j, 10)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)

# ## Funkce numpy.geomspace()
# - Krok mezi prvky není lineární ale tvoří geometrickou posloupnost
# - Při znalosti první a poslední hodnoty ve vektoru
# - Zadává se
#     - počáteční hodnota
#     - koncová hodnota
#     - počet prvků vektoru (implicitně 50 prvků)

# ## Příklady použití funkce `numpy.geomspace()`

# ### Nejprve pro jistotu zjistíme, jestli je funkce `geomspace` volatelná
if "geomspace" not in globals():
    raise Exception("Symbol geomspace neexistuje")
if not callable(geomspace):
    raise Exception("Nelze volat funkci geomspace")

# ### Implicitní počet prvků

# ## Funkce numpy.logspace()
# - Krok mezi prvky není lineární ale tvoří logaritmickou posloupnost
# - Při znalosti první hodnoty, poslední hodnoty a báze
# - Nepatrně odlišné od funkce `linspace` a `geomspace`
# - Zadává se
#     - počáteční hodnota
#     - koncová hodnota
#     - báze (implicitně 10)
#     - krok je vypočten na základě ln(samples) / ln(base)

# ## Příklady použití funkce `numpy.logspace()`

# ### Nejprve pro jistotu zjistíme, jestli je funkce `logspace` volatelná
if "logspace" not in globals():
    raise Exception("Symbol logspace neexistuje")
if not callable(geomspace):
    raise Exception("Nelze volat funkci logspace")

# ### Implicitní počet prvků
