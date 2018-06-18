# Jazyk Python - základy programování

## Obsah kurzu

* Úvod – proč a k čemu používat Python, srovnání s ostatními programovacími jazyky
* Základy jazyka - čísla a řetězce, řetězce Unicode, seznamy (pole), práce se slovníky
* Řízení toku programu - konstrukce, funkce, příkazy, větvení
* Procedury a funkce – použití, definice, platnost proměnných
* Funkcionální prvky jazyka
* Moduly – přehled, vyhledávání, pravidla, funkce, balíčky
* Vstup a výstup – práce se soubory, souborové objekty, formátování výstupu
* Chyby a výjimky – přehled, vyvolání, obsluha, syntaktické chyby, složitější použití
* Třídy – použitá terminologie, definování, objekty, dědičnost
* Úprava příkazového řádku – vytvoření, argumenty, klávesové zkratky
* Použití debuggeru

---

## Úvod

* Základní informace o jazyku Python
* Proč a k čemu používat jazyk Python
* Srovnání s ostatními programovacími jazyky
* Implementace Pythonu
* Python 2.x vs Python 3.x

---

### Základní informace o jazyku Python

* Interpret
    - s generováním bajtkódu
* Objektově orientovaný jazyk
* Dynamicky typovaný
* Používá odsazení pro deklaraci bloků
* Dostupný pro mnoho platforem
* Používaný pro CLI aplikace, na serverech, pro GUI atd.
* "Batteries included"
    - rozsáhlá základní knihovna
    - nápověda
    - nástroje (tools)

---

### Interpretery vs překladače

* Interpret
    - Python, Perl, JavaScript, Ruby, TCL, shelly
    - typicky dynamicky typované jazyky (rychlejší vývoj)
    - snadněji použitelné (jednodušší syntaxe a sémantika)
    - kompaktnější kód
    - obecně pomalejší běh programů
    - lepší podpora tzv. introspekce
* Překladač
    - Java, C, C++, C#, Fortran
    - nutnost překladu (a slinkování)
    - pomalejší cyklus vývoje: editace-překlad-slinkování-spuštění
    - výsledné aplikace rychlejší (1:10 apod.)

---

### Proč a k čemu používat jazyk Python

* Nástroje a utility ovládané z příkazového řádku
* Aplikace s grafickým uživatelským rozhraním
* Client-server
    - serverová část (Flash, ...)
* Moderní způsoby využití
    - AI
    - Machine Learning (Deep Learning)
    - Big data

---

### Srovnání s ostatními programovacími jazyky

* Skriptovací jazyk
    - Perl
    - Ruby
* Dynamicky typovaný jazyk
    - Ruby, Perl
* Objektově orientovaný jazyk
    - Java
    - C++
    - C#

---

### Implementace Pythonu

* Nejpoužívanější implementace
    - CPython
    - Jython
    - Iron Python
    - Pypy

* Další implementace
    - Psyco
    - Stackles Python
    - MicroPython
    - Numba

* Speciální implementace
    - Cython
    - RPython

---

### Python 2.x vs Python 3.x

* Tyto dvě větve nejsou plně kompatibilní
* Skript `2to3` pro automatický převod
    - nutno ručně zkontrolovat
* Nejdůležitější rozdíly
    - `print`: příkaz vs funkce
    - celočíselné dělení
    - Unicode řetězce: nyní tři typy (str, byte, bytearray)
    - striktnější pravidla při porovnávání hodnot různých typů
    - xrange(): nyní se range() chová jako xrange()
    - argument při vyhazování výjimek musí být v závorkách
    - `except TypVýjimky, e:` versus `except TypVýjimky as e:`
    - generátory nemají metodu `next()`, namísto ní se používá funkce `next()`
    - range() vrací iterátor, ne seznam
    - některé funkce typu apply() byly přesunuty do zvlástního modulu

```python
n = 10000

def test_range(n):
    for i in range(n):
        pass

def test_xrange(n):
    for i in xrange(n):
        pass

test_range(n)
test_xrange(n)
```

---

## Základy jazyka

* Python jako skript
* Vstupně/výstupní funkce
* Ukázkový příklad
* Rezervovaná klíčová slova
* Datové typy
* Čísla
* Pravdivostní hodnoty
* Řetězce (raw, Unicode)
* Seznamy (pole)
* Slovníky
* Množiny
* N-tice

---

### Python jako skript

```python
# Body Mass Index calculator

print("Mass (kg): ")
mass = int(input())

print("Height (cm): ")
height = int(input())

height = height / 100.0

bmi = mass / (height * height)
print("BMI = ", bmi)
```

---

### Vstupně/výstupní funkce

* `print()`
    - tisk jakékoli hodnoty
    - viz další slajd
* `input()`
    - se zpracováním vstupu
    - v Pythonu 2 se odvozoval typ hodnoty
    - v Pythonu 3 se vždy vrací řetězec
* `raw_input()`
    - v Pythonu 2
    - vždy vrací řetězec
