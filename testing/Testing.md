# Jazyk Python - testování

* Pavel Tišnovský
    - `ptisnovs@redhat.com`
* Slajdy a demonstrační příklady:
    - `https://github.com/tisnik/python-programming-courses`

---



## Obsah kurzu

* Základní technologie testování
* Pyramida testů
* Zmrzlinový kornout jako antipattern
* Jednotkové testy
* Modul `pytest`
* Nástroj Hypothesis
* Fuzzy testy


--

# Testování

## Úvod

* Problematika testování stále složitějších aplikací a systémů
* CI/CD
* Základní problém
    - čím později je chyba odhalena, tím dražší je její oprava
    - z jiného oboru:
        - triviální úprava ventilu při návrhu motoru
        - vs svolávání aut do servisu
        - vs případné žaloby v případě, že chyba způsobí nehody
* Další časté problémy dnešních aplikací
    - velký vývojářský tým
    - používá se větší množství jazyků (jak se domluvit?)
    - zákazník a jeho role při vývoji
    - někdy nejasné role (vývojář či tester?)



## Základní technologie testování

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


## Pyramida typů testů

* Business část
    - Beta testy
    - Alfa testy
    - Akceptační testy
* Technologická část
    - UI testy
    - API testy
    - Integrační testy
    - Testy komponent
    - Unit testy
* Další typy testů
    - Benchmarky

---


## Pyramida typů testů

* Různé podoby testovací pyramidy

- [Pyramida #1](https://www.root.cz/obrazek/408774/)

- [Pyramida #2](https://www.root.cz/obrazek/408775/)

- [Pyramida #3](https://www.root.cz/obrazek/408776/)

- [Pyramida #4](https://www.root.cz/obrazek/408777/)



## Antipattern - zmrzlinový kornout

* Na první pohled může vypadat "logicky"
* Ovšem velmi pracné a časově náročné
    - navíc se UI může často měnit
    - (bikeshedding)

- [Kornout](https://www.root.cz/obrazek/408773/)



## Typy testů

* Jednotkové testy (unit tests)
* Testy komponent
* Systémové testy
* Akceptační testy
* Testy chování (BDD)
* Testy uživatelského rozhraní



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



### Systémové testy, akceptační testy

* Systémové testy se většinou rozdělují do dalších podkategorií
    - smoke testy (původ jména)
    - pouze velmi rychle zjišťují, zda je zajištěna alespoň minimální míra funkčnosti aplikace předtím, než se spustí složitější a časově mnohem náročnější testy
    - pokud smoke testy zhavarují, vrací se aplikace zpět k vývojářům a popř. k devops týmu

* Po úspěšném provedení smoke testů se mohou spouštět systémové testy
    - primárním účelem je ověření, jestli aplikace (služba) sestavená do jednoho celku pracuje korektně
    - tvorbou těchto testů již může být pověřen samostatný tým

* Testy akceptační jsou ještě zajímavější
    - na jejich vytváření se může podílet i zákazník



### Testy chování

* (BDD: behavior-driven development)

* Na pomezí mezi
    - integračními testy
    - API testy
    - akceptačními testy

* Popis očekávaného chování systému z pohledu zákazníka/uživatele
    - samotný systém je z pohledu BDD většinou černá skříňka

* Lze použít pro backend i pro frontend
    - na systém se pohlíží jako na černou skříňku

* Testovací scénáře může psát i poučený zákazník
    - specializovaný jazyk Gherkin

* Mají i dokumentační funkci
    - poměrně mnoho systémů popsaných právě pomocí BDD



### Testy uživatelského rozhraní

* Na jednu stranu nejjednodušší na pochopení
    - zákazníkem
    - vedením projektu

* Ovšem chování UI se velmi často mění
    - zastaralé testy
    - testy testující něco jiného, než vidí uživatel
    - mnohdy se situace řeší "zakomentováním" testů

* Skutečné UI testy simulující práci uživatele
    - nástroje umožňující "záznam" práce uživatele

* Testy na úrovni webové stránky (manipulace s DOM)
    - Selenium



## Praktická část



### Jednotkové testy

* Nástroj Pytest



### Pytest

* Základní operace
    - samotné spouštění jednotkových testů
    - vyhodnocení výsledků jednotkových testů
    - zjištění pokrytí zdrojového kódu testy
    - spouštění benchmarků
* Další vlastnosti
    - označení testů
    - tabulky s daty
    - tzv. fixtures
* Doplňkové moduly
    - https://docs.pytest.org/en/latest/reference/plugin_list.html



### Instalace

* https://docs.pytest.org/en/6.2.x/getting-started.html



### Pokrytí kódu jednotkovými testy

### Mocking

* "Falešný" blok kódu je možné rozdělit do několika kategorií:
   - fake – vrací jedinou programátorem zvolenou hodnotu. Příkladem funkce nahrazující čtení z databáze, která vždy vrátí jediný záznam.
   - stub – již obsahuje jednoduchou logiku, například dokáže reagovat na špatný vstup podobně, jako nahrazovaný blok.
   - spy – dokáže zaznamenat předávané parametry či dokonce celý stav (nebo podstav) aplikace.
   - mock – mnohdy se jedná o blok s vlastnostmi, které se přibližují reálnému (nahrazovanému) kódu. Vylepšená verze stub.


```
# 	Nástroj
1 	Ludibrio
2 	Python Mock
3 	PyMock
4 	mock
5 	pMock
6 	minimock
7 	svnmock
8 	Mocker
9 	Stubble
10 	Mox
11 	MockTest
12 	Fudge
13 	Mockito for Python
14 	CaptureMock
15 	flexmock
16 	doublex
17
```


### Příklad - výpočet průměru

* Testovaný zdrojový kód

! examples/pytest/average01/average.py

* Vlastní jednotkový test

! examples/pytest/average01/test_average.py

* Spuštění jednotkových testů

```
pytest
```

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average01](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average01)



### Testování kódu obsahujícího chybu

* Schválně výpočet poškodíme

! examples/pytest/average02/average.py

* Nové spuštění jednotkových testů

```
pytest
```

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average02](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average02)



### Další rozšíření a vylepšení testů

* Vylepšení konstrukce assert

! examples/pytest/average03/test_average.py

* Přidání dalšího testu pro mezní případ

! examples/pytest/average04/test_average.py

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average03](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average03)
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average04](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average04)



### Testy pro funkce, které mohou vyhodit výjimku

* Test, zda dochází k vyhození výjimky

! examples/pytest/average05/test_average.py

* Větší množství testovacích scénárů
    - nedoporučovaný způsob

! examples/pytest/average06/test_avegate_no_params.py

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average06](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average06)



