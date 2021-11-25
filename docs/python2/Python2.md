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

* "Name mangling" interních atributů

```python
class Employee:
    """Třída reprezentující zaměstnance."""

    __counter = 0

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        Employee.inc_counter()

    def display_employee(self):
        """Metoda pro výpis hodnoty objektu."""
        print("Full name: {name} {surname}   Salary: {salary}".format(
            name=self._first_name,
            surname=self._surname,
            salary=self._salary))

    @classmethod
    def inc_counter(cls):
        cls.__counter += 1

    @classmethod
    def num_employees(cls):
        return cls.__counter


def test():
    # vytvoření dvou instancí třídy
    employee1 = Employee("Eda", "Wasserfall", 10000)
    print("Now we have", Employee.num_employees(), "employees")

    employee2 = Employee("Přemysl", "Hájek", 25001)
    print("Now we have", Employee.num_employees(), "employees")


test()
print("Now we have", Employee.num_employees(), "employees")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/name_mangling.py)



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

* Další příklady na polymorfismus

```python
class Person:

    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        print("Person.__init__")
        self._first_name = first_name
        self._surname = surname

    def get_name(self):
        return "Person:  {} {}".format(self._first_name, self._surname)

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

    def get_name(self):
        return "Student: {} {}".format(self._first_name, self._surname)

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

    def get_name(self):
        return "Employee: {} {}".format(self._first_name, self._surname)

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Employee** Full name: {name} {surname}   Salary: {salary}".format(
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
    print(p.get_name())
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/polymorphism3.py)

```python
class Person:

    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        print("Person.__init__")
        self._first_name = first_name
        self._surname = surname

    def get_name(self):
        return "Person:  {} {}".format(self._first_name, self._surname)

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

    def get_name(self):
        return "Student: {} {}".format(self._first_name, self._surname)

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

    def calc_bonus(self):
        return self._salary * 0.5

    def get_name(self):
        return "Employee: {} {}".format(self._first_name, self._surname)

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Employee** Full name: {name} {surname}   Salary: {salary}".format(
                name=self._first_name,
                surname=self._surname,
                salary=self._salary)


class Manager(Employee):
    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        print("Manager.__init__")
        super().__init__(first_name, surname, salary)

    def calc_bonus(self):
        return self._salary * 0.75


e1 = Employee("Eric", "Iverson", 10000)
m1 = Manager("aaa", "bbb", 10000)

print(e1.calc_bonus())
print(m1.calc_bonus())
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/OOP/polymorphism4.py)



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

* Další příklady

```python
def increment_by(n):

    return lambda x: x+n


def add(x):
    return x+x

i1 = increment_by(2)
print(i1(1))
print(i1(10))

i2 = increment_by(100)
print(i2(1))
print(i2(10))

print(add)
print(i1)
print(i2)

```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/clojure_lambda.py)

```python
def counter(start=0, step=1):
    cnt = start

    def impl():
        nonlocal cnt
        cnt += step
        return cnt

    return impl


c1 = counter(10, 1)
c2 = counter(0, 2)
c3 = counter(100, -10)

for i in range(10):
    print("c1", c1())

print()

for i in range(10):
    print("c2", c2())

print()

for i in range(10):
    print("c3", c3())
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/closure3.py)



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

* Proč generátorová notace seznamu?
    - ostatní způsoby jsou dlouhé
    - a nejsou idiomatické

```python
seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(seznam)

seznam2 = []

for item in seznam:
    seznam2.append(item*2)

print(seznam2)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/list_comprehension_why.py)

```python
seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(seznam)

seznam3 = []

for item in seznam:
    if item % 3 == 0:
        seznam3.append(item)

print(seznam3)

seznam3B = [item for item in seznam if item % 3 == 0]

print(seznam3B)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/list_comprehension_why_2.py)



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

* Výpočet faktoriálu s využitím `reduce`

```python
#!/usr/bin/env python
# encoding=utf-8

"""Výpočet faktoriálu pomocí reduce."""

from functools import reduce


def factorial(n):
    """Výpočet faktoriálu pomocí reduce."""
    return reduce(lambda a, b: a * b, range(1, n + 1))


# výpočet 10!
print(factorial(10))

# tabulka s hodnotami n!
for n in range(1, 11):
    print(n, factorial(n))
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Functional/factorial.py)



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

* Generátorová notace...

```python
#!/usr/bin/env python
# encoding=utf-8

seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

g1 = (item for item in seznam)

g2 = (item*2 for item in seznam)

g3 = (item for item in seznam if item % 3 == 0)

print(seznam)
print(g1)
print(g2)
print(g3)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/generators/generator_comprehension1.py)

```python
#!/usr/bin/env python
# encoding=utf-8

seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

g1 = list(item for item in seznam)

g2 = list(item*2 for item in seznam)

g3 = list(item for item in seznam if item % 3 == 0)

print(seznam)
print(g1)
print(g2)
print(g3)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/generators/generator_comprehension2.py)



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

* Metoda `split`


```python
x = "prvni,druhy,treti,ctvrty"

l = x.split(",")
```

* Metoda `join`

```python
l = ["prvni", "druhy", "treti", "ctvrty"]

x = ",".join(l)
```

* Metoda `replace`

```python
"vccvxvcxz".replace("c", "-")
'v--vxv-xz'
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
         `"[-+]?([0-9]+\.?[0-9]*|\.[0-9]+)([eE][-+]?[0-9]+)?"`

* První možné řešení:

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

* Časově efektivnější řešení:

```python
import subprocess
import re

def get_framebuffer_resolution(framebuffer_device):
    fbset_output = subprocess.check_output(["fbset", "-s", "-fb", framebuffer_device])

    regexp = re.compile(r"geometry (\d+) (\d+)")

    for line in fbset_output.split("\n"):
        line = line.strip()
        if line.startswith("geometry"):
            print(line)
            parsed = regexp.match(line)
            return (parsed.group(1), parsed.group(2))

print(get_framebuffer_resolution("/dev/fb0"))

```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/get_framebuffer_resolution2.py)

* Reálný příklad:

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

* Online nástroje
    - [https://extendsclass.com/regex-tester.html](https://extendsclass.com/regex-tester.html)
    - [https://regex101.com/](https://regex101.com/)



### Modul `datetime`

* Manipulace s časovými razítky
* Podpora pro časové zóny
* Třídy
    - `datetime.date`
    - `datetime.time`
    - `datetime.datetime`
    - `datetime.timedelta`

```python
import datetime

dt = datetime.datetime.now()
print(dt)

s = dt.strftime("%Y-%m-%d")
print(s)

s = dt.strftime("%d.%m.%Y")
print(s)

s = dt.strftime("%m/%d/%Y")
print(s)

s = dt.strftime("%H:%m:%S")
print(s)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/strftime.py)

```python
import datetime

s = "2021-11-12"

dt = datetime.datetime.strptime(s, "%Y-%m-%d")
print(dt)

s = "2021-11-12 10:20:30"

dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print(dt)

s = "10:20:30"

dt = datetime.datetime.strptime(s, "%H:%M:%S")
print(dt)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/strptime.py)



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
'i' signed int int            2 (4)
'I' unsigned int int          2 (4)
'l' signed long int           4 (8)
'L' unsigned long int         4 (8)
'q' signed long long int      8 (16)
'Q' unsigned long long int    8 (16)
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
#!/usr/bin/env python3

import queue

q = queue.Queue(500)

for item in range(10):
    print("Size", q.qsize())
    print("Empty?", q.empty())
    print("Full?", q.full())
    q.put("prvek # {}".format(item))

while not q.empty():
    print("Read item:", q.get())
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/queue_example.py)

```python
#!/usr/bin/env python3

import queue

q = queue.SimpleQueue()

for item in range(10):
    print("Size", q.qsize())
    print("Empty?", q.empty())
    print("Full?", q.full())
    q.put("prvek # {}".format(item))

while not q.empty():
    print("Read item:", q.get())
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/simple_queue_example.py)

```python
#!/usr/bin/env python3

import queue

q = queue.LifoQueue(500)

for item in range(10):
    print("Size", q.qsize())
    print("Empty?", q.empty())
    print("Full?", q.full())
    q.put("prvek # {}".format(item))

while not q.empty():
    print("Read item:", q.get())
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/stack_example.py)

