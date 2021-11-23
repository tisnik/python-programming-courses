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
    - Magické/speciální metody
    - Dědičnost, polymorfismus
    - Properties
    - Statické metody

* Základy funkcionálního programování v Pythonu
    - Lambda výrazy
    - Anonymní funkce, first-class funkce, rekurze, closures, ...
    - Map, reduce, filter
    - Zkrácené logické výrazy

* Pokročilé konstrukty jazyka Python
    - Generátory a iterátory
    - Generátorová notace
    - Dekorátory

* Tvorba skriptů v Pythonu
    - Psaní skriptů
    - Parametry na příkazové řádce
    - Návratové hodnoty
    - Přesměrování vstupů a výstupů

* Standardní knihovna, zajímavé moduly a balíčky
    - Přehled modulů a balíčků standardní knihovny
    - Repositář PyPi
    - Nástroje pip popř., ensurepip

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
    - Zpracování událostí
    - Animace

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
    - funkce definovaná ve třídě
    - běžná metoda má přístup k atributům
    - statické metody
    - třídní metody
* Atribut
    - objektu
    - třídní
* Konstruktor
    - zavolán při vytváření objektu
* Destruktor
    - zavolán před uvolněním objektu
    - v Pythonu problematické



### Definice třídy

* Třída představuje nový uživatelsky definovaný datový typ
* Současně obsahuje předpis metod
* Může obsahovat i statické metody popř. třídní atributy a metody
* V Pythonu však neobsahuje explicitní definice atributů objektů!
    - je to dynamický jazyk

```python
"""Kostra jednoduché třídy reprezentující zaměstnance."""


class Employee:
    """Kostra třídy reprezentující zaměstnance."""
    pass
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/employee_class_0.py)



### Objekty

* Instance třídy
* Z jedné třídy lze vytvořit více objektů
    - dtto pro další datové typy
    - (seznam, slovník, celé číslo)
* Třída -> datový typ
* Objekt -> hodnota daného datového typu

```python
"""Kostra jednoduché třídy reprezentující zaměstnance."""


class Employee:
    """Kostra třídy reprezentující zaměstnance."""
    pass

# vytvoření dvou instancí třídy
employee1 = Employee()
employee2 = Employee()

# výpis hodnot objektů
print(employee1)
print(employee2)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/employee_class_1.py)



### Atributy tříd a objektů

* Datové položky
* Vytvářené explicitně pro každou instanci třídy
    - typicky v konstruktoru
* Přístup k atributům
    - interně přes `self`
    - externě pomocí jména proměnné
    - "tečková notace"
* Třídní/statický atribut
    - deklarován přímo ve třídě
    - sdílený všemi instancemi
    - přístup přes `JménoTřídy.jménoAtributu`
    - mohou být pojmenovány stejně jako atributy objektu

```python
class CLS:
    x = 10

c1 = CLS()
print(CLS.x)
print(c1.x)

c1.x = 20
print(CLS.x)
print(c1.x)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/class_attribute.py)



### Konstruktor

* Zavolán automaticky při konstrukci objektu
* Může akceptovat další parametry
* Může přistupovat k atributům (většinou je vytváří)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Ukázka jednoduché třídy reprezentující zaměstnance."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary


# vytvoření dvou instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Přemysl", "Hájek", 25001)

# výpis hodnot objektů
print(employee1._first_name)
print(employee2._first_name)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/employee_class_2.py)



### Destruktor

* Zavolán automaticky při uvolňování objektu
    - popř. pokud objekt již nemá kontext
* Neakceptuje další parametry
* Může přistupovat k atributům (problematické!)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Ukázka jednoduché třídy reprezentující zaměstnance."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        print("Konstruktor:", first_name, surname)
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def __del__(self):
        """Destruktor objektu."""
        print("Destruktor:", self._first_name, self._surname)


def test_destructor():
    # vytvoření dvou instancí třídy
    employee1 = Employee("Eda", "Wasserfall", 10000)
    employee2 = Employee("Přemysl", "Hájek", 25001)


test_destructor()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/employee_class_destructor1.py)

* Volání konstruktoru může přijít "pozdě" - po ukončení skriptu

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Ukázka jednoduché třídy reprezentující zaměstnance."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        print("Konstruktor:", first_name, surname)
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def __del__(self):
        """Destruktor objektu."""
        print("Destruktor:", self._first_name, self._surname)


# vytvoření dvou instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Přemysl", "Hájek", 25001)

print("Konec programu")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/employee_class_destructor2.py)

* Explicitní smazání konstruktoru konstrukcí `del`

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Explicitní smazání objektu konstrukcí del."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        print("Konstruktor:", first_name, surname)
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def __del__(self):
        """Destruktor objektu."""
        print("Destruktor:", self._first_name, self._surname)


def test_destructor():
    # vytvoření dvou instancí třídy
    employee1 = Employee("Eda", "Wasserfall", 10000)
    employee2 = Employee("Přemysl", "Hájek", 25001)

test_destructor()

employee3 = Employee("x", "y", 0)

print("Volam del")
del employee3

print("Konec programu")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/explicit_del_call.py)


### Metody

* Funkce, které mají přístup k datovým položkám
    - přístup přes `self`
    - zavolání s využitím "tečkové notace"

* Deklarovány uvnitř třídy

```python
    def display_employee(self):
        print("Full name: ", self._first_name, self._surname, "   Salary: ", self._salary)