### Rozšíření testů o tabulky s daty

* Testovací data deklarovaná vně testu
    - doporučovaný způsob

! examples/pytest/average07/test_average.py

* Explicitní identifikátory testů

! examples/pytest/average08/test_average.py

* Další varianta zápisu
    - data přímo součástí dekorátoru

! examples/pytest/average09/test_average.py

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average07](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average07)
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average08](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average08)
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average09](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average09)



### Spuštění pouze vybraných testů

* Označení testů (tagy)

! examples/pytest/average11/test_average.py

* Spuštění testů podle tagů

```
pytest -v -m smoketest
pytest -v -m thorough
pytest -v -m other
```

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average11](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average11)



### Fixtures

* Využití "fixtures"

! examples/pytest/average13/test_average.py

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average13](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average14)



### Složitější příklad - výpočet prvočísel

* Testovaný zdrojový kód

! examples/pytest/primes1/primes.py

* Vlastní jednotkový test

! examples/pytest/primes1/test_primes.py

* Spuštění jednotkových testů

```
pytest
```

```
pytest -v
```

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/primes1](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/primes1)



* Rozšíření testů o mezní případ

! examples/pytest/primes2/test_primes.py

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/primes2](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/primes2)



### Zjištění pokrytí kódu testy

```
pytest --cov=. > cov_all.txt

# specifikace balíčku
pytest --cov=primes > cov_primes.txt

# řádky nepokryté jednotkovými testy
pytest --cov=primes --cov-report term-missing > cov_missing.txt

# export do HTML
pytest --cov=primes --cov-report html
```

### Pragma no cover

! examples/pytest/primes3/primes.py

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/primes3](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/primes3)



### Benchmarky