```python
#!/usr/bin/env python3

import queue
import random

q = queue.PriorityQueue(40)

for item in range(30):
    print("Size", q.qsize())
    print("Empty?", q.empty())
    print("Full?", q.full())

    value = random.randint(1, 20)
    print(value)
    q.put("prvek # {:2d}".format(value))


while not q.empty():
    print("Read item:", q.get())
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/priority_queue_example.py)

* Fronty jako komunikační médium mezi vlákny

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

* Praktická nutnost v 21.století
    - multijádrová CPU
    - výkon jednotlivých jader již nestoupá (závratně)
    - distributované systémy
    - paměťová lokalita
* Několik úrovní souběžnosti
    - multiprocessing
    - multithreading
    - gorutiny
    - SIMD/MIMD
* Problémy
    - zcela jiný koncept přístupu k problémům
    - deadlock
    - starvation
    - ...
* Řešení
    - CSP
    - python-csp
    - PyCSP
    - Trellis
    - STM
    - Kamaelia
    - Multiprocessing



### Balíček `threading`

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

* Dlouhodobé procesy (pro kontrolu, co se děje "uvnitř")

```python
#!/usr/bin/env python3

"""Multithreading."""

import threading
import time


def worker(threadName, delay, n):
    for counter in range(1, n+1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))


# vytvoření trojice vláken
t1 = threading.Thread(target=worker, args=("Thread-1", 0.5, 10))
t2 = threading.Thread(target=worker, args=("Thread-2", 1.0, 10))
t3 = threading.Thread(target=worker, args=("Thread-3", 1.5, 10))

# spuštění všech vláken
t1.start()
t2.start()
t3.start()

# čekání na dokončení všech vláken
t1.join()
t2.join()
t3.join()

print("Done!")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/multithreading3.py)



### Komunikace mezi vlákny přes fronty

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


### Vlákna běžící na pozadí, čekání na dokončení vláken

```python
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

# automaticky se čeká na dokončení vláken
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/multithreading_no_join_no_deamon.py)

```python
import threading
import time


def worker():
    threadName = threading.current_thread().name
    delay = 1
    n = 10
    for counter in range(1, n+1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))


# vytvoření a spuštění trojice vláken v režimu daemon
threading.Thread(target=worker, daemon=True).start()
threading.Thread(target=worker, daemon=True).start()
threading.Thread(target=worker, daemon=True).start()

# na dokončení vláken se nečeká!
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/multithreading_no_join_deamon.py)

```python
import threading
import time


def worker():
    threadName = threading.current_thread().name
    delay = 1
    n = 10
    for counter in range(1, n+1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))


# vytvoření a spuštění trojice vláken v režimu daemon
t1 = threading.Thread(target=worker, daemon=True)
t2 = threading.Thread(target=worker, daemon=True)
t3 = threading.Thread(target=worker, daemon=True)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/multithreading_join_deamon.py)

```python
import threading
import time


def worker(threadName, delay, n):
    for counter in range(1, n+1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))


# vytvoření trojice vláken
t1 = threading.Thread(target=worker, args=("Thread-1", 0.5, 10))
t2 = threading.Thread(target=worker, args=("Thread-2", 1.0, 10))
t3 = threading.Thread(target=worker, args=("Thread-3", 1.5, 10))

# spuštění všech vláken
t1.start()
t2.start()
t3.start()

# čekání na dokončení všech vláken
t3.join(timeout=5)

if t3.is_alive():
    print("wait timeout")
else:
    print("t3 has finished")

t2.join()
print("t2 has finished")

t1.join()
print("t1 has finished")


print("Done!")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/multithreading_timeout.py)


### Balíček `concurrent.futures`

* Nový přístup k plánování práce "workerů"

```python
from concurrent.futures.thread import ThreadPoolExecutor
import time


def worker(threadName, delay, n):
    for counter in range(1, n+1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))



with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(worker, "Thread-1", 0.5, 10)
    executor.submit(worker, "Thread-2", 1.0, 10)
    executor.submit(worker, "Thread-3", 1.5, 10)


print("Done!")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/thread_pool_1.py)

```python
from concurrent.futures.thread import ThreadPoolExecutor
import time