```

* Celý skript s metodou `display_employee`

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Ukázka jednoduché třídy reprezentující zaměstnance."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def display_employee(self):
        """Metoda pro výpis hodnoty objektu."""
        print("Full name: ", self._first_name, self._surname, "   Salary: ", self._salary)


# vytvoření dvou instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Přemysl", "Hájek", 25001)

# výpis hodnot objektů
employee1.display_employee()
employee2.display_employee()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/employee_class_3.py)

* Vylepšení formátování výstupu

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vylepšení metody pro výpis hodnoty objektu."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def display_employee(self):
        """Metoda pro výpis hodnoty objektu."""
        print("Full name: {name} {surname}   Salary: {salary}".format(
            name=self._first_name,
            surname=self._surname,
            salary=self._salary))


# vytvoření dvou instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Přemysl", "Hájek", 25001)

# výpis hodnot objektů
employee1.display_employee()
employee2.display_employee()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/employee_class_4.py)

--



## Pokročilé OOP techniky

* Magické/speciální metody
* Dědičnost, polymorfismus
* Properties
* Atributy třídy, třídní metody
* Statické metody


### Speciální metody

* Použity pro takzvané přetěžování operátorů
    - aritmetické operátory
    - relační operátory
* Ovšem nelze modifikovat zejména
    - prioritu operátorů
    - asociativitu operátorů
* Některé metody volány ve specifických situacích
    - konstruktor objektu
    - destruktor objektu
    - přístup k atributům objektu, mazání atributu
    - převod objektu na řetězec

### Seznam speciálních metod

* Metody volané automaticky ve specifických situacích

```
__init__
__str__
__repr__
__hash__
__call__
__iter__
__getattr__
__getattribute__
__setattr__
__delattr__
```

* Přetížení relačních operátorů

```
__eq__  x, y   x == y
__ne__  x, y   x != y
__lt__  x, y   x < y
__gt__  x, y   x > y
__le__  x, y   x <= y
__ge__  x, y   x >= y
```

* Přetížení unárních a binárních operátorů

```
__add__        binární + operátor
__sub__        binární - operátor
__mul__        * operátor
__div__        / operátor
__floordiv__   // operátor (Python 2)
__truediv__    / operátor (Python 3)
__mod__        % operátor
__pow__        ** operátor or pow(x, y, z)
__neg__        unární - operátor
__pos__        unární + operátor
__abs__        absolutní hodnota
__nonzero__    konverze na Boolean
__invert__     ~ operátor
__lshift__     << operátor
__rshift__     >> operátor
__and__        & operátor
__or__  x, y   | operátor
__xor__        ^ operátor
```

* Přetížení kombinace přiřazení + binární operátor

```
__iadd__       += operátor
__isub__       -= operátor
__imul__       *= operátor
__idiv__       /= operátor (Python 2)
__ifloordiv__  //= operátor
__itruediv__   /= operátor (Python 3)
__imod__       %= operátor
__ipow__       **= operátor
__ilshift__    <<= operátor
__irshift__    >>= operátor
__iand__       &= operátor
__ior__        |= operátor
__ixor__       ^= operátor
```



### Speciální metoda `__str__`

* Zavolána při převodu objektu na řetězec
* Lze ji přetížit její (re)definicí

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Přetížení speciální metody pri převod objektu na řetězec."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "Full name: {name} {surname}   Salary: {salary}".format(
                name=self._first_name,
                surname=self._surname,
                salary=self._salary)


# vytvoření dvou instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Přemysl", "Hájek", 25001)

# výpis hodnot objektů
print(employee1)
print(employee2)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/employee_class_5.py)



### Speciální metoda `__eq__`

* Zavolána při porovnávání objektů

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Přetížení speciální metody pro porovnání dvou objektů."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        self._poznamka = 124

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "name: {name} {surname}   Salary: {salary}".format(name=self._first_name,
                                                                  surname=self._surname,
                                                                  salary=self._salary)

    def __eq__(self, other):
        if other is None:
            return False
        return self._first_name == other._first_name and \
            self._surname == other._surname and \
            self._salary == other._salary


# vytvoření tří instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Eda", "Wasserfall", 10000)
employee3 = Employee("Přemysl", "Hájek", 25001)

# výpis hodnot objektů
print(employee1)
print(employee2)
print(employee1 == employee2)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/employee_class_6.py)



### Třída komplexních čísel

* Základní reprezentace komplexního čísla

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Třída představující komplexní čísla."""


class Complex:
    """Třída představující komplexní čísla."""

    def __init__(self, real=0, imag=0):
        """Konstruktor."""
        self._real = real
        self._imag = imag


c1 = Complex(1, 2)
c2 = Complex(10, 20)
c3 = Complex(100)
c4 = Complex()

c5 = Complex(1, 2)
print(c1)
print(c2)
print(c3)
print(c4)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/complex1.py)

* Převod na řetězec

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Převod objektu na řetězec."""


class Complex:

    def __init__(self, real=0, imag=0):
        self._real = real
        self._imag = imag

    def __str__(self):
        return "{r} + {i}j".format(r=self._real, i=self._imag)


c1 = Complex(1, 2)
c2 = Complex(10, 20)
c3 = Complex(100)
c4 = Complex()

c5 = Complex(1, 2)
print(c1)
print(c2)
print(c3)
print(c4)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/complex2.py)

* Porovnání dvou komplexních čísel

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Porovnání komplexních čísel."""


class Complex:

    def __init__(self, real=0, imag=0):
        self._real = real
        self._imag = imag

    def __str__(self):
        return "{r} + {i}j".format(r=self._real, i=self._imag)

    def __eq__(self, other):
        return self._real == other._real and self._imag == other._imag


c1 = Complex(1, 2)
c2 = Complex(10, 20)
c3 = Complex(100)
c4 = Complex()

c5 = Complex(1, 2)
print(c1)
print(c2)
print(c3)
print(c4)

print(c1 == c5)
print(c2 == c5)
print(c3 == c5)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/complex3.py)

* Součet komplexních čísel operátorem `+`

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Součet komplexních čísel."""


class Complex:

    def __init__(self, real=0, imag=0):
        self._real = real
        self._imag = imag

    def __str__(self):
        return "{r} + {i}j".format(r=self._real, i=self._imag)

    def __eq__(self, other):
        return self._real == other._real and self._imag == other._imag

    def __add__(self, other):
        r = self._real + other._real
        i = self._imag + other._imag
        return Complex(r, i)


c1 = Complex(1, 2)
c2 = Complex(10, 20)
c3 = Complex(100)
c4 = Complex()

c1 += c3
print(c1)

c5 = Complex(1, 2)
print(c1)
print(c2)
print(c3)
print(c4)

print(c1 == c5)
print(c2 == c5)
print(c3 == c5)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/complex4.py)

* Přičtení ke komplexnímu číslu operátorem `+=`

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Přičtení komplexního čísla."""


class Complex:

    def __init__(self, real=0, imag=0):
        self._real = real
        self._imag = imag

    def __str__(self):
        return "{r} + {i}j".format(r=self._real, i=self._imag)

    def __eq__(self, other):
        return self._real == other._real and self._imag == other._imag

    def __add__(self, other):
        r = self._real + other._real
        i = self._imag + other._imag
        return Complex(r, i)

    def __iadd__(self, other):
        self._real += other._real
        self._imag += other._imag
        return self


c1 = Complex(1, 2)
c2 = Complex(10, 20)
c3 = Complex(100)
c4 = Complex()

c1 += c3
print(c1)

c5 = Complex(1, 2)
print(c1)
print(c2)
print(c3)
print(c4)

print(c1 == c5)
print(c2 == c5)
print(c3 == c5)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/complex5.py)

* Negace komplexního čísla

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Negace komplexního čísla."""


class Complex:

    def __init__(self, real=0, imag=0):
        self._real = real
        self._imag = imag

    def __str__(self):
        return "{r} + {i}j".format(r=self._real, i=self._imag)

    def __eq__(self, other):
        return self._real == other._real and self._imag == other._imag

    def __add__(self, other):
        r = self._real + other._real
        i = self._imag + other._imag
        return Complex(r, i)

    def __iadd__(self, other):
        self._real += other._real
        self._imag += other._imag
        return self

    def __neg__(self):
        r = self._real
        i = self._imag
        return Complex(-r, -i)


c1 = Complex(1, 2)
c2 = Complex(10, 20)
c3 = Complex(100)
c4 = Complex()

c1 += c3
print(c1)

c5 = Complex(1, 2)
print(c1)
print(c2)
print(c3)
print(c4)

print(c1 == c5)
print(c2 == c5)
print(c3 == c5)

c6 = - c1
print(c1)
print(c6)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/complex6.py)

* Přidání metody `__repr__`

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Metoda __repr__."""


class Complex:
    """Třída představující komplexní čísla."""

    def __init__(self, real=0, imag=0):
        """Konstruktor."""
        self._real = real
        self._imag = imag

    def __str__(self):
        return "{r} + {i}j".format(r=self._real, i=self._imag)

    def __repr__(self):
        return "Complex({r}, {i})".format(r=self._real, i=self._imag)

    def __eq__(self, other):
        return self._real == other._real and self._imag == other._imag

    def __add__(self, other):
        r = self._real + other._real
        i = self._imag + other._imag
        return Complex(r, i)

    def __iadd__(self, other):
        self._real += other._real
        self._imag += other._imag
        return self

    def __neg__(self):
        r = self._real
        i = self._imag
        return Complex(-r, -i)


c1 = Complex(1, 2)
c2 = Complex(10, 20)

c3 = c1 + c2
print(c3)

print(c3)

print(c3.__repr__())
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/complex7.py)



### Dědičnost

* Z jedné třídy lze odvodit třídu další
    - předek/potomek
    - superclass
* Nová třída zdědí vlastnosti z třídy předchozí
* Vybrané vlastnosti je možné modifikovat

* Třída `Person` a od ní odvozená třída `Student`

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Třída Person a odvození třídy Student."""


class Person:

    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Person** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


class Student(Person):
    pass

# vytvoření dvou instancí třídy
p1 = Person("Eda", "Wasserfall")
p2 = Person("Přemysl", "Hájek")

print(p1)
print(p2)

s1 = Student("John", "Doe")

print(s1)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/inheritance1.py)

* Přetížení metody `__str__` ve třídě Student

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Přetížení metody __str__ ve třídě Student."""


class Person:

    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Person** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


class Student(Person):

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Student** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


# vytvoření dvou instancí třídy
p1 = Person("Eda", "Wasserfall")
p2 = Person("Přemysl", "Hájek")

print(p1)
print(p2)

s1 = Student("John", "Doe")

print(s1)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/inheritance2.py)

* Volání konstruktoru nadtřídy

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Volání konstruktoru nadtřídy."""


class Person:

    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Person** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


class Student(Person):
    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        super().__init__(first_name, surname)

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Student** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


# vytvoření dvou instancí třídy
p1 = Person("Eda", "Wasserfall")
p2 = Person("Přemysl", "Hájek")

print(p1)
print(p2)

s1 = Student("John", "Doe")

print(s1)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/inheritance3.py)

* Volání konstruktoru nadtřídy, rozlišení konstruktorů

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Volání konstruktoru nadtřídy, rozlišení konstruktorů."""


class Person:

    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        print("Person.__init__")
        self._first_name = first_name
        self._surname = surname

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Person** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


class Student(Person):
    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        print("Student.__init__")
        super().__init__(first_name, surname)

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Student** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


# vytvoření dvou instancí třídy
p1 = Person("Eda", "Wasserfall")
p2 = Person("Přemysl", "Hájek")

print(p1)
print(p2)

s1 = Student("John", "Doe")

print(s1)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/inheritance4.py)

* Další třída `Employee` odvozená od třídy `Person`

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Další třída Employee odvozená od třídy Person."""


class Person:

    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        print("Person.__init__")
        self._first_name = first_name
        self._surname = surname

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Person** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


class Student(Person):
    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        print("Student.__init__")
        super().__init__(first_name, surname)

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Student** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


class Employee(Person):
    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        print("Employee.__init__")
        super().__init__(first_name, surname)
        self._salary = salary

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Employee** Full name: {name} {surname}   Salary: {salary}".format(
                name=self._first_name,
                surname=self._surname,
                salary=self._salary)


# vytvoření dvou instancí třídy
p1 = Person("Eda", "Wasserfall")
p2 = Person("Přemysl", "Hájek")

print(p1)
print(p2)

s1 = Student("John", "Doe")

print(s1)

e1 = Employee("Eric", "Iverson", 10000)

print(e1)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/inheritance5.py)



### Polymorfismus

* Ukázka polymorfismu

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Ukázka polymorfismu."""


class Person:

    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        print("Person.__init__")
        self._first_name = first_name
        self._surname = surname

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Person** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


class Student(Person):
    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        print("Student.__init__")
        super().__init__(first_name, surname)

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Student** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


class Employee(Person):
    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        print("Employee.__init__")
        super().__init__(first_name, surname)
        self._salary = salary

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Employee** Full name: {name} {surname}   Salary: {salary}".format(
                name=self._first_name,
                surname=self._surname,
                salary=self._salary)


people = [
    Person("Eda", "Wasserfall"),
    Person("Přemysl", "Hájek"),
    Student("John", "Doe"),
    Employee("Eric", "Iverson", 10000)
]

for p in people:
    print(p)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/polymorphism1.py)

* Třída jako rozhraní v Pythonu

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Ukázka polymorfismu (třída jako rozhraní)."""



class Printable:
    def display(self):
        print(self)


class Person(Printable):

    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        print("Person.__init__")
        self._first_name = first_name
        self._surname = surname

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Person** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


class Student(Person):
    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        print("Student.__init__")
        super().__init__(first_name, surname)

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Student** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


class Employee(Person):
    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        print("Employee.__init__")
        super().__init__(first_name, surname)
        self._salary = salary

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Employee** Full name: {name} {surname}   Salary: {salary}".format(
                name=self._first_name,
                surname=self._surname,
                salary=self._salary)


people = [
    Person("Eda", "Wasserfall"),
    Person("Přemysl", "Hájek"),
    Student("John", "Doe"),
    Employee("Eric", "Iverson", 10000)
]

for p in people:
    p.display()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/polymorphism2.py)



### Atributy třídy, třídní metody

* Předepsány přímo v deklaraci třídy
* Jsou sdíleny všemi instancemi této třídy!
* Přístup přes třídní metody
    - class method
* Parametr `cls` (jako class) nikoli `self`

* Atribut třídy a tečková notace

```python
class CLS:
    x = 10