### BDD: behavior-driven development

### Jazyk Gherkin

* Založen na použití několika klíčových slov a běžných vět
* V určitém ohledu podobný způsob zápisu jako v Pythonu
    - odsazení
    - klíčová slova, nikoli speciální znaky
* Existuje i možnost překladu klíčových slov do jiných jazyků
* Není pevně spojen s žádným konkrétním programovacím jazykem
* Výsledek: mohou ho používat i neprogramátoři

---

### Ukázka jednoduchého testovacího scénáře

```gherkin
Given the customer has logged into their current account
  And the balance is shown to be 100 euros
 When the customer transfers 75 euros to their savings account
 Then the new current account balance should be 25 euros
```

Části testovacího scénáře:

* Klíčová slova Given, And, When, Then
* Následuje část věty v libovolném jazyce (praktická je angličtina)
* Ve větě se mohou objevovat proměnné části: 100, 75, 25

---

### Víceřádkový text

```gherkin
Feature: Count words function test

  Scenario: Check the function count_words()
    Given a sample text
       """
       Velmi kratka veta.
       """
    When I count all words in text
    Then I should get 3 as a result

  Scenario: Check the function count_words()
    Given a sample text
       """
       Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
       eiusmod tempor incididunt ut labore et dolore magna aliqua.
       """
    When I count all words in text
    Then I should get 19 as a result
```

---

### Tabulky

```gherkin
Feature: Sum function test 1

  Scenario: Check the function sum()
    Given a list of integers
      |value |
      | 1    |
      | 10   |
      | 100  |
      | 1000 |
    When I summarize all those integers
    Then I should get 1111 as a result
```

---

### Tabulky (druhý příklad)

```
  Scenario: Check the exchange rate calculation
    Given the following exchange rate table
      | currency |  rate  |
      | CZK      |  1.000 |
      | CAD      | 16.172 |
      | HRK      |  3.407 |
      | USD      | 20.655 |
    When I sell 10 CAD
    Then I should receive 161.72 CZK
```

### Tabulky použité pro specifikaci několika běhů testů

```gherkin
  Scenario Outline: Check the user search feature, perform the search for more users
    Given GitHub is accessible
    When I search for user with nick <nick>
    Then I should receive 200 status code
     And I should receive proper JSON response
     And I should find the user with full name <fullname>
     And I should find that the user works for company <company>

     Examples: users
     |nick|fullname|company|
     |torvalds|Linus Torvalds|Linux Foundation|
     |brammool|Bram Moolenaar|Zimbu Labs|
     |tisnik|Pavel Tišnovský|Red Hat, Inc.|
```

### Tabulky použité pro specifikaci několika běhů testů

```gherkin
  Scenario Outline: Check the exchange rate calculation
    Given the following exchange rate table
      | currency |  rate  |
      | CZK      |  1.000 |
      | CAD      | 16.172 |
      | HRK      |  3.407 |
      | USD      | 20.655 |
    When I sell <sold> <currency>
    Then I should receive <amount> CZK

    Examples: sold
        | sold | currency | amount |
        | 1    |   CZK    |    1.000 |
        | 10   |   CZK    |   10.000 |
        | 1    |   CAD    |   16.172 |
        | 100  |   CAD    | 1617.200 |
        | 2    |   HRK    |    6.814 |
```

---

## Praktická část

* Knihovna Behave
* Struktura projektu s BDD testy
    - testovaný modul
    - testovací scénář
    - implementace testovacího scénáře
    - specifikace prostředí testů

---

### Repositář s demonstračními příklady

* https://github.com/tisnik/python-behave-demos

```
git clone https://github.com/tisnik/python-behave-demos
```

---

### Knihovna Behave

* Knihovna Behave
    - určena pro Python 2.x i Python 3.x
    - implementuje většinu funkcionality jazyka Gherkin
    - snadné napojení popisu testů na jejich implementaci
    - používají se dekorátory
    - automatické odvození parametrů z textu dekorátoru

---

### Struktura projektu s BDD testy

```
├── feature_list.txt
├── features
│   ├── adder.feature
│   └── steps
│       └── common.py
├── requirements.in
├── requirements.txt
├── run_tests.sh
└── src
    └── adder.py
```