def worker(threadName, delay, n):
    for counter in range(1, n+1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))
    print("{}: DONE!".format(threadName))



workers = 10

with ThreadPoolExecutor(max_workers=workers) as executor:
    for w in range(workers):
        executor.submit(worker, "Thread-{}".format(w+1), 0.5 + w/10.0, 10)


print("Done!")
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/thread_pool_2.py)



### Balíček `multiprocessing`

```python
from multiprocessing import Process


def worker(name):
    print("hello", name)


def main():
    p = Process(target=worker, args=("foo",))
    p.start()
    p.join()


if __name__ == '__main__':
    print("Running main")
    main()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/multiprocessing1.py)

```python
from multiprocessing import Process
import time


def worker(name):
    print("hello", name)
    time.sleep(5)
    print("done", name)


def main():
    ps = []

    for name in ("foo", "bar", "baz", "other"):
        p = Process(target=worker, args=(name,))
        p.start()
        ps.append(p)

    for p in ps:
        p.join()


if __name__ == '__main__':
    print("Running main")
    main()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/multiprocessing2.py)

```python
from multiprocessing import Process
import time


def worker(name):
    print("hello", name)
    time.sleep(5)
    print("done", name)


def main():
    ps = [Process(target=worker, args=(name,)) for name in ("foo", "bar", "baz", "other")]

    for p in ps:
        p.start()

    for p in ps:
        p.join()


if __name__ == '__main__':
    print("Running main")
    main()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/multiprocessing3.py)

```python
from multiprocessing import Process, Queue
import time


def worker(name, q):
    while True:
        cmd = q.get()
        print(name, cmd)
        if cmd == "quit":
            print("Quitting")
            return
        time.sleep(1)


def main():
    q = Queue()

    ps = [Process(target=worker, args=(name, q)) for name in ("foo", "bar", "baz")]

    for p in ps:
        p.start()

    for i in range(10):
        q.put("command {}".format(i))

    for i in range(3):
        q.put("quit")

    for p in ps:
        p.join()


if __name__ == '__main__':
    print("Running main")
    main()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/multiprocessing4.py)

```python
from multiprocessing import Process, Pipe
import time


def worker(name, conn):
    while True:
        cmd = conn.recv()
        print("{} received {}".format(name, cmd))
        if cmd == "quit":
            return
        else:
            conn.send("{} accepted {}".format(name, cmd))
        time.sleep(1)


def main():
    parent_conn, child_conn = Pipe()

    p = Process(target=worker, args=("Worker", child_conn))
    p.start()

    for i in range(10):
        parent_conn.send("command {}".format(i))
        print(parent_conn.recv())

    parent_conn.send("quit")

    p.join()


if __name__ == '__main__':
    main()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/stdlib/multiprocessing5.py)



## CPython a jeho alternativy

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

* Speciální implementace
    - Cython
    - RPython
    - Numba

* Python pro webový browser
    - Brython

### CPython

### Jython

### Iron Python

### Pypy

### MicroPython

* 2013, mikrořadič pyboard
* Dnes dostupný na více jednodeskových mikropočítačů
    - Micro Bit
    - Arduino
    - ESP32
    - ESP8255
    - PIC16...
* Typické omezení
    - 256 kB ROM
    - 16 kB RAM
* Dva možné režimy činnosti
    - interpret přímo na CPU/MCU
    - překlad do hex/objektového kódu
* Repositář
    - https://github.com/micropython/micropython
    - překlad pro každý CPU/MCU zvlášť



### Rozdíly CPython vs MicroPython

* Chybí některé standardní knihovny
* Navíc přístup k hardware

```python
from machine import Pin
pin = Pin(0, Pin.IN)
print(pin.value())
```

```python
from machine import Pin
pin = Pin(14, Pin.OUT)
pin.value(1)
```


### MicroPython pro MicroBit

* MicroPython pro MicroBit
    - http://microbit.org/guide/python/
    - Online editor: http://python.microbit.org/v/1
    - převod zdrojového kódu do Intel hex formátu
    - upload v Intel hex formátu



### RPython

* Určen pro překlad programů napsaných v podmnožině programovacího jazyka Python do nativního kódu
* Snaží se odvozovat datové typy proměnných, argumentů i návratových hodnot funkcí na základě analýzy grafu (CFG)
* Počáteční písmeno v názvu „RPython“ znamená „restricted“,

### Cython

* Tento překladač pracuje poněkud odlišným způsobem než RPython
* Transformace (transpilace) do jazyka C
* Ve chvíli, kdy Cython nezná datový typ funkce/proměnné/argumentu, použije `PyObject *`
* Rozšiřuje jazyk Python o další klíčová slova, především pak o slovo `cdef`

```python
def calc(width, height, maxiter, palette):
    ...
    ...
    ...
