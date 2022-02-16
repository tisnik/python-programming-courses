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

* "Name mangling" interních atributů

! examples/OOP/name_mangling.py



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

* Přidání metody `__repr__`

! examples/OOP/complex7.py



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

* Další příklady na polymorfismus

! examples/OOP/polymorphism3.py

! examples/OOP/polymorphism4.py



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

* Další příklady

! examples/Functional/clojure_lambda.py

! examples/Functional/closure3.py



### Generátorová notace seznamu

* List comprehension
    - možnost konstrukce n-tice nebo seznamu na jediném řádku bez `append`
    - lze kombinovat s podmínkou
    - existuje i varianta založená na generátorech

! examples/Functional/list_comprehension.py

* Proč generátorová notace seznamu?
    - ostatní způsoby jsou dlouhé
    - a nejsou idiomatické

! examples/Functional/list_comprehension_why.py

! examples/Functional/list_comprehension_why_2.py



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

* Výpočet faktoriálu s využitím `reduce`

! examples/Functional/factorial.py



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

* Generátorová notace...

! examples/generators/generator_comprehension1.py

! examples/generators/generator_comprehension2.py



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


### Od getterů a setterů k properties

! examples/OOP/employee_class_7.py

! examples/OOP/employee_class_8.py

! examples/OOP/employee_class_9.py



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

! examples/stdlib/file_write.py

! examples/stdlib/file_append.py

! examples/stdlib/ord_chr.py


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

! examples/stdlib/get_framebuffer_resolution.py

* Časově efektivnější řešení:

! examples/stdlib/get_framebuffer_resolution2.py

* Reálný příklad:

! examples/stdlib/regular_expression2.py

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

! examples/stdlib/strftime.py

! examples/stdlib/strptime.py



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

! examples/stdlib/arrays1.py

! examples/stdlib/arrays2.py

! examples/stdlib/arrays3.py

! examples/stdlib/arrays4.py



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

! examples/stdlib/queue_example.py

! examples/stdlib/simple_queue_example.py

! examples/stdlib/stack_example.py

! examples/stdlib/priority_queue_example.py

* Fronty jako komunikační médium mezi vlákny

! examples/stdlib/queues1.py

! examples/stdlib/queues2.py

! examples/stdlib/queues3.py

! examples/stdlib/queues4.py



### Modul `math`

* Matematické funkce

! examples/stdlib/math_sin_cos.py



### Modul `sys`

* Systémová volání resp. rozhraní pro ně

! examples/stdlib/bounds.py



### Modul `os`

* Funkce specifické pro různé operační systémy

! examples/stdlib/environ.py



### Modul `subprocess`

* Spuštění dalších procesů
* Zpracování vstupů a výstupů z těchto procesů

! examples/stdlib/get_framebuffer_resolution.py



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

! examples/stdlib/multithreading1.py

! examples/stdlib/multithreading2.py

* Dlouhodobé procesy (pro kontrolu, co se děje "uvnitř")

! examples/stdlib/multithreading3.py



### Komunikace mezi vlákny přes fronty

! examples/stdlib/queues1.py

! examples/stdlib/queues2.py

! examples/stdlib/queues3.py

! examples/stdlib/queues4.py


### Vlákna běžící na pozadí, čekání na dokončení vláken

! examples/stdlib/multithreading_no_join_no_deamon.py

! examples/stdlib/multithreading_no_join_deamon.py

! examples/stdlib/multithreading_join_deamon.py

! examples/stdlib/multithreading_timeout.py


### Balíček `concurrent.futures`

* Nový přístup k plánování práce "workerů"

! examples/stdlib/thread_pool_1.py

! examples/stdlib/thread_pool_2.py



### Balíček `multiprocessing`

! examples/stdlib/multiprocessing1.py

! examples/stdlib/multiprocessing2.py

! examples/stdlib/multiprocessing3.py

! examples/stdlib/multiprocessing4.py

! examples/stdlib/multiprocessing5.py



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

! examples/serialization/pickle_write.py

! examples/serialization/pickle_write_protocol.py

! examples/serialization/pickle_read.py



### Pickle - serializace a deserializace objektů

! examples/serialization/employee_class_pickle_write.py

! examples/serialization/employee_class_pickle_read.py



### Shelve

* Databáze hodnot/objektů

! examples/serialization/shelve_db_write.py

! examples/serialization/shelve_db_read.py



### Shelve - ukládání objektů do databáze

! examples/serialization/employee_class_shelve_write.py

! examples/serialization/employee_class_shelve_read.py


## Kafka

! examples/Kafka/producer1.py

! examples/Kafka/consumer1.py