Význam souborů v projektu:

```
src/adder.py                     vlastní modul, který budeme chtít otestovat
requirements.in/requirements.txt soubory pro pip (instalátor balíčků)
feature_list.txt                 seznam testovacích scénářů, které se mají spustit
features/                        adresář obsahující testovací scénáře i implementaci jednotlivých kroků testů
run_tests.sh	                 pomocný skript pro spuštění testovacích scénářů
```

---

### Testovaný modul

```python
def add(x, y):
    return x + y
```

---

### Popis testovacího scénáře

```gherkin
Feature: Adder test
 
  Scenario: Check the function add()
    Given The function add is callable
    When I call function add with arguments 1 and 2
    Then I should get 3 as a result
```

---

### Implementace jednotlivých kroků testu

* Povšimněte si použití argumentu *context*.

```python
from behave import given, then, when
from src.adder import add
 
 
@given('The function {function_name} is callable')
def initial_state(context, function_name):
    pass
 
 
@when('I call function {function} with arguments {x:d} and {y:d}')
def call_add(context, function, x, y):
    context.result = add(x, y)
 
 
@then('I should get {expected:d} as a result')
def check_integer_result(context, expected):
    assert context.result == expected, \
        "Wrong result: {r} != {e}".format(r=context.result, e=expected)
```

---

### Prostředí testů

* Příklad implementace prostředí ve chvíli, kdy se testuje nativní knihovna

```
from behave.log_capture import capture
import ctypes


def _load_library(context, library_name):
    if context.tested_library is None:
        context.tested_library = ctypes.CDLL(library_name)


def before_all(context):
    """Perform setup before the first event."""
    context.tested_library = None
    context.load_library = _load_library
```

---

### Skript pro spuštění testů

```shell
#!/bin/bash -ex
 
export NOVENV=1
function prepare_venv() {
    virtualenv -p python3 venv && source venv/bin/activate && python3 `which pip3` install -r requirements.txt
}
 
[ "$NOVENV" == "1" ] || prepare_venv || exit 1
 
PYTHONDONTWRITEBYTECODE=1 python3 `which behave` --tags=-skip -D dump_errors=true @feature_list.txt $@
```

---

### Vlastní spuštění textu

```
Feature: Adder test # features/adder.feature:1

  Scenario: Check the function add()                # features/adder.feature:3
    Given The function add is callable              # features/steps/common.py:20 0.000s
    When I call function add with arguments 1 and 2 # features/steps/common.py:25 0.000s
    Then I should get 3 as a result                 # features/steps/common.py:30 0.000s

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.000s
```

---

### Testování nativních funkcí/knihoven

* Použití knihovny *ctypes*

#### Testovací scénář

```gherkin
  @smoketest
  Scenario: Check the function int add(int, int)
    Given The library libadder.so is loaded
    When I call native function add with arguments 1 and 2
    Then I should get 3 as a result

  Scenario Outline: Thorough checking function int add(int, int)
    Given The library libadder.so is loaded
    When I call native function add with arguments <x> and <y>
    Then I should get <result> as a result

     Examples: results
     |x|y|result|
     # basic arithmetic
     |          0| 0|          0|
     |          1| 2|          3|
     |          1|-2|         -1|
     # no overflows at 16 bit limits
     |      32767| 1|      32768|
     |      65535| 1|      65536|
     # integer overflow
     | 2147483648| 1|-2147483647|
     |-2147483647|-1|-2147483648|
     |-2147483648|-1| 2147483647|
```

#### Prostředí testů

```python
from behave.log_capture import capture
import ctypes


def _load_library(context, library_name):
    if context.tested_library is None:
        context.tested_library = ctypes.CDLL(library_name)


def before_all(context):
    """Perform setup before the first event."""
    context.tested_library = None
    context.load_library = _load_library
```

#### Implementace kroků testu

```python
from behave import given, then, when


@given('The library {library_name} is loaded')
def initial_state(context, library_name):
    context.load_library(context, library_name)


@when('I call native function add with arguments {x:d} and {y:d}')
def call_add(context, x, y):
    context.result = context.tested_library.add(x, y)


@then('I should get {result:d} as a result')
def check_integer_result(context, result):
    assert context.result == result, "Expected result: {e}, returned value: {r}".format(e=result, r=context.result)
```