* `input("zprava")`
    - zobrazí zprávu

---

### Funkce print

* Existuje ve formě příkazu v Pythonu 2.x:

```python
print "Hello"
```

* V Pythonu 3 jde o funkci:

```python
print("Hello")
```

* Použijeme ji v navazujících slajdech

---

### Základní struktura kódu

```python
#!/usr/bin/env python
# encoding=utf-8

"""Dokumentační řetězec"""

# importy
# třídy
# funkce

if __name__ == "__main__":
    # vstupní bod
```

### Ukázkový příklad

```python
#!/usr/bin/env python
# encoding=utf-8

"""Body Mass Index calculator."""

import sys

def compute_bmi(mass, height):
    height = height / 100.0
    bmi = mass / (height * height)
    return bmi


print("Mass (kg): ")
mass = int(input())

if mass < 0:
    print("Invalid input")
    sys.exit(1)

print("Height (cm): ")
height = int(input())

if height < 0:
    print("Invalid input")
    sys.exit(1)

print("BMI = ", compute_bmi(mass, height))
```

---

### Rezervovaná klíčová slova

```
and       del       from      not       while
as        elif      global    or        with
assert    else      if        pass      yield
break     except    import    print
class     exec      in        raise
continue  finally   is        return
def       for       lambda    try
```

---

### Datové typy

* čísla (tři typy)
    - int / long
    - float
    - complex
* pravdivostní hodnoty
* řetězce
* seznamy
* slovníky
* množiny
* n-tice
* sekvence bajtů (bytes)
* pole bajtů (bytearray)
* frozenset
* NoneType
* objekt

---

### Měnitelnost

* mutability/immutability
* význam ve funkcionálních i imperativních jazycích

* Měnitelné typy
    - seznamy
    - slovníky
    - množiny
    - pole bajtů (bytearray)
    - objekt
* Neměnitelné typy
    - čísla
    - pravdivostní hodnoty
    - řetězce
    - n-tice
    - frozenset
    - sekvence bajtů
    - NoneType

---

### Čísla

* měnitelnost
    - neměnitelné
* ve skutečnosti tři typy
    - int / long (Python 2.x / Python 3.x)
    - float
    - complex

```python
print(42)
print(3.1415)
print(2+3j)
```

* pozor na:

---

### Pravdivostní hodnoty

* měnitelnost
    - neměnitelné
* datový typ
    - bool
* hodnoty
    - True
    - False

---

### Řetězce (raw, Unicode)

* měnitelnost
    - neměnitelné
* sekvence znaků
* původně sekvence bajtů
    - rozdíl - Unicode

```python
# běžný řetězec
print("Hello")

# bytové pole
print(b"abcdef")

# podpora pro Unicode
print(u"příliš žluťoučký kůň")

# řídicí znaky
print("abc\ndef")

# 'raw' řetězce
print(r"abc\ndef")

# víceřádkový řetězec
print("""A
B
C
D
E
F""")
```

---

### Seznamy (pole)

* měnitelnost
    - měnitelné
* homogenní datový typ
    - ne
* základní vlastnosti
    - do seznamu je možné přidávat nové prvky
    - prvky je možné i odstraňovat
    - k prvkům se přistupuje pomocí celočíselného indexu
    - lze získat i podseznam (výsek seznamu)


```python
```

---

### Slovníky

* měnitelnost
    - měnitelné


```python
```

---

### Množiny

* měnitelnost
    - měnitelné


```python
```

---

### N-tice

* měnitelnost
    - neměnitelné


```python
```

---

### Proměnné


```python
```

---

### Výrazy, operátory

* aritmetické operátory
    - `+`
    - `*`
    - `/`
    - `//`
    - `%`
    - `**`
* porovnávání
    - `==`
    - `!=`
    - `<>`
    - `>`
    - `<`
    - `>=`
    - `<=`
* logické operátory
    - `and`
    - `or
    - `not`
* bitové operátory
    - `&`
    - `|`
    - `^`
    - `~`
    - `<<`
    - `>>`
* přiřazení
    - `=`
    - `+=`
    - `-=`
    - `\*=`
    - `/=`
    - `%=`
    - `\*\*=`
    - `//=`
* další operátory
    - `in`
    - `not in`
    - `is`
    - `is not`

---

### Výrazy, operátory: ukázky použití

```python
```

---

### Priority operátorů

```
1       **
2       ~ + -
3       * / % //
4       + -
5       >> <<
6       &
7       ^ |
8       <= < > >=
9       <> == !=
10      = %= /= //= -= += *= **=
11      is   is not
12      in   not in
13      not or and
```

---

### Celočíselné dělení

* Nekompatibilita mezi Pythonem 2.x a Pythonem 3.x

```python
print '3 / 2 =', 3 / 2
print '3 // 2 =', 3 // 2
print '3 / 2.0 =', 3 / 2.0
print '3 // 2.0 =', 3 // 2.0
```

