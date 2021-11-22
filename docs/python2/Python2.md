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


# vytvoření dvou instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Eda", "Wasserfall", 10000)
employee3 = Employee("Přemysl", "Hájek", 25001)

# výpis hodnot objektů
print(employee1)
print(employee2)
print(employee1 == employee2)
```



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

* Lambda výraz bez parametrů

```python
f = lambda : "hello"
print(f())
```

* Někdy je zapotřebí parametr ignorovat
    - uvidíme při návrhu GUI u událostí (events)

```python
f = lambda _: "hello"
print(f("foo"))
```



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



### Větší množství dekorátorů

* Bez dekorátorů

```python
def hello():
    print("Hello!")


hello()
```

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

--



## Standardní knihovna, zajímavé moduly a balíčky

* Oproti některým jiným jazykům obsahuje Python velmi rozsáhlou základní knihovnu
    - https://docs.python.org/3/library/index.html



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

* Přečtení datového souboru uloženého ve formátu JSON

```python
#!/usr/bin/env python3

import json

with open("test.json", "r") as fin:
    data = json.load(fin)
    print(data)
```

--



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

--

## Testování

--

## Aplikace s GUI

--

---

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