c1 = CLS()
print(CLS.x)
print(c1.x)

c1.x = 20
print(CLS.x)
print(c1.x)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/class_attribute.py)

* Typický příklad použití - počitadlo instancí

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Metoda třídy."""


class Employee:
    """Třída reprezentující zaměstnance."""

    counter = 0

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        Employee.inc_counter()

    def display_employee(self):
        """Metoda pro výpis hodnoty objektu."""
        print("Full name: {name} {surname}   Salary: {salary}".format(
            name=self._first_name,
            surname=self._surname,
            salary=self._salary))

    @classmethod
    def inc_counter(cls):
        cls.counter += 1

    @classmethod
    def num_employees(cls):
        return cls.counter


# vytvoření dvou instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
print("Now we have", Employee.num_employees(), "employees")

employee2 = Employee("Přemysl", "Hájek", 25001)
print("Now we have", Employee.num_employees(), "employees")


# výpis hodnot objektů
employee1.display_employee()
employee2.display_employee()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/class_method.py)

* (bylo by vhodné upravit přetížením destruktoru)



### Statické metody

* Pouze funkce zapouzdřené do jmenného prostoru třídy
* Nemají přístup k žádným atributům
* I proto nemají parametr `self`

* Nekorektní příklad použití

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Statická metoda."""