! examples/Kafka/consumer2.py

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
1                   unittest
2                   doctest
3                   pytest
4                   nose
5                   testify
6                   Trial
7                   Twisted
8                   subunit
9                   testresources
10                  reahl.tofu
11                  unit testing
12                  testtools
13                  Sancho
14                  zope.testing
15                  pry
16                  pythoscope
17                  testlib
18                  pytest
19                  dutest
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

! examples/gui/tkinter.py



### appJar

* použití ve výuce
* nejrychlejší a současně i nejjednodušší způsob, jak v Pythonu vytvořit aplikaci s grafickým uživatelským rozhraním
* některé pokročilejší ovládací prvky nejsou k dispozici

! examples/gui/appjar.py



### PyGTK

* určena pro desktopová prostředí založená na GTK+, konkrétně ovšem na GTK+ 2.x
* dnes již zastaralé
* složitější práce v porovnání s Tkinterem a appJarem

! examples/gui/pygtk.py

! examples/gui/pygtk_no_events.py



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

! examples/gui/pyqt.py



### PySide

* podobné PyQt
* odlišné licencování
* dnes používanější

! examples/gui/pyside1.py

! examples/gui/pyside2.py



### wxPython

* zajišťuje rozhraní k populární GUI knihovně wxWidgets
* původně wxWindows -> wxWidgets
* multiplatformní aplikace

! examples/gui/wxpython.py



### Kivy

* ucelený framework určený především pro tvorbu aplikací pro mobilní platformy
* použití i na běžných desktopech
* akcelerace vykreslení prvků přes OpenGL ES 2
* pro deklaraci GUI použít speciální jazyk nazvaný K
    - hraje podobnou roli jako například QML (Qt Modeling Language)

! examples/gui/kivy.py



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

## Tkinter

* Výchozí GUI knihovna pro Python
* Založeno na TCL/Tk
* Základní koncepty
    - Widgety
    - Kontejnery
    - Správci umístění (geometrie) widget§
    - Události
    - Handlery událostí

### Widgety

```
Jméno widgetu     Význam a funkce
---------------------------------
label             widget, který zobrazuje v okně či dialogu měnitelný text
button            graficky zobrazené tlačítko, které implicitně reaguje na levé tlačítko myši
checkbutton       dvoustavový přepínač, který implicitně reaguje na levé tlačítko myši
radiobutton       widget, jichž může být sdruženo větší množství, vždy pouze jeden je vybraný
scale             dnes nazýván pojmem slider atd., jedná se o widget s posuvnou částí a přidruženým textem, kde se zobrazuje hodnota v závislosti na poloze posuvné části
entry             widget, do kterého je možné zapisovat text, k tomu má přidruženo mnoho klávesových zkratek (jde o kombinaci staršího a novějšího standardu)
spinbox           widget určený pro zadávání číselných hodnot kombinací klávesnice a myši (i s kontrolou mezí)
menu              vertikální menu, které se skládá z více položek
menubutton        používá se spolu s menu pro vytváření jednotlivých položek
listbox           widget, jež nabízí na výběr libovolné množství řádků s textem
scrollbar         podobné widgetu scale s tím rozdílem, že zobrazuje posuvné šipky a naopak nezobrazuje přidruženou číselnou hodnotu
frame             jeden z několika nabízených kontejnerů; tento má tvar obdélníka (může být také neviditelný nebo může mít 3D rámeček)
toplevel          další z kontejnerů, tento se chová jako samostatné okno či dialog
bitmap            bitmapa, tj. rastrový obrázek
photo/photoimage  rastrový obrázek, jež může být načten z externího souboru v mnoha různých formátech
canvas            widget, na který lze programově vkládat další grafické komponenty (úsečky, oblouky, kružnice, polyčáry, text atd.)
```

### Vlastnosti widgetů

```
Jméno vlastnosti   Popis vlastnosti
------------------------------------
background         barva pozadí widgetu v případě, že widget není aktivní (vybraný)
foreground         barva popředí widgetu (například zobrazeného textu) v případě, že widget není aktivní (vybraný)
borderwidth        šířka okraje widgetu, která je zadaná v pixelech
activebackground   barva pozadí widgetu v případě, že je widget vybrán (typicky kurzorem myši)
activeforeground   barva popředí widgetu v případě, že je widget vybrán
disabledforeground barva popředí widgetu v případě, že je ovládání widgetu zakázáno
relief             způsob prostorového zobrazení widgetu
compound           způsob umístění bitmapy či obrázku na widgetu
bitmap             bitmapa, která má být ve widgetu zobrazena
image              obrázek, který má být ve widgetu zobrazen (více o bitmapách a obrázcích bude uvedeno v dalších dílech)
font               jméno fontu, který je použit pro text uvnitř widgetu (font lze specifikovat platformově nezávislým způsobem)
text               text, který má být ve widgetu (tlačítko, položka menu atd.) zobrazen
cursor             jméno kurzoru myši, který bude použit v případě, že se kurzor nachází nad widgetem
textvariable       jméno proměnné, která je nastavována podle uživatelových manipulací s widgetem (StringVar v Tkinteru)
justify            zarovnání textu ve widgetu v případě, že se zobrazuje více řádků
anchor             způsob umístění textu či obrázku ve widgetu
```