```
3 / 2 = 1
3 // 2 = 1
3 / 2.0 = 1.5
3 // 2.0 = 1.0
```

```python
print('3 / 2 =', 3 / 2)
print('3 // 2 =', 3 // 2)
print('3 / 2.0 =', 3 / 2.0)
print('3 // 2.0 =', 3 // 2.0)
```

```
3 / 2 = 1.5
3 // 2 = 1
3 / 2.0 = 1.5
3 // 2.0 = 1.0
```

---

## Řízení toku programu

* Základní pojmy
* Větvení (rozhodovací konstrukce)
* Složitější formy větvení
* Programové smyčky

---

### Základní pojmy

---

### Větvení (rozhodovací konstrukce)


```python
if condition1:
    pass
```

---

### Složitější formy větvení

```python
if condition1:
    pass
elif condition2:
    pass
elif condition3:
    pass
else:
    pass
```

---

### Složitější formy větvení

```python
```

---

### Programové smyčky

---

### Programová smyčka `while`

```python
x = 1

while x < 2000:
    print(x)
    x *= 2
```

```
1
2
4
8
16
32
64
128
256
512
1024
```

---

### Programová smyčka `for`

```python
list = ["one", "two", "three", "four"]

for item in list:
    print(item)
```

```
one
two
three
four
```


```python
for i in range(10):
    print(i)
```

```
0
1
2
3
4
5
6
7
8
9
```

```python
for i in range(4, 11, 2):
    print(i)
```

```
4
6
8
10
```

```python
for i in range(10, 0, -1):
    print(i)
```

```
10
9
8
7
6
5
4
3
2
1
```

---

## Procedury a funkce

* Základní pojmy
* Příklady použití
* Rekurznivní funkce
* Definice funkcí
* Oblast platnosti proměnných
* Použití globálních proměnných

---

### Základní pojmy

---

### Příklady použití

---

### Rekurznivní funkce

```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


print(factorial(10))

for n in range(1, 11):
    print(n, factorial(n))
```

```python
calls = 0

def ackermann(m, n):
    global calls
    calls += 1
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

print(ackermann(3,4))
```

---

### Definice funkcí

---

### Oblast platnosti proměnných

---

### Použití globálních proměnných

---

## Funkcionální prvky jazyka

* Lambda výrazy
* Generátorová notace seznamu

---

### Lambda výrazy

---

### Generátorová notace seznamu

---

## Moduly

* Přehled
* Vyhledávání
* Pravidla a idiomy
* Funkce
* Balíčky

---

## Vstup a výstup

* Práce se soubory
* Souborové objekty
* Formátování výstupu

---

## Chyby a výjimky

* Přehled
* Vyvolání výjimky
* Obsluha výjimky
* Syntaktické chyby
* Další možnosti použití

---

## Třídy

* Použitá terminologie
* Definice třídy
* Atributy
* Metody
* Objekty
* Dědičnost

---

### Definice třídy

```python
class Employee:

    def __init__(self, first_name, surname, salary):
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def display_employee(self):
        print("Full name: ", self._first_name, self._surname, "   Salary: ", self._salary)
```

```python
class Employee:

    def __init__(self, first_name, surname, salary):
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def display_employee(self):
        print("Full name: {name} {surname}   Salary: {salary}".format(name=self._first_name,
                                                                      surname=self._surname,
                                                                      salary=self._salary))


employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Přemysl", "Hájek", 25001)

employee1.display_employee()
employee2.display_employee()
```

---

### Přetížení speciální metody \_\_str\_\_

```python
class Employee:

    def __init__(self, first_name, surname, salary):
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def __str__(self):
        return "Full name: {name} {surname}   Salary: {salary}".format(name=self._first_name,
                                                                       surname=self._surname,
                                                                       salary=self._salary)


employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Přemysl", "Hájek", 25001)

print(employee1)
print(employee2)
```

---

## Úprava příkazového řádku

* Vytvoření
* Argumenty
* Klávesové zkratky

---

---

## Použití debuggeru

```
python -m pdb test.py
pdb.set_trace()
```

## Post mortem debug

```
try:
    raise Exception()
except:
    import pdb
    pdb.post_mortem()
```

---

## Užitečné odkazy

* Python Quick Reference: http://rgruet.free.fr/#QuickRef
* Python docs: http://www.python.org/doc/
* PEP 8: http://www.python.org/dev/peps/pep-0008/
* pep8.py: http://pypi.python.org/pypi/pep8/
* pylint: http://www.logilab.org/project/pylint
* Epydoc: http://epydoc.sourceforge.net/
* Sphinx: http://sphinx-doc.org/
* Python in Python: http://pypy.org/
* The key differences between Python 2.7.x and Python 3.x with examples: http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html
* Language differences and workarounds: http://python3porting.com/differences.html
* Everything you did not want to know about Unicode in Python 3: http://lucumr.pocoo.org/2014/5/12/everything-about-unicode/
* Unicode (Wikipedia): https://en.wikipedia.org/wiki/Unicode
