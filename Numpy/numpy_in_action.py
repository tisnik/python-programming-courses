# coding: utf-8

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
#╔════════════╤═══════════════════════════╤═══════════════════════════════╗
#║ Formát     │ Popis                     │ Rozsah                        ║
#╟────────────┼───────────────────────────┼───────────────────────────────╢
#║ bool       │ uloženo po bajtech        │  True/False                   ║
#╟────────────┼───────────────────────────┼───────────────────────────────╢
#║ int8       │ celočíselný se znaménkem  │ -128..127                     ║
#║ int16      │ celočíselný se znaménkem  │ -32768..32767                 ║
#║ int32      │ celočíselný se znaménkem  │ -2147483648..2147483647       ║
#║ int64      │ celočíselný se znaménkem  │ -9223372036854775808..        ║
#║            │                           │  9223372036854775807          ║
#╟────────────┼───────────────────────────┼───────────────────────────────╢
#║ uint8      │ celočíselný bez znaménka  │  0..255                       ║
#║ uint16     │ celočíselný bez znaménka  │  0..65535                     ║
#║ uint32     │ celočíselný bez znaménka  │  0..4294967295                ║
#║ uint64     │ celočíselný bez znaménka  │  0..18446744073709551615      ║
#╟────────────┼───────────────────────────┼───────────────────────────────╢
#║ float16    │ plovoucí řádová čárka     │  poloviční přesnost (half)    ║
#║ float32    │ plovoucí řádová čárka     │  jednoduchá přesnost (single) ║
#║ float64    │ plovoucí řádová čárka     │  dvojitá přesnost (double)    ║
#╟────────────┼───────────────────────────┼───────────────────────────────╢
#║ complex64  │ komplexní číslo (dvojice) │  2×float32                    ║
#║ complex128 │ komplexní číslo (dvojice) │  2×float64                    ║
#╚════════════╧═══════════════════════════╧═══════════════════════════════╝
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