class Employee:
    """Třída reprezentující zaměstnance."""

    counter = 0

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        Employee.inc_counter()
        Employee.dec_counter()

    def display_employee(self):
        """Metoda pro výpis hodnoty objektu."""
        print("Full name: {name} {surname}   Salary: {salary}".format(
            name=self._first_name,
            surname=self._surname,
            salary=self._salary))

    @classmethod
    def inc_counter(cls):
        cls.counter += 1

    @staticmethod
    def dec_counter():
        # !!!
        cls.counter += 1

    @classmethod
    def num_employees(cls):
        return cls.counter



# vytvoření dvou instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
print("Now we have", Employee.num_employees(), "employees")

employee2 = Employee("Přemysl", "Hájek", 25001)
print("Now we have", Employee.num_employees(), "employees")


# výpis hodnot objektů
employee1.display_employee()
employee2.display_employee()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/static_method1.py)

* Korektní příklad použití

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Statická metoda."""


class Employee:
    """Třída reprezentující zaměstnance."""

    counter = 0

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        Employee.inc_counter()

    def display_employee(self):
        """Metoda pro výpis hodnoty objektu."""
        print("Full name: {name} {surname}   Salary: {salary}".format(
            name=self._first_name,
            surname=self._surname,
            salary=self._salary))

    @classmethod
    def inc_counter(cls):
        cls.counter += 1
        if Employee.too_much(cls.counter):
            raise Exception("Company is full!")

    @staticmethod
    def too_much(cnt):
        return cnt > 3

    @classmethod
    def num_employees(cls):
        return cls.counter



# vytvoření dvou instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
print("Now we have", Employee.num_employees(), "employees")

employee2 = Employee("Přemysl", "Hájek", 25001)
print("Now we have", Employee.num_employees(), "employees")


# výpis hodnot objektů
employee1.display_employee()
employee2.display_employee()

e3 = Employee("Foo", "Bar", 0)
e4 = Employee("Foo", "Baz", 0)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/static_method2.py)



--

## Základy funkcionálního programování v Pythonu

* Lambda výrazy, anonymní funkce
* Generátorová notace seznamu
* Funkce vyššího řádu
* First-class funkce, rekurze, closures, ...
* Map, reduce, filter
* Zkrácené logické výrazy



### Lambda výrazy

* Anonymní funkce
* Lze použít na místech, kde se očekává reference na funkci (`map` atd.)
* Implicitní konstrukce `return`
* V Pythonu platí některá omezení
    - jeden výraz v těle funkce
    - žádné příkazy (skutečně jen výraz)

* Lambda výraz s parametry

```python
f = lambda x, y : x + y
print(f(1,2))
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/lambda1.py)

* Lambda výraz bez parametrů

```python
f = lambda : "hello"
print(f())
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/lambda2.py)

* Někdy je zapotřebí parametr ignorovat
    - uvidíme při návrhu GUI u událostí (events)

```python
f = lambda _: "hello"
print(f("foo"))
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/lambda3.py)



### First-class funkce

* Funkce jsou v Pythonu plnohodnotným datovým typem
    - akceptují se jako parametry jiných funkcí
    - lze je vracet jako návratové hodnoty jiných funkcí
    - lze je ukládat do n-tic, seznamů, slovníků...

* Funkce jako parametr jiné funkce

```python
def calculate(what, x, y):
    return what(x, y)


def add(x, y):
    return x + y


result = calculate(add, 10, 20)

print(result)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/accept_function.py)

* Funkce jako návratová hodnota jiné funkce

```python
def calculate(what, x, y):
    return what(x, y)


def add(x, y):
    return x + y


def get_function(selector):
    if selector == "add":
        return add
    return None


adder = get_function("add")
result = calculate(adder, 10, 20)

print(result)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/adder.py)



### Uzávěry (closures)

* Funkce mající přístup k nelokální proměnné/hodnotě
    - "uzavírají" tuto hodnotu

```python
def increment_by(n):

    def add(x):
        return x + n

    return add


i1 = increment_by(2)
print(i1(1))
print(i1(10))

i2 = increment_by(100)
print(i2(1))
print(i2(10))
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/closure.py)

* Nutnost použití modifikátoru `nonlocal`

* Typický příklad - libovolné množství čítačů

```python
def counter():
    cnt = 0

    def impl():
        nonlocal cnt
        cnt += 1
        return cnt

    return impl


c1 = counter()
c2 = counter()

print(c1())
print(c1())
print(c1())

print(c2())

print(c1())
print(c1())
print(c1())

print(c2())

```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/counter.py)

* (lze implementovat i s využitím generátorů)



### Generátorová notace seznamu

* List comprehension
    - možnost konstrukce n-tice nebo seznamu na jediném řádku bez `append`
    - lze kombinovat s podmínkou
    - existuje i varianta založená na generátorech

```python
"""Generátorová notace seznamu."""

seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

seznam1 = [item for item in seznam]

seznam2 = [item*2 for item in seznam]

seznam3 = [item for item in seznam if item % 3 == 0]

print(seznam)
print(seznam1)
print(seznam2)
print(seznam3)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/list_comprehension.py)



### Funkce vyššího řádu

* Funkce vyššího řádu = všechny funkce, které:
    - akceptují jiné funkce jako parametry
    - vrací funkce (návratové hodnoty)

* Typická trojice funkcí vyššího řádu
    - `map`
    - `reduce`
    - `filter`

* Funkce `map`
    - aplikace nějaké funkce na všechny prvky nějaké sekvence
    - typicky se používá společně s anonymní funkcí `lambda`

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Funkce vyššího řádu map."""

x = range(10)

print(x)

y = map(lambda value: value*2, x)
print(list(y))
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/map_function.py)

    - popř. s pojmenovanou funkcí

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Funkce vyššího řádu map."""

def inc(x):
    return x+1

x = range(10)

print(x)

y = map(inc, x)
print(list(y))
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/map_function2.py)

* Funkce `filter`
    - výběr hodnot ze sekvence na základě zadané podmínky

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Funkce vyššího řádu filter."""

x = range(20)

print(x)

y = filter(lambda value: value % 3 == 0, x)
print(list(y))
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/filter_function.py)

* Funkce `reduce`
    - postupné zkracování vstupní sekvence akumulací mezivýsledku
    - musí být importována z balíčku `functools`

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Funkce vyššího řádu reduce."""

from functools import reduce

x = range(1, 11)

print(x)

y = reduce(lambda a, b: a*b, x)
print(y)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/reduce_function.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Funkce vyššího řádu reduce."""

from functools import reduce

x = range(1, 101)

print(x)

y = reduce(lambda a, b: a+b, x)
print(y)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/reduce_sum.py)



### Zkrácené logické výrazy