---

### Testování REST API

* Použití knihovny *requests*

#### Testovací scénář

```
  @smoketest
  Scenario: Check the GitHub API entry point
    Given GitHub is accessible
    When I access the API endpoint /
    Then I should receive 200 status code

  Scenario: Check the user search feature
    Given GitHub is accessible
    When I search for user with nick torvalds
    Then I should receive 200 status code
     And I should receive proper JSON response
     And I should find the user with full name Linus Torvalds
     And I should find that the user works for company Linux Foundation
```

#### Prostředí testů

```python
import json
import os.path

from behave.log_capture import capture
import requests


def _is_accessible(context, accepted_codes=None):
    accepted_codes = accepted_codes or {200, 401}
    url = context.api_url
    try:
        res = requests.get(url)
        return res.status_code in accepted_codes
    except requests.exceptions.ConnectionError as e:
        print("Connection error: {e}".format(e=e))
    return False


def before_all(context):
    """Perform setup before the first event."""
    context.is_accessible = _is_accessible
    context.api_url = "https://api.github.com"


@capture
def before_scenario(context, scenario):
    """Perform setup before each scenario is run."""
    pass


@capture
def after_scenario(context, scenario):
    """Perform cleanup after each scenario is run."""
    pass


@capture
def after_all(context):
    """Perform cleanup after the last event."""
    pass
```
---

## Robot framework

## Hypothesis

## Odkazy

