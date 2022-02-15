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

```python
"""Výpočet průměru."""


def average(x):
    """Výpočet průměru ze seznamu hodnot předaných v parametru x."""
    return sum(x) / float(len(x))
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average01/average.py)

* Vlastní jednotkový test

```python
"""Implementace jednotkových testů."""

from average import average


def test_average_basic():
    """Otestování výpočtu průměru."""
    result = average([1, 2])
    assert result == 1.5
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average01/test_average.py)

* Spuštění jednotkových testů

```
pytest
```

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average01](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average01)



### Testování kódu obsahujícího chybu

* Schválně výpočet poškodíme

```python
"""Výpočet průměru."""


def average(x):
    """Výpočet průměru ze seznamu hodnot předaných v parametru x."""
    return sum(x) / float(1 + len(x))
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average02/average.py)

* Nové spuštění jednotkových testů

```
pytest
```

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average02](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average02)



### Další rozšíření a vylepšení testů

* Vylepšení konstrukce assert

```python
"""Implementace jednotkových testů."""

from average import average


def test_average_basic():
    """Otestování výpočtu průměru."""
    result = average([1, 2])
    expected = 1.5
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average03/test_average.py)

* Přidání dalšího testu pro mezní případ

```python
"""Implementace jednotkových testů."""

from average import average


def test_average_basic():
    """Otestování výpočtu průměru."""
    result = average([1, 2])
    expected = 1.5
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


def test_average_empty_list():
    """Otestování výpočtu průměru."""
    result = average([])
    expected = 0.0
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average04/test_average.py)

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average03](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average03)
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average04](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average04)



### Testy pro funkce, které mohou vyhodit výjimku

* Test, zda dochází k vyhození výjimky

```python
"""Implementace jednotkových testů."""

import pytest

from average import average


def test_average_basic():
    """Otestování výpočtu průměru."""
    result = average([1, 2])
    expected = 1.5
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


def test_average_empty_list():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        result = average([])