* Druhý operand je vyhodnocen pouze v případě, že není dopředu známý výsledek výrazu
    - `x and y` - pokud `x==False`, není nutné vyhodnotit `y`
    - `x or y` - pokud `x==True`, není nutné vyhodnotit `y`

* Ukázka všech možných kombinací, které mohou nastat

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zkrácené vyhodnocení logických operátorů."""

def x():
    print("x() called")
    return False

def y():
    print("y() called")
    return False

if x() or y():
    print("if branch")
else:
    print("else branch")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/short_circuit_1.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zkrácené vyhodnocení logických operátorů."""

def x():
    print("x() called")
    return True

def y():
    print("y() called")
    return False

if x() or y():
    print("if branch")
else:
    print("else branch")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/short_circuit_2.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zkrácené vyhodnocení logických operátorů."""

def x():
    print("x() called")
    return False

def y():
    print("y() called")
    return True

if x() or y():
    print("if branch")
else:
    print("else branch")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/short_circuit_3.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zkrácené vyhodnocení logických operátorů."""

def x():
    print("x() called")
    return True

def y():
    print("y() called")
    return True

if x() or y():
    print("if branch")
else:
    print("else branch")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/short_circuit_4.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zkrácené vyhodnocení logických operátorů."""

def x():
    print("x() called")
    return False

def y():
    print("y() called")
    return False

if x() and y():
    print("if branch")
else:
    print("else branch")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/short_circuit_5.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zkrácené vyhodnocení logických operátorů."""

def x():
    print("x() called")
    return True

def y():
    print("y() called")
    return False

if x() and y():
    print("if branch")
else:
    print("else branch")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/short_circuit_6.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zkrácené vyhodnocení logických operátorů."""

def x():
    print("x() called")
    return False

def y():
    print("y() called")
    return True

if x() and y():
    print("if branch")
else:
    print("else branch")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/short_circuit_7.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zkrácené vyhodnocení logických operátorů."""

def x():
    print("x() called")
    return True

def y():
    print("y() called")
    return True

if x() and y():
    print("if branch")
else:
    print("else branch")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/short_circuit_8.py)



--

## Pokročilé konstrukty jazyka Python

* Generátory a iterátory
* Dekorátory



### Generátory

* Běžná funkce, která vygeneruje seznam o zadané délce

```python
def n_items(max_n):
    n, numbers = 0, []
    while n <= max_n:
        numbers.append(n)
        n += 1
    return numbers


lst = n_items(20)
print(lst)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/generators/gen_list.py)

* Generátor seznamu o zadané délce

```python
def generator(max_n):
    n = 0
    while n < max_n:
        yield n
        n += 1


for i in generator(10000):
    print(i)
    if i >= 10:
        break
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/generators/function_generator_1.py)

* Generátor seznamu o nekonečné (neomezené) délce

```python
def infinite_generator():
    n = 0
    while True:
        yield n
        n += 1


for i in infinite_generator():
    print(i)
    if i >= 10:
        break
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/generators/function_generator_2.py)

* Generátor konečného seznamu implementovaný jako třída

```python
class generator():

    def __init__(self, max_n):
        self.max_n = max_n
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max_n:
            current, self.n = self.n, self.n+1
            return current
        raise StopIteration()


for i in generator(10000):
    print(i)
    if i >= 10:
        break
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/generators/generator_class_1.py)

* Generátor nekonečného seznamu implementovaný jako třída

```python
class infinite_generator():

    def __init__(self):
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        current, self.n = self.n, self.n+1
        return current


for i in infinite_generator():
    print(i)
    if i >= 10:
        break

```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/generators/generator_class_2.py)



### Dekorátory

* Funkce vracející jinou funkci
    - jedná se tedy o funkci vyššího řádu
    - ovšem s odlišnou formou zápisu, která je uživatelsky přívětivá
    - lze použít větší množství dekorátorů

```python
def function_caller(function):

    def inner_function():
        print("Calling function...")
        function()
        print("...done")

    return inner_function


def hello():
    print("Hello!")


f = function_caller(hello)
f()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/decorators/return_function.py)

* Přepis předchozího příkladu jako dekorátoru

```python
def function_caller(function):

    def inner_function():
        print("Calling function...")
        function()
        print("...done")

    return inner_function


@function_caller
def hello():
    print("Hello!")


hello()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/decorators/decorator.py)

* Užitečný dekorátor - měření času

```python
# Original code:
# https://pythonbasics.org/decorators/#Real-world-examples


import time


def measure_time(func):

    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        print("Function took " + str(time.time()-t) + " seconds to run")
        return res

    return wrapper


@measure_time
def tested_function(n):
    time.sleep(n)


tested_function(1)
tested_function(2)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/decorators/measure_time.py)



### Větší množství dekorátorů

* Bez dekorátorů

```python
def hello():
    print("Hello!")


hello()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/decorators/decorators1.py)

* Jeden dekorátor
    
```python
def wrapper1(function):

    def inner_function():
        print("-"*40)
        function()
        print("-"*40)

    return inner_function


@wrapper1
def hello():
    print("Hello!")


hello()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/decorators/decorators2.py)

* Dva dekorátory

```python
def wrapper1(function):

    def inner_function():
        print("-"*40)
        function()
        print("-"*40)

    return inner_function


def wrapper2(function):

    def inner_function():
        print("="*40)
        function()
        print("="*40)

    return inner_function


@wrapper1
@wrapper2
def hello():
    print("Hello!")


hello()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/decorators/decorators3.py)