```

```
cdef calc(int width, int height, int maxiter, palette):
    ...
    ...
    ...
```



### Numba

--

## Užitečné nástroje pro Python

* pydocstyle
    - testuje, zda jsou správně zapsány komentáře
* pycodestyle (pep8)
    - kontroluje styl zápisu programů
    - udržuje štábní kulturu



## Datové formáty, perzistentní úložiště, databáze

* Pickle
* Shelve



### Pickle

* Serializace a deserializace (libovolných) hodnot a objektů

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Serializce hodnot do souboru."""

import pickle

data = {
        "x": "Hello",
        "y": "world",
        "z": [1, 2, 3, 4],
        "w": (1, 2, 3, 4)}

with open("test", "wb") as fout:
    pickle.dump(data, fout)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/serialization/pickle_write.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Serializce hodnot do souboru se specifikací protokolu."""

import pickle

data = {
        "x": "Hello",
        "y": "world",
        "z": [1, 2, 3, 4],
        "w": (1, 2, 3, 4)}

with open("test", "wb") as fout:
    pickle.dump(data, fout, pickle.HIGHEST_PROTOCOL)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/serialization/pickle_write_protocol.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Deserializce hodnot ze souboru."""

import pickle

with open("test", "rb") as fin:
    data = pickle.load(fin)
    print(data)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/serialization/pickle_read.py)



### Pickle - serializace a deserializace objektů

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Serializace objektů do souboru."""

import pickle


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


with open("test", "wb") as fout:
    data = [employee1, employee2, employee3]
    pickle.dump(data, fout)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/serialization/employee_class_pickle_write.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Serializace objektů do souboru."""

import pickle


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


with open("test", "rb") as fin:
    employees = pickle.load(fin)
    for employee in employees:
        print(employee)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/serialization/employee_class_pickle_read.py)



### Shelve

* Databáze hodnot/objektů

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zápis prvků do databáze."""

import shelve

with shelve.open("test") as db:
    db["x"] = "Hello"
    db["y"] = "world"
    db["z"] = [1, 2, 3, 4]
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/serialization/shelve_db_write.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Čtení prvků z databáze."""

import shelve

with shelve.open("test") as db:
    print(db["x"])
    print(db["y"])
    print(db["z"])
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/serialization/shelve_db_read.py)



### Shelve - ukládání objektů do databáze

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zápis objektů do databáze."""

import shelve


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


with shelve.open("test") as db:
    db["employee1"] = employee1
    db["employee2"] = employee2
    db["employee3"] = employee3
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/serialization/employee_class_shelve_write.py)

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Přečtení objektů z databáze."""

import shelve


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


with shelve.open("test") as db:
    print(db["employee1"])
    print(db["employee2"])
    print(db["employee3"])
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/serialization/employee_class_shelve_read.py)


## Kafka

```python
#!/usr/bin/env python3

from kafka import KafkaProducer
from time import sleep
from json import dumps

server = 'localhost:9092'
topic = 'upload'

print('Connecting to Kafka')
producer = KafkaProducer(bootstrap_servers=[server],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))
print('Connected to Kafka')

for i in range(1000):
    data = {'counter': i}
    producer.send(topic, value=data)
    sleep(5)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Kafka/producer1.py)

```python
#!/usr/bin/env python3

import sys
from kafka import KafkaConsumer

server = 'localhost:9092'
topic = 'upload'
group_id = 'group1'

print('Connecting to Kafka')
consumer = KafkaConsumer(topic,
                         group_id=group_id,
                         bootstrap_servers=[server],
                         auto_offset_reset='earliest')
print('Connected to Kafka')

try:
    for message in consumer:
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                             message.offset, message.key, message.value))
except KeyboardInterrupt:
    sys.exit()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Kafka/consumer1.py)

```python
#!/usr/bin/env python3