### Témata

* clam
* alt
* default
* classic

### Dialogy

* `showinfo()`
* `showwarning()`
* `showerror()`
* `askokcancel()`
* `askretrycancel()`
* `askyesno()`
* `askquestion()`

```python
messagebox.showinfo("Title", "Text"))
 
messagebox.showwarning("Title", "Text"))
 
messagebox.showerror("Title", "Text"))
```

### Demonstrační příklady

! examples/tkinter/01_label.py

! examples/tkinter/02_button.py

! examples/tkinter/03_button_and_lambda.py

! examples/tkinter/04_buttons_in_regular_grid.py

! examples/tkinter/05_buttons_in_regular_grid_cmd.py

! examples/tkinter/06_buttons_and_pack_manager.py

! examples/tkinter/07_buttons_in_grid.py

! examples/tkinter/08_buttons_in_grid_cmd.py

! examples/tkinter/09_columnspan.py

! examples/tkinter/10_no_sticky_buttons.py

! examples/tkinter/11_sticky_buttons_west.py

! examples/tkinter/12_sticky_buttons_east.py

! examples/tkinter/13_sticky_buttons_west_east.py

! examples/tkinter/14_sticky_buttons_north_south.py

! examples/tkinter/15_button_styles.py

! examples/tkinter/16_ttk_styles.py

! examples/tkinter/17_themes.py

! examples/tkinter/18_theme_selection.py

! examples/tkinter/19_theme_settings_and_selection.py

! examples/tkinter/20_button_styles.py

! examples/tkinter/21_button_styles_2.py

! examples/tkinter/22_grid_padding.py

! examples/tkinter/23_border_width.py

! examples/tkinter/24_pack_manager.py

! examples/tkinter/25_checkbutton.py

! examples/tkinter/26_checkbutton_alt_theme.py

! examples/tkinter/27_checkbox_variable.py

! examples/tkinter/28_checkbox_specific_values.py

! examples/tkinter/29_entry.py

! examples/tkinter/30_entry_variable.py

! examples/tkinter/31_radio_button.py

! examples/tkinter/32_radio_button_align.py

! examples/tkinter/33_radio_button_default_value.py

! examples/tkinter/34_ttk_radio_button.py

! examples/tkinter/35_ttk_button_groups.py

! examples/tkinter/36_ttk_button_pack.py

! examples/tkinter/37_listbox.py

! examples/tkinter/38_listbox_bind.py

! examples/tkinter/39_listbox_scroll.py

! examples/tkinter/40_listbox_scroll_linked.py

! examples/tkinter/41_spinbox.py

! examples/tkinter/42_spinbox_values.py

! examples/tkinter/43_frame.py

! examples/tkinter/44_labelframe.py

! examples/tkinter/45_toplevel_menu.py

! examples/tkinter/46_toplevel_menu_other_gui.py

! examples/tkinter/47_popup_menu.py

! examples/tkinter/48_pulldown_menu.py

! examples/tkinter/49_pulldown_menu_no_tearoff.py

! examples/tkinter/50_pulldown_menu_no_tearoff.py

! examples/tkinter/51_menu_colors.py

! examples/tkinter/52_menu_keys.py

! examples/tkinter/53_menu_images.py

! examples/tkinter/54_menu_images2.py

! examples/tkinter/55_checkbuttons_in_menu.py

! examples/tkinter/56_radiobuttons_in_menu.py

! examples/tkinter/57_menu_accelerators.py

! examples/tkinter/58_bind_accelerators.py

! examples/tkinter/59_basic_canvas.py

! examples/tkinter/60_canvas_style.py

! examples/tkinter/67_objects_on_canvas.py

! examples/tkinter/98_tkdialog.py

! examples/tkinter/99_ask_dialogs.py

! examples/tkinter/animation.py

--

## Časté problémy

! examples/pitfalls/classes.py

! examples/pitfalls/default_argument_1.py

! examples/pitfalls/default_argument_2.py

! examples/pitfalls/scoping1.py

! examples/pitfalls/scoping2.py

! examples/pitfalls/scoping3.py

! examples/pitfalls/scoping4.py

! examples/pitfalls/closures.py

! examples/pitfalls/floats.py

! examples/pitfalls/mutating_list.py

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