### Od getterů a setterů k properties

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Gettery a settery."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        self._poznamka = 124
        self._age = None

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "name: {name} {surname}   Salary: {salary}   Age: {age}".format(name=self._first_name,
                                                                               surname=self._surname,
                                                                               salary=self._salary,
                                                                               age=self._age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age

    def get_age(self):
        return self._age


# vytvoření tří instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Eda", "Wasserfall", 10000)

employee1.set_age(30)
employee2.set_age(40)

# výpis hodnot objektů
print(employee1)
print(employee2)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/employee_class_7.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Properties."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        self._poznamka = 124
        self._age = None

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "name: {name} {surname}   Salary: {salary}   Age: {age}".format(name=self._first_name,
                                                                               surname=self._surname,
                                                                               salary=self._salary,
                                                                               age=self._age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age

    def get_age(self):
        return self._age

    age = property(fget=get_age, fset=set_age)


# vytvoření tří instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Eda", "Wasserfall", 10000)

employee1.age = 30
employee2.age = 40

# výpis hodnot objektů
print(employee1)
print(employee2)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/employee_class_8.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Properties."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        self._poznamka = 124
        self._age = None

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "name: {name} {surname}   Salary: {salary}   Age: {age}".format(name=self._first_name,
                                                                               surname=self._surname,
                                                                               salary=self._salary,
                                                                               age=self._age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age


# vytvoření tří instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Eda", "Wasserfall", 10000)

employee1.age = 30
employee2.age = 40

# výpis hodnot objektů
print(employee1)
print(employee2)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/employee_class_9.py)



--

## Tvorba skriptů v Pythonu

* skript vs. nativní binární soubor
    - magické číslo
    - "shebang"

* vstupní bod aplikace
    - lze rozlišit import vs. spuštění z příkazového řádku

* parametry na příkazovém řádku
    - ukázka zpracování parametrů



### Shebang

* Rozpoznáván na prvním textovém řádku!
    - nelze přemístit

```python
#!/usr/bin/env python3
```

* Většinou je vhodné uvést i kódování
    - existuje několik způsobů
    - následující způsob je rozpoznán interpretrem

```python
# vim: set fileencoding=utf-8
```



### Vstupní bod aplikace (skriptu)

```python
if __name__ == "__main__":
    main()
```



### Zpracování parametrů předaných při spouštění skriptů

* Dostupné přes `sys.argv`
    - `len(sys.argv)` pro počet předaných parametrů
    - poměrně nešikovná práce
    - existují ovšem i lepší způsoby

* Využití knihovny `argparse`

```python
#!/usr/bin/env python3

from argparse import ArgumentParser

def cli_arguments():
    """Retrieve all CLI arguments provided by user."""
    # First of all, we need to specify all command line flags that are
    # recognized by this tool.
    parser = ArgumentParser()

    # All supported command line arguments and flags
    parser.add_argument("-a", "--address", dest="address", required=False,
                        help="Address of REST API for external data pipeline")

    parser.add_argument("-u", "--user", dest="user", required=False,
                        help="User name for basic authentication")

    parser.add_argument("-p", "--password", dest="password", required=False,
                        help="Password for basic authentication")

    parser.add_argument("-i", "--input", dest="input", default=None, required=False,
                        help="Specification of input file (with list of clusters, for example)")

    parser.add_argument("-c", "--compare-results", dest="compare_results", action="store_true",
                        default=None, required=False,
                        help="Compare two sets of results, each set stored in its own directory")

    parser.add_argument("-e", "--export", dest="export_file_name", required=False,
                        default="report.csv",
                        help="Name of CSV file with exported comparison results")

    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", default=None,
                        help="Make messages verbose", required=False)

    # Now it is time to parse flags, check the actual content of command line
    # and fill-in the object named `args`.
    return parser.parse_args()


def main():
    """Entry point to this script."""
    # Parse and process and command line arguments.
    args = cli_arguments()

    # Verbosity flag
    verbose = args.verbose


# If this script is started from command line, run the `main` function which is
# entry point to the processing.
if __name__ == "__main__":
    main()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/cli_args.py)



### Příklad využití knihovny `argparse`

```python
#!/usr/bin/env python3

from argparse import ArgumentParser

def cli_arguments():
    """Retrieve all CLI arguments provided by user."""
    # First of all, we need to specify all command line flags that are
    # recognized by this tool.
    parser = ArgumentParser()

    # All supported command line arguments and flags
    parser.add_argument("-a", "--address", dest="address", required=False,
                        help="Address of REST API for external data pipeline")

    parser.add_argument("-u", "--user", dest="user", required=False,
                        help="User name for basic authentication")

    parser.add_argument("-p", "--password", dest="password", required=False,
                        help="Password for basic authentication")

    parser.add_argument("-i", "--input", dest="input", default=None, required=False,
                        help="Specification of input file (with list of clusters, for example)")

    parser.add_argument("-c", "--compare-results", dest="compare_results", action="store_true",
                        default=None, required=False,
                        help="Compare two sets of results, each set stored in its own directory")

    parser.add_argument("-e", "--export", dest="export_file_name", required=False,
                        default="report.csv",
                        help="Name of CSV file with exported comparison results")

    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", default=None,
                        help="Make messages verbose", required=False)

    # Now it is time to parse flags, check the actual content of command line
    # and fill-in the object named `args`.
    return parser.parse_args()


def main():
    """Entry point to this script."""
    # Parse and process and command line arguments.
    args = cli_arguments()

    # Verbosity flag
    verbose = args.verbose


# If this script is started from command line, run the `main` function which is
# entry point to the processing.
if __name__ == "__main__":
    main()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/cli_args.py)

--



## Standardní knihovna, zajímavé moduly a balíčky

* Oproti některým jiným jazykům obsahuje Python velmi rozsáhlou základní knihovnu
    - https://docs.python.org/3/library/index.html

```python
fout = open("data.txt", "w")

for i in range(1, 11):
    fout.write(str(i) + "\n")

fout.close()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/file_write.py)

```python
fout = open("data.txt", "a")

for i in range(1, 11):
    fout.write(str(i) + "\n")

fout.close()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/file_append.py)

```python
for znak in range(ord("a"), ord("z") + 1):
    print(chr(znak))
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/ord_chr.py)


### Modul `string`

* Manipulace s řetězci
* Formátování řetězců
    - vlastní doménově specifický jazyk pro specifikaci formátu
* Příklad použiti

```python
print("hodnota: {value:5d}".format(value=42))
print("hodnota: {value:05d}".format(value=42))
```
* Formátování tabulky na výstupu

```python
for x in range(1, 11):
    y = 1.0/x
    print("1/{x:2d} = {y:5.3f}".format(x=x, y=y))
```

```python
for x in range(1, 11):
    y = 1.0/x
    print("1/{x:02d} = {y:5.3f}".format(x=x, y=y))
```

```python
for x in range(1, 11):
    y = 1.0/x
    print("1/{x:<2d} = {y:5.3f}".format(x=x, y=y))
```



### Modul `re`

* Podpora pro regulární výrazy
* Vlastní doménově specifický jazyk pro regulární výrazy
    - znaky se speciálním významem
        - kvalifikátory
        - atomy
        - znaky pro začátek a konec řádku
        - výrazy v []
        - třídy znaků
        - speciální znaky
* Součásti regulárních výrazů
    - kvalifikátory
        - `*`     sekvence 0..n atomů
        - `+`     sekvence 1..n atomů
        - `?`     žádný nebo jeden atom
        - `{m}`   v závorce je zapsán přesný počet atomů
        - `{m,}`  v závorce je zapsán minimální počet atomů
        - `{m,n}` v závorce je minimální a maximální počet atomů
    - atomy
        - `x`  konkrétní znak
        - `()` prázdný řetězec
        - `.`  jediný znak
        - `\X` řídicí znak či znak se zadaným kódem
        - `(xxx)` část výrazu, k níž lze později přistupovat (podle indexu)
    - znaky pro začátek a konec řádku
        - `^` nahrazuje začátek řádku
        - `$` nahrazuje konec řádku
    - výrazy v []
        - lze zde zapsat množinu znaků
        - při rozdělení znaků pomocí `-` se určuje rozsah `a-z`, `5-7` atd.
        - `^` negace - všechny znaky, které NEodpovídají dalšímu výrazu
    - třídy znaků
        - vnější závorky `[]` změní třídu znaků na množinu
    - speciální (řídicí) znaky
        - `\a`      alert (bell)
        - `\b`      backspace
        - `\B`      může se použít namísto `\\` (čitelnější)
        - `\e`      znak ESCape
        - `\n`      nový řádek
        - `\r`      návrat kurzoru
        - `\t`      tab
        - `\u1234`  znak se zadaným Unikódem
    - vybrané třídy znaků zapsané zkrácenou formou
        - `\d` `[[:digit:]]`
        - `\s` `[[:space:]]`
        - `\w` `[[:alnum:]_]`  jako `\d` a `_`
        - `\D` `[^[:digit:]]`
        - `\S` `[^[:space:]]`
        - `\W` `[^[:alnum:]_]` negace `\W`
* Příklady regulárních výrazů
    - regulární výraz pro IPv4 adresu (nepřesný!)
         `"(\[0-9]{1,3})\.(\[0-9]{1,3})\.(\[0-9]{1,3})\.(\[0-9]{1,3})"`
    - regulární výraz akceptující reálná čísla
         `"[-+]?([0-9]+\.?[0-9]*|\.[0-9]+)([eE][-+]?[0-8]+)?"`

```python
import subprocess
import re