import sys
from kafka import KafkaConsumer, TopicPartition

server = 'localhost:9092'
topic = 'upload'
group_id = 'group1'

print('Connecting to Kafka')
consumer = KafkaConsumer(group_id=group_id,
                         bootstrap_servers=[server])
print('Connected to Kafka')

tp = TopicPartition(topic=topic, partition=0)
consumer.assign([tp])
consumer.seek(tp, 0)

try:
    for message in consumer:
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                             message.offset, message.key, message.value))
except KeyboardInterrupt:
    sys.exit()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/Kafka/consumer2.py)

--

## Testování

* Základní technologie testování
* Pyramida testů
* Zmrzlinový kornout jako antipattern
* Jednotkové testy
* Modul `pytest`
* Nástroj Hypothesis
* Fuzzy testy



### Základní technologie testování

* Velké množství testovacích frameworků

```
1 	unittest
2 	doctest
3 	pytest
4 	nose
5 	testify
6 	Trial
7 	Twisted
8 	subunit
9 	testresources
10 	reahl.tofu
11 	unit testing
12 	testtools
13 	Sancho
14 	zope.testing
15 	pry
16 	pythoscope
17 	testlib
18 	pytest
19 	dutest
```



### Pyramida typů testů

* Různé podoby testovací pyramidy

