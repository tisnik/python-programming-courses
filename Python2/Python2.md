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

! examples/OOP/employee_class_0.py



### Objekty

* Instance třídy
* Z jedné třídy lze vytvořit více objektů
    - dtto pro další datové typy
    - (seznam, slovník, celé číslo)
* Třída -> datový typ
* Objekt -> hodnota daného datového typu

! examples/OOP/employee_class_1.py



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

! examples/OOP/class_attribute.py



### Konstruktor

* Zavolán automaticky při konstrukci objektu
* Může akceptovat další parametry
* Může přistupovat k atributům (většinou je vytváří)

! examples/OOP/employee_class_2.py



### Destruktor

* Zavolán automaticky při uvolňování objektu
    - popř. pokud objekt již nemá kontext
* Neakceptuje další parametry
* Může přistupovat k atributům (problematické!)

! examples/OOP/employee_class_destructor1.py

* Volání konstruktoru může přijít "pozdě" - po ukončení skriptu

! examples/OOP/employee_class_destructor2.py

* Explicitní smazání konstruktoru konstrukcí `del`

! examples/OOP/explicit_del_call.py


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

! examples/OOP/employee_class_3.py

* Vylepšení formátování výstupu

! examples/OOP/employee_class_4.py

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

! examples/OOP/employee_class_5.py



### Speciální metoda `__eq__`

* Zavolána při porovnávání objektů

! examples/OOP/employee_class_6.py



### Třída komplexních čísel

* Základní reprezentace komplexního čísla

! examples/OOP/complex1.py

* Převod na řetězec

! examples/OOP/complex2.py

* Porovnání dvou komplexních čísel

! examples/OOP/complex3.py

* Součet komplexních čísel operátorem `+`

! examples/OOP/complex4.py

* Přičtení ke komplexnímu číslu operátorem `+=`

! examples/OOP/complex5.py

* Negace komplexního čísla

! examples/OOP/complex6.py



### Dědičnost

* Z jedné třídy lze odvodit třídu další
    - předek/potomek
    - superclass
* Nová třída zdědí vlastnosti z třídy předchozí
* Vybrané vlastnosti je možné modifikovat

* Třída `Person` a od ní odvozená třída `Student`

! examples/OOP/inheritance1.py

* Přetížení metody `__str__` ve třídě Student

! examples/OOP/inheritance2.py

* Volání konstruktoru nadtřídy

! examples/OOP/inheritance3.py

* Volání konstruktoru nadtřídy, rozlišení konstruktorů

! examples/OOP/inheritance4.py

* Další třída `Employee` odvozená od třídy `Person`

! examples/OOP/inheritance5.py



### Polymorfismus

* Ukázka polymorfismu

! examples/OOP/polymorphism1.py

* Třída jako rozhraní v Pythonu

! examples/OOP/polymorphism2.py



### Atributy třídy, třídní metody

* Předepsány přímo v deklaraci třídy
* Jsou sdíleny všemi instancemi této třídy!
* Přístup přes třídní metody
    - class method
* Parametr `cls` (jako class) nikoli `self`

* Atribut třídy a tečková notace

! examples/OOP/class_attribute.py

* Typický příklad použití - počitadlo instancí

! examples/OOP/class_method.py

* (bylo by vhodné upravit přetížením destruktoru)



### Statické metody

* Pouze funkce zapouzdřené do jmenného prostoru třídy
* Nemají přístup k žádným atributům
* I proto nemají parametr `self`

* Nekorektní příklad použití

! examples/OOP/static_method1.py

* Korektní příklad použití

! examples/OOP/static_method2.py



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

! examples/Functional/lambda1.py

* Lambda výraz bez parametrů

! examples/Functional/lambda2.py

* Někdy je zapotřebí parametr ignorovat
    - uvidíme při návrhu GUI u událostí (events)

! examples/Functional/lambda3.py



### First-class funkce

* Funkce jsou v Pythonu plnohodnotným datovým typem
    - akceptují se jako parametry jiných funkcí
    - lze je vracet jako návratové hodnoty jiných funkcí
    - lze je ukládat do n-tic, seznamů, slovníků...

* Funkce jako parametr jiné funkce

! examples/Functional/accept_function.py

* Funkce jako návratová hodnota jiné funkce

! examples/Functional/adder.py



### Uzávěry (closures)

* Funkce mající přístup k nelokální proměnné/hodnotě
    - "uzavírají" tuto hodnotu

! examples/Functional/closure.py

* Nutnost použití modifikátoru `nonlocal`

* Typický příklad - libovolné množství čítačů

! examples/Functional/counter.py

* (lze implementovat i s využitím generátorů)



### Generátorová notace seznamu

* List comprehension
    - možnost konstrukce n-tice nebo seznamu na jediném řádku bez `append`
    - lze kombinovat s podmínkou
    - existuje i varianta založená na generátorech

! examples/Functional/list_comprehension.py



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

! examples/Functional/map_function.py

    - popř. s pojmenovanou funkcí

! examples/Functional/map_function2.py

* Funkce `filter`
    - výběr hodnot ze sekvence na základě zadané podmínky

! examples/Functional/filter_function.py

* Funkce `reduce`
    - postupné zkracování vstupní sekvence akumulací mezivýsledku
    - musí být importována z balíčku `functools`

! examples/Functional/reduce_function.py

! examples/Functional/reduce_sum.py



### Zkrácené logické výrazy

* Druhý operand je vyhodnocen pouze v případě, že není dopředu známý výsledek výrazu
    - `x and y` - pokud `x==False`, není nutné vyhodnotit `y`
    - `x or y` - pokud `x==True`, není nutné vyhodnotit `y`

* Ukázka všech možných kombinací, které mohou nastat

! examples/Functional/short_circuit_1.py

! examples/Functional/short_circuit_2.py

! examples/Functional/short_circuit_3.py

! examples/Functional/short_circuit_4.py

! examples/Functional/short_circuit_5.py

! examples/Functional/short_circuit_6.py

! examples/Functional/short_circuit_7.py

! examples/Functional/short_circuit_8.py



--

## Pokročilé konstrukty jazyka Python

* Generátory a iterátory
* Dekorátory



### Generátory

* Běžná funkce, která vygeneruje seznam o zadané délce

! examples/generators/gen_list.py

* Generátor seznamu o zadané délce

! examples/generators/function_generator_1.py

* Generátor seznamu o nekonečné (neomezené) délce

! examples/generators/function_generator_2.py

* Generátor konečného seznamu implementovaný jako třída

! examples/generators/generator_class_1.py

* Generátor nekonečného seznamu implementovaný jako třída

! examples/generators/generator_class_2.py



### Dekorátory

* Funkce vracející jinou funkci
    - jedná se tedy o funkci vyššího řádu
    - ovšem s odlišnou formou zápisu, která je uživatelsky přívětivá
    - lze použít větší množství dekorátorů

! examples/decorators/return_function.py

* Přepis předchozího příkladu jako dekorátoru

! examples/decorators/decorator.py

* Užitečný dekorátor - měření času

! examples/decorators/measure_time.py



### Větší množství dekorátorů

* Bez dekorátorů

! examples/decorators/decorators1.py

* Jeden dekorátor
    
! examples/decorators/decorators2.py

* Dva dekorátory

! examples/decorators/decorators3.py


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

! examples/stdlib/cli_args.py

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

! examples/stdlib/json_output_1.py

* Zajištění lepší čitelnosti JSON výstupu

! examples/stdlib/json_output_2.py

* Přečtení datového souboru uloženého ve formátu JSON

! examples/stdlib/json_input.py

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