def get_framebuffer_resolution(framebuffer_device):
    fbset_output = subprocess.check_output(["fbset", "-s", "-fb", framebuffer_device])

    for line in fbset_output.split("\n"):
        line = line.strip()
        if line.startswith("geometry"):
            print(line)
            parsed = re.match(r"geometry (\d+) (\d+)", line)
            return (parsed.group(1), parsed.group(2))

print(get_framebuffer_resolution("/dev/fb0"))

```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/get_framebuffer_resolution.py)

```python
HTTP_RE = re.compile(
    r"^(?:https://[^/]+\.s3\.amazonaws\.com/[0-9a-zA-Z/\-]+|"
    r"https://s3\.[0-9a-zA-Z\-]+\.amazonaws\.com/[0-9a-zA-Z\-]+/[0-9a-zA-Z/\-]+|"
    r"http://minio:9000/insights-upload-perma/[0-9a-zA-Z\.\-]+/[0-9a-zA-Z\-]+)\?"
    r"X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=[^/]+$"
)

def get(self, src):
    """Download a file from HTTP server and store it in a temporary file."""
    if src is None or not HTTP_RE.fullmatch(src):
        raise DataPipelineError(f"Invalid URL format: {src}")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/regular_expression2.py)



### Modul `datetime`

* Manipulace s časovými razítky
* Podpora pro časové zóny
* Třídy
    - `datetime.date`
    - `datetime.time`
    - `datetime.datetime`
    - `datetime.timedelta`


### Modul `pprint`

* "Hezký" tisk strukturovaných dat
* Třída `pprint.PrettyPrinter`
    - `indent=1`
    - `width=80`
    - `depth=None`
* Metoda `PrettyPrinter.format`
* Funkce `pprint.pprint`



### Modul `array`

* Paměťově efektivní uložení prvků v polích

* Podporované typy prvků

```
'b' signed char int           1
'B' unsigned char int         1
'u' wchar_t Unicode character 2
'h' signed short int          2
'H' unsigned short int        2
'i' signed int int            2
'I' unsigned int int          2
'l' signed long int           4
'L' unsigned long int         4
'q' signed long long int      8
'Q' unsigned long long int    8
'f' float float               4
'd' double float              8
```

```python
#!/usr/bin/env python3

"""Základní způsob použití modulu `array`."""

from array import array

a1 = array('l')
a2 = array('u', 'hello \u2567')
a3 = array('l', [1, 2, 3, 4, 5])
a4 = array('d', [1.0, 2.0, 3.14])

print(a1)
print(a2)
print(a3)
print(a4)

a3[3] = -1
print(a3)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/arrays1.py)

```python
#!/usr/bin/env python3

"""Základní způsob použití modulu `array` - celočíselné typy."""

from array import array

input_data = [i for i in range(0, 10)]

a1 = array('b', input_data)
a2 = array('B', input_data)
a3 = array('h', input_data)
a4 = array('H', input_data)
a5 = array('i', input_data)
a6 = array('I', input_data)
a7 = array('l', input_data)
a8 = array('L', input_data)

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)
print(a8)

print(a1.buffer_info()[1]*a1.itemsize)
print(a2.buffer_info()[1]*a2.itemsize)
print(a3.buffer_info()[1]*a3.itemsize)
print(a4.buffer_info()[1]*a4.itemsize)
print(a5.buffer_info()[1]*a5.itemsize)
print(a6.buffer_info()[1]*a6.itemsize)
print(a7.buffer_info()[1]*a7.itemsize)
print(a8.buffer_info()[1]*a8.itemsize)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/arrays2.py)

```python
#!/usr/bin/env python3

"""Základní způsob použití modulu `array` - zápis polí do souboru."""

from array import array

a1 = array('l')
a2 = array('u', 'hello \u2567')
a3 = array('l', [1, 2, 3, 4, 5])
a4 = array('d', [1.0, 2.0, 3.14])

with open("a1", "wb") as fout:
    a1.tofile(fout)

with open("a2", "wb") as fout:
    a2.tofile(fout)

with open("a3", "wb") as fout:
    a3.tofile(fout)

with open("a4", "wb") as fout:
    a4.tofile(fout)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/arrays3.py)

```python
#!/usr/bin/env python3

"""Základní způsob použití modulu `array` - čtení polí ze souboru."""

from array import array

a1 = array('l')
a2 = array('u')
a3 = array('l')
a4 = array('d')


with open("a1", "rb") as fin:
    a1.fromfile(fin, 0)

with open("a2", "rb") as fin:
    a2.fromfile(fin, 5)

with open("a3", "rb") as fin:
    a3.fromfile(fin, 5)

with open("a4", "rb") as fin:
    a4.fromfile(fin, 3)

print(a1)
print(a2)
print(a3)
print(a4)

print(a1.buffer_info()[1]*a1.itemsize)
print(a2.buffer_info()[1]*a2.itemsize)
print(a3.buffer_info()[1]*a3.itemsize)
print(a4.buffer_info()[1]*a4.itemsize)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/arrays4.py)



### Modul `queue`

* Synchronizované fronty
* Třída `queue.Queue`
    - klasická fronta se zadanou kapacitou
* Třída `queue.SimpleQueue`
    - klasická fronta s neomezenou kapacitou
* Třída `queue.LifoQueue`
    - zásobník se zadanou kapacitou
* Třída `queue.PriorityQueue`
    - prioritní fronta se zadanou kapacitou

* Podporované metody
    - `qsize`
    - `empty`
    - `full`
    - `put`
    - `put_nowait`
    - `get`
    - `get_nowait`
    - `join`

```python
import time
import threading
import queue


# vytvoření fronty
q = queue.Queue()


# simulace konzumenta
def consumer():
    while True:
        job = q.get()
        print(f'Starting consuming {job}')
        time.sleep(0.4)
        print(f'Consumed {job}')
        q.task_done()


# spuštění konzumenta
threading.Thread(target=consumer, daemon=True, name="první").start()

# vytvoření úloh v producentovi
for job in range(10):
    print(f'Producing {job}')
    q.put(job)

# čekání na zpracování všech zpráv ve frontě
q.join()
print('Done')
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/queues1.py)

```python
import time
import threading
import queue