- [Pyramida #1](https://www.root.cz/obrazek/408774/)

- [Pyramida #2](https://www.root.cz/obrazek/408775/)

- [Pyramida #3](https://www.root.cz/obrazek/408776/)

- [Pyramida #4](https://www.root.cz/obrazek/408777/)



### Antipattern - zmrzlinový kornout

* Na první pohled může vypadat "logicky"
* Ovšem velmi pracné a časově náročné
    - navíc se UI může často měnit
    - (bikeshedding)

- [Kornout](https://www.root.cz/obrazek/408773/)



### Jednotkové testy

* Co považovat za jednotku?
* Tvoří je většinou autor kódu
    - spravedlnost
    - čím složitější kód, tím hůře se testuje!
* Lze zjistit pokrytí kódu testy
    - code coverage



### Testy komponent

* Jednotkové testy nedokáží odhalit problémy na vyšších úrovních abstrakce
    - například problematické sestavení jednotlivých modulů do vyšších celků

- [Okno](https://www.root.cz/obrazek/408778/)

* Někdy velmi komplikované/nemožné testovat (reálný HW)
[Proton M](https://www.youtube.com/watch?v=vqW0LEcTAYg)



# Systémové testy, akceptační testy

* Systémové testy se většinou rozdělují do dalších podkategorií
    - smoke testy (původ jména)
    - pouze velmi rychle zjišťují, zda je zajištěna alespoň minimální míra funkčnosti aplikace předtím, než se spustí složitější a časově mnohem náročnější testy
    - pokud smoke testy zhavarují, vrací se aplikace zpět k vývojářům a popř. k devops týmu

* Po úspěšném provedení smoke testů se mohou spouštět systémové testy
    - primárním účelem je ověření, jestli aplikace (služba) sestavená do jednoho celku pracuje korektně
    - tvorbou těchto testů již může být pověřen samostatný tým

* Testy akceptační jsou ještě zajímavější
    - na jejich vytváření se může podílet i zákazník



--

## Aplikace s GUI

* Tkinter
* appJar
* PyGTK
* PyGObject
* PyQt
* PySide
* wxPython
* Kivy
* Pyforms
* PyjamasDesktop (pyjs Desktop)

* Knihovny pro tvorbu grafického uživatelského rozhraní v Pythonu
    - [https://www.root.cz/clanky/knihovny-pro-tvorbu-grafickeho-uzivatelskeho-rozhrani-v-pythonu/](https://www.root.cz/clanky/knihovny-pro-tvorbu-grafickeho-uzivatelskeho-rozhrani-v-pythonu/)



### Tkinter

* tvoří rozhraní ke knihovně Tk
* Tk je takzvaný toolkit
* pro jednoduchý a rychlý vývoj programů obsahujících grafické uživatelské rozhraní
* úsporný, flexibilní a přitom čitelný zápis programu se specifikací
    - ovládacích prvků
    - jejich umístění v oknech
    - vlastností
    - callback funkcí volaných v důsledku uživatelské činnosti

```python
#!/usr/bin/env python

from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root, text="Hello world!")

label.pack()

root.mainloop()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/gui/tkinter.py)



### appJar

* použití ve výuce
* nejrychlejší a současně i nejjednodušší způsob, jak v Pythonu vytvořit aplikaci s grafickým uživatelským rozhraním
* některé pokročilejší ovládací prvky nejsou k dispozici

```python
#!/usr/bin/env python

from appJar import gui

app = gui()

app.addLabel("title", "Hello world!")

app.go()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/gui/appjar.py)



### PyGTK

* určena pro desktopová prostředí založená na GTK+, konkrétně ovšem na GTK+ 2.x
* dnes již zastaralé
* složitější práce v porovnání s Tkinterem a appJarem

```python
import pygtk
pygtk.require('2.0')
import gtk


def delete_event(widget, event, data=None):
    print "delete event occurred"
    return False


def destroy(widget, data=None):
    print "destroy signal occurred"
    gtk.main_quit()


window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.connect("delete_event", delete_event)
window.connect("destroy", destroy)

label = gtk.Label("Hello world!")
window.add(label)
label.show()

window.show()
gtk.main()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/gui/pygtk.py)

```python
import pygtk
pygtk.require('2.0')
import gtk


window = gtk.Window(gtk.WINDOW_TOPLEVEL)

label = gtk.Label("Hello world!")
window.add(label)
label.show()

window.show()
gtk.main()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/gui/pygtk_no_events.py)



### PyGObject

* pro novější verze GTK
* velké množství aplikací, například https://en.wikipedia.org/wiki/Category:Software_that_uses_PyGObject
* ne zcela vhodné pro multiplatformní aplikace



### PyQt

* rozhraní pro Qt, které je používáné (nejenom) v desktopovém prostředí KDE
    - ve skutečnosti se s Qt setkáme i v iOS či v Androidu
* Qt je ucelený framework
    - v PyQt mají vývojáři k dispozici rozhraní se zhruba 440 třídami a 6000 funkcemi i metodami
    - grafické uživatelské rozhraní (i s použitím deklarativního jazyka QML)
    - widget QScintilla používaný v textových editorech a procesorech
    - relační databáze
    - vektorový grafický formát SVG
    - práce se soubory XML
    - apod.

```python
import sys

# zajisteni importu noveho rozhrani
import sip

sip.setapi('QDate', 2)
sip.setapi('QDateTime', 2)
sip.setapi('QString', 2)
sip.setapi('QTextStream', 2)
sip.setapi('QTime', 2)
sip.setapi('QUrl', 2)
sip.setapi('QVariant', 2)

from PyQt4.Qt import *

qt_application = QApplication(sys.argv)

label = QLabel('Hello world!')

label.show()

qt_application.exec_()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/gui/pyqt.py)



### PySide

* podobné PyQt
* odlišné licencování
* dnes používanější

```python
import sys

from PySide.QtCore import *
from PySide.QtGui import *

qt_application = QApplication(sys.argv)

label = QLabel('Hello world!')

label.show()

qt_application.exec_()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/gui/pyside1.py)

```python
import sys

from PySide.QtCore import *
from PySide.QtGui import *

qt_application = QApplication(sys.argv)


class HelloWorldLabel(QLabel):
    def __init__(self):
        QLabel.__init__(self, "Hello world!")

        self.setMinimumSize(QSize(600, 400))
        self.setAlignment(Qt.AlignCenter)
        self.setWindowTitle('Hello world!')

    def run(self):
        self.show()
        qt_application.exec_()


HelloWorldLabel().run()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/gui/pyside2.py)



### wxPython

* zajišťuje rozhraní k populární GUI knihovně wxWidgets
* původně wxWindows -> wxWidgets
* multiplatformní aplikace

```python
# vim: set fileencoding=utf-8

from wx import App, Frame, ID_ANY

# vytvoření instance objektu představujícího běžící aplikaci
app = App()

# vytvoření hlavního okna se specifikací jeho vlastností a titulku
frame = Frame(None, ID_ANY, "wxPython!")

# zobrazení hlavního okna aplikace
frame.Show(True)

# vstup do smyčky pro čtení a zpracování událostí (event loop)
app.MainLoop()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/gui/wxpython.py)



### Kivy

* ucelený framework určený především pro tvorbu aplikací pro mobilní platformy
* použití i na běžných desktopech
* akcelerace vykreslení prvků přes OpenGL ES 2
* pro deklaraci GUI použít speciální jazyk nazvaný K
    - hraje podobnou roli jako například QML (Qt Modeling Language)

```python
from kivy.app import App
from kivy.uix.label import Label


class TestApp(App):
    def build(self):
        return Label(text='Hello World')


TestApp().run()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/gui/kivy.py)



### Pyforms

* pro desktopové i webové aplikace
* interně může používat PySide pro desktopové aplikace



### PyjamasDesktop (pyjs Desktop)

* především webové aplikace
* desktopové aplikace založené na webových technologiích
    - viz Electron
    - editor Atom
    - VSCode atd.
* transpilace Pythonu do JavaScriptu
--


--

## Užitečné odkazy

* Python Quick Reference:
    - [http://rgruet.free.fr/#QuickRef](http://rgruet.free.fr/#QuickRef)
* Python docs:
    - [http://www.python.org/doc/](http://www.python.org/doc/)
* PEP 8:
    - [http://www.python.org/dev/peps/pep-0008/](http://www.python.org/dev/peps/pep-0008/)
* pep8.py:
    - [http://pypi.python.org/pypi/pep8/](http://pypi.python.org/pypi/pep8/)
* pylint:
    - [http://www.logilab.org/project/pylint](http://www.logilab.org/project/pylint)
* Epydoc:
    - [http://epydoc.sourceforge.net/](http://epydoc.sourceforge.net/)
* Sphinx:
    - [http://sphinx-doc.org/](http://sphinx-doc.org/)
* Python in Python:
    - [http://pypy.org/](http://pypy.org/)
* The key differences between Python 2.7.x and Python 3.x with examples:
    - [http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html)
* Language differences and workarounds:
    - [http://python3porting.com/differences.html](http://python3porting.com/differences.html)
* Everything you did not want to know about Unicode in Python 3:
    - [http://lucumr.pocoo.org/2014/5/12/everything-about-unicode/](http://lucumr.pocoo.org/2014/5/12/everything-about-unicode/)
* Unicode (Wikipedia):
    - [https://en.wikipedia.org/wiki/Unicode](https://en.wikipedia.org/wiki/Unicode)
* Dive Into Python:
    - [http://www.diveintopython.net/](http://www.diveintopython.net/)
* Dive into Python 3:
    - [http://www.diveintopython3.net/](http://www.diveintopython3.net/)
* Testování webových aplikací s REST API z Pythonu
    - [https://www.root.cz/clanky/testovani-webovych-aplikaci-s-rest-api-z-pythonu/](https://www.root.cz/clanky/testovani-webovych-aplikaci-s-rest-api-z-pythonu/)
* Testování aplikací s využitím nástroje Hypothesis
    - [https://www.root.cz/clanky/testovani-aplikaci-s-vyuzitim-nastroje-hypothesis/](https://www.root.cz/clanky/testovani-aplikaci-s-vyuzitim-nastroje-hypothesis/)
* Použití Pythonu pro tvorbu testů: od jednotkových testů až po testy UI
    - [https://www.root.cz/clanky/pouziti-pythonu-pro-tvorbu-testu-od-jednotkovych-testu-az-po-testy-ui/](https://www.root.cz/clanky/pouziti-pythonu-pro-tvorbu-testu-od-jednotkovych-testu-az-po-testy-ui/)
* Testování nativních funkcí s využitím programovacího jazyka Python
    - [https://www.root.cz/clanky/testovani-nativnich-funkci-s-vyuzitim-programovaciho-jazyka-python/](https://www.root.cz/clanky/testovani-nativnich-funkci-s-vyuzitim-programovaciho-jazyka-python/)

