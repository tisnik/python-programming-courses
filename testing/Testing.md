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

* Jednotkové testy
* Testy komponent
* Systémové testy
* Akceptační testy
* Testy chování
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
### Testy uživatelského rozhraní