# vytvoření fronty
q = queue.Queue()


# simulace konzumenta
def consumer():
    name = threading.current_thread().name
    while True:
        job = q.get()
        print(f'{name} thread: Starting consuming {job}')
        time.sleep(0.4)
        print(f'{name} thread: Consumed {job}')
        q.task_done()


# spuštění konzumentů
threading.Thread(target=consumer, daemon=True, name="1st").start()
threading.Thread(target=consumer, daemon=True, name="2nd").start()
threading.Thread(target=consumer, daemon=True, name="3rd").start()

# vytvoření úloh v producentovi
for job in range(10):
    print(f'Producing {job}')
    q.put(job)

# čekání na zpracování všech zpráv ve frontě
q.join()
print('Done')
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/queues2.py)

```python
import time
import threading
import queue


# vytvoření fronty
q = queue.Queue()


# simulace producenta
def producer():
    name = threading.current_thread().name
    for job in range(10):
        print(f'{name} thread: Starting producing {job}')
        q.put(job)
        time.sleep(0.3)
        print(f'{name} thread: Produced {job}')


# simulace konzumenta
def consumer():
    name = threading.current_thread().name
    while True:
        job = q.get()
        print(f'{name} thread: Starting consuming {job}')
        time.sleep(0.4)
        print(f'{name} thread: Consumed {job}')
        q.task_done()


# spuštění konzumentů
threading.Thread(target=consumer, daemon=True, name="1st").start()
threading.Thread(target=consumer, daemon=True, name="2nd").start()
threading.Thread(target=consumer, daemon=True, name="3rd").start()

# spuštění producentů
threading.Thread(target=producer, daemon=True, name="1st").start()
threading.Thread(target=producer, daemon=True, name="2nd").start()
threading.Thread(target=producer, daemon=True, name="3rd").start()
threading.Thread(target=producer, daemon=True, name="3rd").start()

# čekání na zpracování všech zpráv ve frontě
q.join()
print('Done')
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/queues3.py)

```python
import time
import threading
import queue


# vytvoření fronty
q = queue.Queue()


# simulace producenta
def producer():
    name = threading.current_thread().name
    for job in range(1000):
        print(f'{name} thread: Starting producing {job}')
        q.put(job)
        time.sleep(0.3)
        print(f'{name} thread: Produced {job}')


# simulace konzumenta
def consumer():
    name = threading.current_thread().name
    while True:
        job = q.get()
        print(f'{name} thread: Starting consuming {job}')
        time.sleep(0.4)
        print(f'{name} thread: Consumed {job}')
        q.task_done()


# spuštění konzumentů
threading.Thread(target=consumer, daemon=True, name="1st").start()
threading.Thread(target=consumer, daemon=True, name="2nd").start()
threading.Thread(target=consumer, daemon=True, name="3rd").start()

# spuštění producentů
threading.Thread(target=producer, daemon=True, name="1st").start()
threading.Thread(target=producer, daemon=True, name="2nd").start()
threading.Thread(target=producer, daemon=True, name="3rd").start()
threading.Thread(target=producer, daemon=True, name="3rd").start()

# čekání na zpracování všech zpráv ve frontě
q.join()
print('Done')
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/queues4.py)



### Modul `math`

* Matematické funkce

```python
# Vykreslení čar s různým sklonem
for i in range(1, 90, 5):
    # převod ze stupňů na radiány
    angle = math.radians(i)
    radius = 150
    # výpočet koncových bodů úseček
    x = radius * math.sin(math.radians(i))
    y = radius * math.cos(math.radians(i))
    # vykreslení jedné úsečky
    pygame.draw.line(display, WHITE, (WIDTH-1, 0), (WIDTH-x, y))
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/math_sin_cos.py)



### Modul `sys`

* Systémová volání resp. rozhraní pro ně

```python
class Bounds:

    def __init__(self,
                 xmin=sys.float_info.max, ymin=sys.float_info.max,
                 xmax=-sys.float_info.max, ymax=-sys.float_info.max):
        """Construct new bounds using given coordinates or default values."""
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/bounds.py)



### Modul `os`

* Funkce specifické pro různé operační systémy

```python
import os

def get_event_level():
    """Get level of events to monitor (errors only, or error and warnings)."""
    if os.environ.get("SENTRY_CATCH_WARNINGS", False):
        return logging.WARNING
    return logging.ERROR
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/environ.py)



### Modul `subprocess`

* Spuštění dalších procesů
* Zpracování vstupů a výstupů z těchto procesů

```python
import subprocess
import re

def get_framebuffer_resolution(framebuffer_device):
    fbset_output = subprocess.check_output(["fbset", "-s", "-fb", framebuffer_device])

    for line in fbset_output.split("\n"):
        line = line.strip()
        if line.startswith("geometry"):
            print(line)
            parsed = re.match(r"geometry (\d+) (\d+)", line)
            return (parsed.group(1), parsed.group(2))

print(get_framebuffer_resolution("/dev/fb0"))

```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/get_framebuffer_resolution.py)



### Práce s formátem JSON

* Serializace a deserializace dat
    - primitivní hodnoty
    - seznamy
    - n-tice
    - slovníky
    - slovníky ve slovnících atd.

* Introducing JSON
    - [https://www.json.org/json-en.html](https://www.json.org/json-en.html)

* Výstup datové struktury do formátu JSON

```python
#!/usr/bin/env python3

import json

data = {
        "x": 42,
        "y": [1, 2, 3, 4],
        "z": (1, 2, 3, 4),
        "w": "foobar"
        }

with open("test.json", "w") as fout:
    json.dump(data, fout)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/json_output_1.py)

* Zajištění lepší čitelnosti JSON výstupu

```python
#!/usr/bin/env python3

import json

data = {
        "x": 42,
        "y": [1, 2, 3, 4],
        "z": (1, 2, 3, 4),
        "w": "foobar"
        }

with open("test.json", "w") as fout:
    json.dump(data, fout, indent=4)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/json_output_2.py)

* Přečtení datového souboru uloženého ve formátu JSON

```python
#!/usr/bin/env python3

import json

with open("test.json", "r") as fin:
    data = json.load(fin)
    print(data)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/json_input.py)

--

## Multithreading

```python
#!/usr/bin/env python3

"""Multithreading."""

import threading
import time


def worker():
    threadName = threading.current_thread().name
    delay = 1
    n = 10
    for counter in range(1, n+1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))


# vytvoření a spuštění trojice vláken
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()

time.sleep(100)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/multithreading1.py)

```python
#!/usr/bin/env python3

"""Multithreading."""

import threading
import time


def worker(threadName, delay, n):
    for counter in range(1, n+1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))


# vytvoření a spuštění trojice vláken
threading.Thread(target=worker, args=("Thread-1", 0.5, 10)).start()
threading.Thread(target=worker, args=("Thread-2", 1.0, 10)).start()
threading.Thread(target=worker, args=("Thread-3", 1.5, 10)).start()

time.sleep(100)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/multithreading2.py)

```python