* Použití Pythonu pro tvorbu testů: od jednotkových testů až po testy UI
    - [https://www.root.cz/clanky/pouziti-pythonu-pro-tvorbu-testu-od-jednotkovych-testu-az-po-testy-ui/](https://www.root.cz/clanky/pouziti-pythonu-pro-tvorbu-testu-od-jednotkovych-testu-az-po-testy-ui/)

* Použití Pythonu pro tvorbu testů: použití třídy Mock z knihovny unittest.mock
    - [https://www.root.cz/clanky/pouziti-pythonu-pro-tvorbu-testu-pouziti-tridy-mock-z-knihovny-unittest-mock/](https://www.root.cz/clanky/pouziti-pythonu-pro-tvorbu-testu-pouziti-tridy-mock-z-knihovny-unittest-mock/)

* Použití nástroje pytest pro tvorbu jednotkových testů a benchmarků
    - [https://www.root.cz/clanky/pouziti-nastroje-pytest-pro-tvorbu-jednotkovych-testu-a-benchmarku/](https://www.root.cz/clanky/pouziti-nastroje-pytest-pro-tvorbu-jednotkovych-testu-a-benchmarku/)

* Nástroj pytest a jednotkové testy: fixtures, výjimky, parametrizace testů
    - [https://www.root.cz/clanky/nastroj-pytest-a-jednotkove-testy-fixtures-vyjimky-parametrizace-testu/](https://www.root.cz/clanky/nastroj-pytest-a-jednotkove-testy-fixtures-vyjimky-parametrizace-testu/)

* Nástroj pytest a jednotkové testy: životní cyklus testů, užitečné tipy a triky
    - [https://www.root.cz/clanky/nastroj-pytest-a-jednotkove-testy-zivotni-cyklus-testu-uzitecne-tipy-a-triky/](https://www.root.cz/clanky/nastroj-pytest-a-jednotkove-testy-zivotni-cyklus-testu-uzitecne-tipy-a-triky/)

* Struktura projektů s jednotkovými testy, využití Travis CI
    - [https://www.root.cz/clanky/struktura-projektu-s-jednotkovymi-testy-vyuziti-travis-ci/](https://www.root.cz/clanky/struktura-projektu-s-jednotkovymi-testy-vyuziti-travis-ci/)

* Omezení stavového prostoru testovaných funkcí a metod
    - [https://www.root.cz/clanky/omezeni-stavoveho-prostoru-testovanych-funkci-a-metod/](https://www.root.cz/clanky/omezeni-stavoveho-prostoru-testovanych-funkci-a-metod/)

* Testování aplikací s využitím nástroje Hypothesis
    - [https://www.root.cz/clanky/testovani-aplikaci-s-vyuzitim-nastroje-hypothesis/](https://www.root.cz/clanky/testovani-aplikaci-s-vyuzitim-nastroje-hypothesis/)

* Testování aplikací s využitím nástroje Hypothesis (dokončení)
    - [https://www.root.cz/clanky/testovani-aplikaci-s-vyuzitim-nastroje-hypothesis-dokonceni/](https://www.root.cz/clanky/testovani-aplikaci-s-vyuzitim-nastroje-hypothesis-dokonceni/)

* Testování webových aplikací s REST API z Pythonu
    - [https://www.root.cz/clanky/testovani-webovych-aplikaci-s-rest-api-z-pythonu/](https://www.root.cz/clanky/testovani-webovych-aplikaci-s-rest-api-z-pythonu/)

* Testování webových aplikací s REST API z Pythonu (2)
    - [https://www.root.cz/clanky/testovani-webovych-aplikaci-s-rest-api-z-pythonu-2/](https://www.root.cz/clanky/testovani-webovych-aplikaci-s-rest-api-z-pythonu-2/)

* Behavior-driven development v Pythonu s využitím knihovny Behave
    - [https://www.root.cz/clanky/behavior-driven-development-v-pythonu-s-vyuzitim-knihovny-behave/](https://www.root.cz/clanky/behavior-driven-development-v-pythonu-s-vyuzitim-knihovny-behave/)

* Behavior-driven development v Pythonu s využitím knihovny Behave (druhá část)
    - [https://www.root.cz/clanky/behavior-driven-development-v-pythonu-s-vyuzitim-knihovny-behave-druha-cast/](https://www.root.cz/clanky/behavior-driven-development-v-pythonu-s-vyuzitim-knihovny-behave-druha-cast/)

* Behavior-driven development v Pythonu s využitím knihovny Behave (závěrečná část)
    - [https://www.root.cz/clanky/behavior-driven-development-v-pythonu-s-vyuzitim-knihovny-behave-zaverecna-cast/](https://www.root.cz/clanky/behavior-driven-development-v-pythonu-s-vyuzitim-knihovny-behave-zaverecna-cast/)

* Validace datových struktur v Pythonu pomocí knihoven Schemagic a Schema
    - [https://www.root.cz/clanky/validace-datovych-struktur-v-pythonu-pomoci-knihoven-schemagic-a-schema/](https://www.root.cz/clanky/validace-datovych-struktur-v-pythonu-pomoci-knihoven-schemagic-a-schema/)

* Validace datových struktur v Pythonu (2. část)
    - [https://www.root.cz/clanky/validace-datovych-struktur-v-pythonu-2-cast/](https://www.root.cz/clanky/validace-datovych-struktur-v-pythonu-2-cast/)

* Validace datových struktur v Pythonu (dokončení)
    - [https://www.root.cz/clanky/validace-datovych-struktur-v-pythonu-dokonceni/](https://www.root.cz/clanky/validace-datovych-struktur-v-pythonu-dokonceni/)

* Univerzální testovací nástroj Robot Framework
    - [https://www.root.cz/clanky/univerzalni-testovaci-nastroj-robot-framework/](https://www.root.cz/clanky/univerzalni-testovaci-nastroj-robot-framework/)

* Univerzální testovací nástroj Robot Framework a BDD testy
    - [https://www.root.cz/clanky/univerzalni-testovaci-nastroj-robot-framework-a-bdd-testy/](https://www.root.cz/clanky/univerzalni-testovaci-nastroj-robot-framework-a-bdd-testy/)

* Úvod do problematiky fuzzingu a fuzz testování
    - [https://www.root.cz/clanky/uvod-do-problematiky-fuzzingu-a-fuzz-testovani/](https://www.root.cz/clanky/uvod-do-problematiky-fuzzingu-a-fuzz-testovani/)

* Úvod do problematiky fuzzingu a fuzz testování – složení vlastního fuzzeru
    - [https://www.root.cz/clanky/uvod-do-problematiky-fuzzingu-a-fuzz-testovani-slozeni-vlastniho-fuzzeru/](https://www.root.cz/clanky/uvod-do-problematiky-fuzzingu-a-fuzz-testovani-slozeni-vlastniho-fuzzeru/)
