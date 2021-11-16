# Jazyk Python - pokročilé techniky

* Pavel Tišnovský
    - `ptisnovs@redhat.com`
* Slajdy a demonstrační příklady:
    - `https://github.com/tisnik/python-programming-courses`

---



## Obsah kurzu

* Objektově orientované konstrukce v jazyku Python
    - Použitá terminologie
    - Definice třídy
    - Atributy
    - Metody
    - Objekty

* Pokročilé OOP techniky
    - Magické metody
    - Dědičnost, polymorfismus
    - Properties
    - Statické metody

* Pokročilé konstrukty jazyka
    - Generátory a iterátory
    - Generátorová notace
    - Dekorátory

* Základy funkcionálního programování v Pythonu
    - Lambda výrazy
    - Anonymní funkce, first-class funkce, rekurze, closures, ...
    - Map, reduce, filter
    - Zkrácené logické výrazy

* Tvorba skriptů v Pythonu
    - Psaní skriptů

* Standardní knihovna, zajímavé moduly a balíčky
    - Přehled modulů a balíčků standardní knihovny
    - Repozitář PyPi
    - Nástroje pip, ensurepip

* CPython a jeho alternativy
    - Hlavní vlastnosti CPythonu
    - Virtuální prostředí s virtualenv, venv, ...
    - PyPy, Jython, IronPython, ...
    - Python ve WWW prohlížeči, Brython, ...
    - Nástroje pro distribuci programu jako Pyinstaller

* Datové formáty, perzistentní úložiště, databáze
    - Práce s formáty Python pickle, JSON
    - Key-value databáze shelve
    - Práce s formátem XLSX

* Testování
    - Základní technologie testování
    - Modul pytest

* Aplikace s GUI
    - Návrh jednoduché aplikace s GUI
    - Widget knihovny jako GTk+, wxWidgets, QT a Python

--



## Objektově orientované konstrukce v jazyku Python

* Použitá terminologie
* Definice třídy
* Atributy
* Metody
* Objekty



### Použitá terminologie

* Třída
    - data+funkce+(zapouzdření)
* Předek, potomek
* Objekt
    - instance třídy
* Metoda
* Atribut
    - objektu
    - třídní
* Konstruktor



### Definice třídy

* Třída představuje nový uživatelsky definovaný datový typ
* Současně obsahuje předpis metod
* Může obsahovat i statické atributy popř. třídní atributy
* V Pythonu však neobsahuje definice atributů objektů!
    - je to dynamický jazyk

! examples/OOP/employee_class_0.py



### Objekty

* Instance třídy
* Jedna třída více objektů

! examples/OOP/employee_class_1.py



### Atributy tříd a objektů

* Datové položky
* Vytvářené explicitně pro každou instanci třídy
    - typicky v konstruktoru
* Přístup k atributům
    - interně přes `self`
    - externě pomocí "tečkové notace"
* Třídní/statický atribut
    - deklarován přímo ve třídě
    - sdílený všemi instancemi
    - přístup přes `JménoTřídy.jménoAtributu`
    - mohou být pojmenovány stejně jako atributy objektu

! examples/OOP/class_attribute.py



### Konstruktor

* Zavolán při konstrukci objektu

! examples/OOP/employee_class_2.py



### Metody

* Funkce, které mají přístup k datovým položkám
    - přístup přes `self`
    - zavolání pomocí "tečkové notace"

```python
    def display_employee(self):
        print("Full name: ", self._first_name, self._surname, "   Salary: ", self._salary)
```

* Celý skript

! examples/OOP/employee_class_3.py

* Vylepšení formátování výstupu

! examples/OOP/employee_class_4.py



--

## Pokročilé OOP techniky


### Speciální metoda `__str__`

* Zavolána při převodu objektu na řetězec

! examples/OOP/employee_class_5.py



### Speciální metoda `__eq__`

* Zavolána při porovnávání objektů

! examples/OOP/employee_class_6.py

--

## Základy funkcionálního programování v Pythonu

* Lambda výrazy
* Generátorová notace seznamu
* Funkce vyššího řádu

--

## Tvorba skriptů v Pythonu

--

## Standardní knihovna, zajímavé moduly a balíčky

--

## CPython a jeho alternativy

--

## Datové formáty, perzistentní úložiště, databáze

--

## Testování

--

## Aplikace s GUI

--

