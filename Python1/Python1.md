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
* Objektově orientovaný jazyk
* Dostupný pro mnoho platforem
* Používaný pro CLI aplikace, na serverech, pro GUI atd.

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

---

## Základy jazyka

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

### Ukázkový příklad

```python
# Body Mass Index calculator

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
* objekt
    - None

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

---

### Čísla

* ve skutečnosti tři typy
    - int / long (Python 2.x / Python 3.x)
    - float
    - complex

---

### Pravdivostní hodnoty

---

### Řetězce (raw, Unicode)

---

### Seznamy (pole)

---

### Slovníky

---

### Množiny

---

### N-tice

---

### Proměnné

---

### Výrazy, operátory

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

---

### Složitější formy větvení

---

### Programové smyčky

---

## Procedury a funkce

* Základní pojmy
* Příklady použití
* Definice funkcí
* Oblast platnosti proměnných
* Použití globálních proměnných

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