def test_average_exception_not_raised():
    """Otestování výpočtu průměru."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        result = average([1, 2])
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average05/test_average.py)

* Větší množství testovacích scénárů
    - nedoporučovaný způsob

```python
"""Implementace jednotkových testů."""

import pytest

from average import average


def test_average_basic_more_checks():
    """Otestování výpočtu průměru."""
    inputs = ((0, 0), (1, 0), (1, 1), (1, 2))
    expected_results = (0, 0.5, 1, 1.5)

    for input, expected in zip(inputs, expected_results):
        result = average(input)
        assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
            expected, result
        )
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average06/test_avegate_no_params.py)

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average06](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average06)



### Rozšíření testů o tabulky s daty

* Testovací data deklarovaná vně testu
    - doporučovaný způsob

```python
"""Implementace jednotkových testů."""

import pytest

from average import average


testdata = [
    ((1, 1), 1),
    ((1, 2), 1.5),
    ((0, 1), 0.5),
    ((1, 2, 3), 2.0),
    ((0, 10), 0.5),
]


@pytest.mark.parametrize("values,expected", testdata)
def test_average_basic(values, expected):
    """Otestování výpočtu průměru."""
    result = average(values)
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


def test_average_empty_list_1():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        result = average([])


def test_average_empty_list_2():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(Exception) as excinfo:
        result = average([])
    # poměrně křehký způsob testování!
    assert excinfo.type == ZeroDivisionError
    assert str(excinfo.value) == "float division by zero"
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average07/test_average.py)

* Explicitní identifikátory testů

```python
"""Implementace jednotkových testů."""

import pytest

from average import average


testdata = [
    ((1, 1), 1),
    ((1, 2), 1.5),
    ((0, 1), 0.5),
    ((1, 2, 3), 2.0),
    ((0, 10), 0.5),
]


@pytest.mark.parametrize(
    "values,expected", testdata, ids=["1,1", "1,2", "0,1", "1,2,3", "0,10"]
)
def test_average_basic_2(values, expected):
    """Otestování výpočtu průměru."""
    result = average(values)
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


def test_average_empty_list_1():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        result = average([])


def test_average_empty_list_2():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(Exception) as excinfo:
        result = average([])
    # poměrně křehký způsob testování!
    assert excinfo.type == ZeroDivisionError
    assert str(excinfo.value) == "float division by zero"
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average08/test_average.py)

* Další varianta zápisu
    - data přímo součástí dekorátoru

```python
"""Implementace jednotkových testů."""

import pytest

from average import average


@pytest.mark.parametrize(
    "values,expected",
    [
        pytest.param((1, 1), 1),
        pytest.param((1, 2), 1.5),
        pytest.param((0, 1), 0.5),
        pytest.param((1, 2, 3), 2.0),
        pytest.param((0, 10), 0.5),
    ],
)
def test_average_basic_3(values, expected):
    """Otestování výpočtu průměru."""
    result = average(values)
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


def test_average_empty_list_1():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        result = average([])


def test_average_empty_list_2():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(Exception) as excinfo:
        result = average([])
    # poměrně křehký způsob testování!
    assert excinfo.type == ZeroDivisionError
    assert str(excinfo.value) == "float division by zero"
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average09/test_average.py)

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average07](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average07)
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average08](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average08)
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average09](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average09)



### Spuštění pouze vybraných testů

* Označení testů (tagy)

```python
"""Implementace jednotkových testů."""

import pytest

from average import average


def pytest_configure(config):
    """Konfigurace jednotkových testů."""
    config.addinivalue_line(
        "markers", "smoketest: mark test that are performed very smoketest"
    )


testdata = [
    ((1, 1), 1),
    ((1, 2), 1.5),
    ((0, 1), 0.5),
    ((1, 2, 3), 2.0),
    ((0, 10), 0.5),
]


@pytest.mark.smoketest
@pytest.mark.parametrize("values,expected", testdata)
def test_average_basic_1(values, expected):
    """Otestování výpočtu průměru."""
    result = average(values)
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


@pytest.mark.smoketest
@pytest.mark.parametrize(
    "values,expected", testdata, ids=["1,1", "1,2", "0,1", "1,2,3", "0,10"]
)
def test_average_basic_2(values, expected):
    """Otestování výpočtu průměru."""
    result = average(values)
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


@pytest.mark.smoketest
@pytest.mark.parametrize(
    "values,expected",
    [
        pytest.param((1, 1), 1),
        pytest.param((1, 2), 1.5),
        pytest.param((0, 1), 0.5),
        pytest.param((1, 2, 3), 2.0),
        pytest.param((0, 10), 0.5),
        pytest.param((), 0),
    ],
)
def test_average_basic_3(values, expected):
    """Otestování výpočtu průměru."""
    result = average(values)
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


@pytest.mark.thorough
def test_average_empty_list_1():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        result = average([])


@pytest.mark.thorough
def test_average_empty_list_2():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(Exception) as excinfo:
        result = average([])
    # poměrně křehký způsob testování!
    assert excinfo.type == ZeroDivisionError
    assert str(excinfo.value) == "float division by zero"
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average11/test_average.py)

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

```python
"""Implementace jednotkových testů."""

import pytest

from average import average


def pytest_configure(config):
    """Konfigurace jednotkových testů."""
    config.addinivalue_line(
        "markers", "smoketest: mark test that are performed very smoketest"
    )


testdata = [
    ((1, 1), 1),
    ((1, 2), 1.5),
    ((0, 1), 0.5),
    ((1, 2, 3), 2.0),
    ((0, 10), 0.5),
]


@pytest.mark.smoketest
@pytest.mark.parametrize("values,expected", testdata)
def test_average_basic_1(values, expected):
    """Otestování výpočtu průměru."""
    result = average(values)
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


@pytest.mark.smoketest
@pytest.mark.parametrize(
    "values,expected", testdata, ids=["1,1", "1,2", "0,1", "1,2,3", "0,10"]
)
def test_average_basic_2(values, expected):
    """Otestování výpočtu průměru."""
    result = average(values)
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


@pytest.mark.smoketest
@pytest.mark.parametrize(
    "values,expected",
    [
        pytest.param((1, 1), 1),
        pytest.param((1, 2), 1.5),
        pytest.param((0, 1), 0.5),
        pytest.param((1, 2, 3), 2.0),
        pytest.param((0, 10), 0.5),
        pytest.param((), 0),
    ],
)
def test_average_basic_3(values, expected):
    """Otestování výpočtu průměru."""
    result = average(values)
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


@pytest.mark.thorough
def test_average_empty_list_1():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        result = average([])


@pytest.mark.thorough
def test_average_empty_list_2():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(Exception) as excinfo:
        result = average([])
    # poměrně křehký způsob testování!
    assert excinfo.type == ZeroDivisionError
    assert str(excinfo.value) == "float division by zero"


@pytest.fixture
def input_values():
    """Vygenerování vstupních hodnot pro jednotkový test."""
    return (1, 2, 3, 4, 5)


def test_average_five_values(input_values):
    """Otestování výpočtu průměru."""
    result = average(input_values)
    expected = 3
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average13/test_average.py)

* Adresář s celým projektem
    - [https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average13](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/average14)



### Složitější příklad - výpočet prvočísel

* Testovaný zdrojový kód

```python
"""Výpočet seznamu prvočísel až do zadaného limitu."""

# originální kód lze nalézt na adrese:
# http://www.rosettacode.org/wiki/Sieve_of_Eratosthenes#Odds-only_version_of_the_array_sieve_above


def primes2(limit):
    """Výpočet seznamu prvočísel až do zadaného limitu."""
    # okrajový případ
    if limit < 2:
        return []

    # druhý případ - 2 je speciálním prvočíslem
    if limit < 3:
        return [2]

    lmtbf = (limit - 3) // 2

    # naplnění tabulky, která se bude prosívat
    buf = [True] * (lmtbf + 1)

    # vlastní prosívání
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)

    # vytvoření seznamu prvočísel
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/primes1/primes.py)

* Vlastní jednotkový test

```python
"""Implementace jednotkových testů."""

from primes import primes2


def test_primes_10():
    """Otestování výpočtu seznamu prvočísel až do limitu 10."""
    # získat seznam prvočísel až do limitu 10
    p = primes2(10)
    # testy lze dále rozšiřovat
    assert 2 in p
    assert 10 not in p
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/primes1/test_primes.py)

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

```python
"""Implementace jednotkových testů."""

from primes import primes2


def test_primes_10():
    """Otestování výpočtu seznamu prvočísel až do limitu 10."""
    # získat seznam prvočísel až do limitu 10
    p = primes2(10)
    # testy lze dále rozšiřovat
    assert 2 in p
    assert 10 not in p


def test_primes_0():
    """Otestování výpočtu seznamu prvočísel do limitu 0."""
    p = primes2(0)
    # otestujeme, zda je sekvence prázdná (není zcela přesné)
    assert not p
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/primes2/test_primes.py)

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

```python
"""Výpočet seznamu prvočísel až do zadaného limitu."""

# originální kód lze nalézt na adrese:
# http://www.rosettacode.org/wiki/Sieve_of_Eratosthenes#Odds-only_version_of_the_array_sieve_above


def primes2(limit):
    """Výpočet seznamu prvočísel až do zadaného limitu."""
    # okrajový případ
    if limit < 2:  # pragma: no cover
        return []

    # druhý případ - 2 je speciálním prvočíslem
    if limit < 3:  # pragma: no cover
        return [2]

    lmtbf = (limit - 3) // 2

    # naplnění tabulky, která se bude prosívat
    buf = [True] * (lmtbf + 1)

    # vlastní prosívání
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)

    # vytvoření seznamu prvočísel
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/testing/examples/pytest/primes3/primes.py)

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
