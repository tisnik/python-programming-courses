# Knihovna Pandas

![pandas_logo.png](pandas_logo.png)

### Autor Pavel Tišnovský, Red Hat
### Email ptisnovs@redhat.com



## Obsah kurzu

* Možnosti poskytované knihovnou Pandas
* Základy práce s datovými rámci
* Zobrazení obsahu datových rámců, vykreslení grafů a validace dat
* Práce s datovými řadami (series)
* Spojování datových rámců s využitím append, concat, merge a join
* Použití metody groupby, naformátování a export tabulek pro tisk
* Práce se seskupenými záznamy, vytvoření multiindexů
* Odkazy na další informační zdroje



## Možnosti poskytované knihovnou Pandas

* Načtení dat z různých datových zdrojů do datových rámců
    - CSV
    - TSV
    - databáze
    - tabulkové procesory
* Programová konstrukce datových rámců
* Prohlížení obsahu datových rámců
* Iterace nad daty, řazení a další podobné operace
* Spojování, seskupování a změna tvaru dat
* Práce s takzvanými sériemi
    - většinou získanými z datových rámců
* Vykreslování grafů z údajů získaných z datových rámců



## Základy práce s datovými rámci

* Knihovna Pandas podporuje využití různých datových zdrojů, především pak:
  - Souborů CSV (Comma-Separated Values)
  - Souborů TSV (Tab-Separated Values)
  - Textových souborů s volitelným oddělovačem a formátem sloupců
  - Tabulek z tabulkových procesorů (xls, xlsx, xlsm, xlsb, odf, ods, odt)
  - Souborů JSON se strukturovanými daty
  - Načítání z relačních databází s využitím SQL driverů
  - Načítání z Parquet souborů
  - atd.

### Načtení obsahu jednoduché tabulky ze souboru typu CSV

* CSV neboli Comma-Separated Values
* Obecně problematické
  - Anglický/český Excel
  - Víceřádkové buňky
  - Hlavičky sloupců

* Vstupní soubor s daty

```
Block size,Time to read
1,672512695
2,338152789
3,280886198
4,261732244
5,241726381
6,222869657
7,214296698
8,202491102
9,182263641
10,177141401
```

* Import dat

```python
import pandas
 
df = pandas.read_csv("integer_values.csv")
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

### Zpracování prázdných hodnot v tabulce

* Upravený vstupní soubor s daty

```
Block size,Time to read
1,672512695
2,338152789
3,280886198
4,261732244
5,
6,222869657
7,214296698
8,202491102
9,182263641
10,177141401
```

* Načtení bez specifikace formátu
- Knihovna Pandas musí nějakým způsobem reprezentovat chybějící hodnotu
- pro tento účel lze (mj.) použít i datový typ `float64` neboli `double`

```python
import pandas
 
df = pandas.read_csv("missing_integer_values.csv")
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

### Hodnota `NA`

```python
import pandas
 
df = pandas.read_csv("missing_integer_values.csv", dtype={"Time to read": "Int64"})
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

### Načtení tabulky obsahující časová razítka

```
n,Timestamp
1,2020-01-15 03:59:47
2,2020-01-15 08:19:25
3,2020-01-15 11:42:07
4,2020-01-15 14:58:48
5,2020-01-15 18:21:56
6,2020-01-15 21:10:01
7,2020-01-15 23:13:58
8,2020-01-16 01:51:52
9,2020-01-16 05:55:55
10,2020-01-16 10:11:54
11,2020-01-16 14:02:32
12,2020-01-16 17:35:25
13,2020-01-16 19:35:43
14,2020-01-16 22:29:24
```

* Prozatím při načtení nebudeme žádným způsobem specifikovat typy sloupců

```python
import pandas
 
df = pandas.read_csv("timestamps.csv")
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

### Korektní parsing časových razítek

* Nutnost specifikace sloupce, který obsahuje časová razítka

```python
import pandas
 
df = pandas.read_csv("timestamps.csv", parse_dates=["Timestamp"])
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

### Problematika vlastního či specifického formátu data a/nebo času

```
n,Timestamp
1,2020/01/15 03-59-47
2,2020/01/15 08-19-25
3,2020/01/15 11-42-07
4,2020/01/15 14-58-48
5,2020/01/15 18-21-56
6,2020/01/15 21-10-01
7,2020/01/15 23-13-58
8,2020/01/16 01-51-52
9,2020/01/16 05-55-55
10,2020/01/16 10-11-54
11,2020/01/16 14-02-32
12,2020/01/16 17-35-25
13,2020/01/16 19-35-43
14,2020/01/16 22-29-24
```

* Výsledek ovšem v tomto případě nedopadne nejlépe
* Pandas se sice pokusí o rozpoznání časových údajů (což jsme ostatně vyžadovali)
* Ovšem specifický formát nedokáže správně rozkódovat

```python
import pandas
 
df = pandas.read_csv("custom_timestamps.csv", parse_dates=["Timestamp"])
 
pandas.to_datetime(df.Timestamp)
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

### Vlastní parsovací funkce

* `datetime_parser`

```python
import pandas
import datetime
 
 
def datetime_parser(raw_data):
    return datetime.datetime.strptime(raw_data, "%Y/%m/%d %H-%M-%S")
 
 
df = pandas.read_csv("custom_timestamps.csv",
                     date_parser=datetime_parser,
                     parse_dates=["Timestamp"])
 
 
pandas.to_datetime(df.Timestamp)
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

### Dtto, ale s lambda výrazem

* Neboli s anonymní funkcí

```python
import pandas
import datetime
 
 
df = pandas.read_csv("custom_timestamps.csv",
                     date_parser=lambda raw_data: datetime.datetime.strptime(raw_data, "%Y/%m/%d %H-%M-%S"),
                     parse_dates=["Timestamp"])
 
 
pandas.to_datetime(df.Timestamp)
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

### Čtení tabulky uložené ve formátu TSV

* TSV neboli Tab-Separated Values
* Je velmi podobným formátem jako CSV
* Ovšem s tím rozdílem, že oddělovačem jednotlivých buněk je znak tabulátoru
  - tím současně odpadají mnohé problémy CSV
* Podobně jako v případě CSV i zde možnost ukládat na první řádek souboru hlavičku

```
Sep 2020        Sep 2019        Change  Language        Ratings Changep
1       2       change  C       15.95   +0.74
2       1       change  Java    13.48   -3.18
3       3               Python  10.47   +0.59
4       4               C++     7.11    +1.48
5       5               C#      4.58    +1.18
6       6               Visual Basic    4.12    +0.83
7       7               JavaScript      2.54    +0.41
8       9       change  PHP     2.49    +0.62
9       19      change  R       2.37    +1.33
10      8       change  SQL     1.76    -0.19
11      14      change  Go      1.46    +0.24
12      16      change  Swift   1.38    +0.28
13      20      change  Perl    1.30    +0.26
14      12      change  Assembly language       1.30    -0.08
15      15              Ruby    1.24    +0.03
16      18      change  MATLAB  1.10    +0.04
17      11      change  Groovy  0.99    -0.52
18      33      change  Rust    0.92    +0.55
19      10      change  Objective-C     0.85    -0.99
20      24      change  Dart    0.77    +0.13
```

### Nerozpoznání formátu

* Při běžném použití importní funkce `pandas.read_csv` není tento formát správně rozpoznán

```python
import pandas
 
df = pandas.read_csv("tiobe.tsv")
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

### Specifikace oddělovače sloupců

* Soubory TSV lze načíst tak, že nepovinným (pojmenovaným) parametrem `sep` specifikujeme oddělovač mezi záznamy
* V tomto případě se jedná o znak „\t“
    - Python používá céčkovský způsob zápisu řídicích znaků

```python
import pandas
 
# separator/delimiter specification
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

### Import dat z textových souborů

* Existuje i mnoho aplikací, v nichž jsou tabulková data uložena ve formě běžných textových souborů
   - s nějakými oddělovači odlišnými od výše zmíněného tabulátoru
   - relativně často se jedná o středníky, dvojtečky nebo o znak |
* Buď se jedná o zobecnění formátů CSV a TSV
* Nebo může mít textový soubor podobu naformátovaných sloupců s pevnou délkou
   - a tedy bez problémů čitelných uživatelem

```
Sep 2020            Sep 2019            Change              Language            Ratings             Changep
1                   2                   change              C                   15.95               +0.74
2                   1                   change              Java                13.48               -3.18
3                   3                                       Python              10.47               +0.59
4                   4                                       C++                 7.11                +1.48
5                   5                                       C#                  4.58                +1.18
6                   6                                       Visual Basic        4.12                +0.83
7                   7                                       JavaScript          2.54                +0.41
8                   9                   change              PHP                 2.49                +0.62
9                   19                  change              R                   2.37                +1.33
10                  8                   change              SQL                 1.76                -0.19
11                  14                  change              Go                  1.46                +0.24
12                  16                  change              Swift               1.38                +0.28
13                  20                  change              Perl                1.30                +0.26
14                  12                  change              Assembly language   1.30                -0.08
15                  15                                      Ruby                1.24                +0.03
16                  18                  change              MATLAB              1.10                +0.04
17                  11                  change              Groovy              0.99                -0.52
18                  33                  change              Rust                0.92                +0.55
19                  10                  change              Objective-C         0.85                -0.99
20                  24                  change              Dart                0.77                +0.13
```

### Problém - sloupce s mezerami

* Výsledek ovšem není zcela dokonalý, protože u sloupců, jejichž jména obsahují
  mezery, došlo k rozdělení na dva sloupce a tím pádem nám vznikly dvě série
  hodnot `NaN`

```python
import pandas
 
# separator/delimiter specification not needed there
df = pandas.read_fwf("tiobe.txt")
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

### Explicitní specifikace šířky sloupců

* Použijeme nepovinný parametr `widths`, kde šířky nastavíme

```python
import pandas
 
# separator/delimiter specification not needed there
df = pandas.read_fwf("tiobe.txt", widths=(20, 20, 20, 20, 20, 20))
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

### Zpracování souborů s nestandardním formátem

* https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
* Evidentně se jedná o tabulková a velmi dobře strukturovaná data, která by bylo vhodné umět automaticky zpracovat

```
20.11.2020 #224
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|16,231
Brazílie|real|1|BRL|4,160
Bulharsko|lev|1|BGN|13,467
Čína|žen-min-pi|1|CNY|3,381
Dánsko|koruna|1|DKK|3,536
EMU|euro|1|EUR|26,340
Filipíny|peso|100|PHP|46,038
Hongkong|dolar|1|HKD|2,864
Chorvatsko|kuna|1|HRK|3,481
Indie|rupie|100|INR|29,950
Indonesie|rupie|1000|IDR|1,567
Island|koruna|100|ISK|16,330
Izrael|nový šekel|1|ILS|6,649
Japonsko|jen|100|JPY|21,383
Jižní Afrika|rand|1|ZAR|1,445
Kanada|dolar|1|CAD|17,011
Korejská republika|won|100|KRW|1,990
Maďarsko|forint|100|HUF|7,328
Malajsie|ringgit|1|MYR|5,425
Mexiko|peso|1|MXN|1,104
MMF|ZPČ|1|XDR|31,598
Norsko|koruna|1|NOK|2,471
Nový Zéland|dolar|1|NZD|15,416
Polsko|zlotý|1|PLN|5,900
Rumunsko|leu|1|RON|5,405
Rusko|rubl|100|RUB|29,180
Singapur|dolar|1|SGD|16,530
Švédsko|koruna|1|SEK|2,577
Švýcarsko|frank|1|CHF|24,363
Thajsko|baht|100|THB|73,313
Turecko|lira|1|TRY|2,911
USA|dolar|1|USD|22,201
Velká Británie|libra|1|GBP|29,464
```

#### Pokus o načtení souboru s nestandardním formátem

* Výsledek není v žádném případě dokonalý, což značí, že budeme muset lépe a přesněji specifikovat konkrétní použitý formát dat

```python
import pandas
 
df = pandas.read_csv("denni_kurz.txt")
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

#### Specifikace oddělovače

* Použijeme pojmenovaný parametr `sep` předaný funkci `pandas.read_csv`

```python
import pandas
 
df = pandas.read_csv("denni_kurz.txt", sep="|")
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

#### Přeskok prvního řádku, který neobsahuje data tabulky ani hlavičku

* Aby byl textový soubor správně načten, musíme zcela přeskočit první řádek, jenž není součástí tabulky
* Nejjednodušší způsob spočívá v použití parametru nazvaného `skiprows`
    - pochopitelně i s dříve použitým parametrem `sep`

```python
import pandas
 
df = pandas.read_csv("denni_kurz.txt", sep="|", skiprows=1)
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

#### Převod záznamů s desetinnou čárkou na číselné hodnoty

* Poslední úpravou datového rámce, kterou musíme provést, je převod hodnot v
  posledním sloupci na numerické hodnoty. Tuto úpravu můžeme spustit po načtení
  datového rámce, a to tak, že de facto do rámce vložíme nový sloupec
  pojmenovaný stejně jako sloupec starý (tedy „kurz“). A hodnoty pro tento
  sloupec získáme nejprve řetězcovou záměnou desetinné čárky za desetinnou
  tečku a posléze převodem na numerické hodnoty, k čemuž použijeme konverzní
  funkci `pandas.to_numeric`

```python
import pandas
 
df = pandas.read_csv("denni_kurz.txt", sep="|", skiprows=1)
 
df["kurz"] = pandas.to_numeric(df["kurz"].str.replace(',','.'), errors='coerce')
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```

#### Načtení dat přímo z webu

* Data, resp. celé tabulky je možné v případě potřeby načíst přímo z internetu, databáze atd.

```python
import pandas
 
url = "https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
df = pandas.read_csv(url, sep="|", skiprows=1)
 
df["kurz"] = pandas.to_numeric(df["kurz"].str.replace(',','.'), errors='coerce')
 
print("Data frame")
print("---------------------------")
print(df)
print()
 
print("Column types")
print("---------------------------")
print(df.dtypes)
```



## Zobrazení obsahu datových rámců, vykreslení grafů a validace dat


### Nové datové typy podporované knihovnou Pandas

* Společně s knihovnou Pandas je dodávána i deklarace nových datových typů
* Důležité jsou především první dva typy
    - `Series` odvozený od jednodimenzionálního pole knihovny Numpy
    - `DataFrame`

```
#       Datový typ        Stručný popis
1       Series            odvozeno od 1D pole knihovny Numpy, rozšířeno o popis os
2       DataFrame         reprezentace dat uložených do tabulky s popisem os (sloupců, řádků)
3       DatetimeTZDtype   datum s přidanou informací o časové zóně
4       PeriodDtype       reprezentace časové periody (offsetu)
5       IntervalDtype     reprezentace numerického intervalu (odvozeno od dalších typů, například int64 atd.)
6       Int8Dtype         typ int8 rozšířený pro podporu hodnoty pandas.NA
7       Int16Dtype        typ int16 rozšířený pro podporu hodnoty pandas.NA
8       Int32Dtype        typ int32 rozšířený pro podporu hodnoty pandas.NA
9       Int64Dtype        typ int64 rozšířený pro podporu hodnoty pandas.NA
10      UInt8Dtype        typ uint8 rozšířený pro podporu hodnoty pandas.NA
11      UInt16Dtype       typ uint16 rozšířený pro podporu hodnoty pandas.NA
12      UInt32Dtype       typ uint32 rozšířený pro podporu hodnoty pandas.NA
13      UInt64Dtype       typ uint64 rozšířený pro podporu hodnoty pandas.NA
14      CategoricalDtype  kategorie (odvozeno od jazyka R, bude popsáno příště)
15      SparseDtype       použito pro ukládání řídkých polí (bude popsáno příště)
16      StringDtype       rozšíření řetězců; prozatím ve fázi experimentálního rozšíření
17      BooleanDtype      rozšíření pravdivostního typu; prozatím ve fázi experimentálního rozšíření
```

### Zobrazení obsahu datového rámce

```python
import pandas
 
df = pandas.read_csv("denni_kurz.txt", sep="|", skiprows=1)
 
df["kurz"] = pandas.to_numeric(df["kurz"].str.replace(',','.'), errors='coerce')
 
print(df)
```

* Pro rozsáhlejší datové rámce

```python
import pandas
 
df = pandas.read_csv("denni_kurz.txt", sep="|", skiprows=1)
 
df["kurz"] = pandas.to_numeric(df["kurz"].str.replace(',','.'), errors='coerce')
 
print(df.head())
```

### Zobrazení podrobnějších informací o datovém rámci

* Informace o typech
* Informace o sloucích
* Obsazení operační paměti

#### `df.types`

```python
import pandas
 
df = pandas.read_csv("denni_kurz.txt", sep="|", skiprows=1)
 
df["kurz"] = pandas.to_numeric(df["kurz"].str.replace(',','.'), errors='coerce')
 
print(df.dtypes)
```

#### `df.columns`

```python
import pandas
 
df = pandas.read_csv("denni_kurz.txt", sep="|", skiprows=1)
 
df["kurz"] = pandas.to_numeric(df["kurz"].str.replace(',','.'), errors='coerce')
 
print(df.columns)
```

#### `df.info`

```python
import pandas
 
df = pandas.read_csv("denni_kurz.txt", sep="|", skiprows=1)
 
df["kurz"] = pandas.to_numeric(df["kurz"].str.replace(',','.'), errors='coerce')
 
print(df.info())
```

#### Osy, dimenze a velikost

* Další informace se týkají os (axes)
  - osy vertikální i horizontální (v rámci tabulky)
* Počtu dimenzí
   - prakticky vždy dvě
* Tvaru
   - počet řádků×počet sloupců
* Velikosti
   - výsledek počet řádků×počet sloupců

```
import pandas
 
df = pandas.read_csv("denni_kurz.txt", sep="|", skiprows=1)
 
df["kurz"] = pandas.to_numeric(df["kurz"].str.replace(',','.'), errors='coerce')
 
print("Axes: ", df.axes)
print("Ndim: ", df.ndim)
print("Size: ", df.size)
print("Shape: ", df.shape)
```

### Základní statistické informace o datech uložených v rámci

* Metodou `describe` lze získat základní (a mnohdy velmi užitečné) statistické informace o záznamech uložených v datovém rámci

```python
import pandas
 
df = pandas.read_csv("denni_kurz.txt", sep="|", skiprows=1)
 
df["kurz"] = pandas.to_numeric(df["kurz"].str.replace(',','.'), errors='coerce')
 
print(df.describe())
```

### Kooperace mezi Pandas a Matplotlibem

* CSV s daty načteme přímo do datového rámce
* Vypočteme koeficienty lineární regrese
* Vykreslíme průběh načtených hodnot
* A taktéž úsečku získanou lineární regresí

```python
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  plot_kafka_lags_pandas.py input_file.csv")
    print("Example:")
    print("  plot_kafka_lags_pandas.py overall.csv")
    sys.exit(1)
 
# First command line argument should contain name of input CSV.
input_csv = sys.argv[1]
 
df = pd.read_csv(input_csv)
 
print(df.info())
print(df.describe())
 
# Linear regression
time = df["Time"]
messages = df["topic : uploads"]
 
# Linear regression
x = np.arange(0, len(messages))
coef = np.polyfit(x, messages, 1)
poly1d_fn = np.poly1d(coef)
 
# Create new graph
plt.plot(messages, "b", poly1d_fn(np.arange(0, len(messages))), 'y--')
 
# Title of a graph
plt.title("Messages in Kafka")
 
# Add a label to x-axis
plt.xlabel("Time")
 
# Add a label to y-axis
plt.ylabel("Messages")
 
plt.legend(loc="upper right")
 
# Set the plot layout
plt.tight_layout()
 
# And save the plot into raster format and vector format as well
plt.savefig("kafka_lags_pandas.png")
plt.savefig("kafka_lags_pandas.svg")
 
# Try to show the plot on screen
plt.show()
```

### Přímé vykreslení grafu bez použití knihovny Matplotlib

* O vytvoření grafu se může postarat přímo knihovna Pandas

```python
import sys
import pandas as pd
import matplotlib.pyplot as plt
 
# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  plot_kafka_lags_pandas_2.py input_file.csv")
    print("Example:")
    print("  plot_kafka_lags_pandas_2.py overall.csv")
    sys.exit(1)
 
# First command line argument should contain name of input CSV.
input_csv = sys.argv[1]
 
df = pd.read_csv(input_csv)
 
print(df.info())
print(df.describe())
 
# Create new histogram graph
df.plot(x="Time", y="topic : uploads")
 
# Try to show the plot on screen
plt.show()
```

### Přidání klouzavého průměru do grafu

* Výpočet klouzavého průměru je relativně přímočarý
  - pouze musíme zajistit, že se do datového rámce přidá další sloupec s výsledky
  - využívají se nám již známé metody `df.shape`, popř. `df.iloc`:

```python
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  plot_kafka_lags_pandas_sma_3.py input_file.csv")
    print("Example:")
    print("  plot_kafka_lags_pandas_sma_3.py overall.csv")
    sys.exit(1)
 
# First command line argument should contain name of input CSV.
input_csv = sys.argv[1]
 
df = pd.read_csv(input_csv)
 
for i in range(0, df.shape[0]-2):
    df.loc[df.index[i+2], 'SMA_3'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1])/3),1)
 
print(df)
print(df.info())
print(df.describe())
 
# Create new histogram graph
df.plot(x="Time", y=["topic : uploads", "SMA_3"])
 
# Try to show the plot on screen
plt.show()
```

### Vylepšený výpočet klouzavého průměru

* Existuje však i možnost použít při výpočtu přímo možností nabízených samotnou knihovnou Pandas
  - konkrétně metody `rolling` a `mean`

```python
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  plot_kafka_lags_pandas_sma_3.py input_file.csv")
    print("Example:")
    print("  plot_kafka_lags_pandas_sma_3.py overall.csv")
    sys.exit(1)
 
# First command line argument should contain name of input CSV.
input_csv = sys.argv[1]
 
df = pd.read_csv(input_csv)
 
df['SMA_3'] = df.iloc[:,1].rolling(window=3).mean()
 
print(df)
print(df.info())
print(df.describe())
 
# Create new histogram graph
df.plot(x="Time", y=["topic : uploads", "SMA_3"])
 
# Try to show the plot on screen
plt.show()
```

### Sloupcové grafy

* `df.plot.bar()`

```python
#!/usr/bin/env python3
 
import sys
import pandas as pd
import matplotlib.pyplot as plt
 
# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  plot_benchmark_results_bar_chart.py ")
    print("Example:")
    print("  plot_benchmark_results_bar_chart.py data.tsv")
    sys.exit(1)
 
# First command line argument should contain name of input CSV.
input_file = sys.argv[1]
 
df = pd.read_csv(input_file, sep="\t")
 
data_columns = ["ANSI C", "Cython #1", "Cython #2", "Cython #3", "Numba #1/interpret", "Numba #2", "Numba #3", "Numba #4"]
 
for data_column in data_columns:
    df[data_column] = pd.to_numeric(df[data_column].str.replace(',', '.'), errors='coerce')
 
print(df)
print()
 
print(df.info())
print()
 
print(df.describe())
print()
 
 
# Create new histogram graph
df.plot.bar(x="Height", y=data_columns)
 
# Try to show the plot on screen
plt.show()
```



## Práce s datovými řadami (series)

* Základním stavebním kamenem knihovny Pandas je typ `Series` (datová řada)
  - zapouzdřuje jednodimenzionální pole z knihovny Numpy
  - představuje uspořádaný sloupec údajů, které mají shodný typ (například int64 nebo float64 atd.)
  - každému prvku je přiřazen index
  - nemusí se přitom jednat o celé číslo, protože indexem mohou být i řetězce atd.

* Instance třídy `Series` mají několik užitečných atributů

```
#  Atribut   Stručný popis
1  index     indexy prvků v řadě
2  values    hodnoty prvků ve formě 1D pole
3  size      počet prvků v řadě
4  name      jméno řady (pokud je specifikováno)
5  dtype     typ prvků uložených v datové řadě
6  hasnans   test, zda je nějaký prvek roven NaN
```

### Konstrukce datové řady

```python
import pandas
 
s = pandas.Series((1, 2, 3, 4, 5, 6))
 
print("Series:")
print(s)
print()
 
print("Index:")
print(s.index)
print()
 
print("Values:")
print(s.values)
print()
```

### Specifikace indexů

* Počet prvků musí být roven počtu indexů!

```python
import pandas
 
s = pandas.Series(('a', 'b', 'c', 'd', 'e', 'f'), (1, 2, 3, 4, 5, 6))
 
print("Series:")
print(s)
print()
 
print("Index:")
print(s.index)
print()
 
print("Values:")
print(s.values)
print()
```

### Konstrukce datové řady ze slovníku

```python
import pandas
 
input_data = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        }
 
print("Input data:")
print(input_data)
print()
 
s = pandas.Series(input_data)
 
print("Series:")
print(s)
print()
 
print("Index:")
print(s.index)
print()
 
print("Values:")
print(s.values)
print()
```

### Pro statší Python (<3.8)

* Zachování pořadí prvků

```python
import pandas
from collections import OrderedDict
 
input_data = OrderedDict()
 
input_data["f"] = 6
input_data["e"] = 5
input_data["d"] = 4
input_data["c"] = 3
input_data["b"] = 2
input_data["a"] = 1
 
print("Input data:")
print(input_data)
print()
 
s = pandas.Series(input_data)
 
print("Series:")
print(s)
print()
 
print("Index:")
print(s.index)
print()
 
print("Values:")
print(s.values)
print()
```

### Vytvoření nové datové řady z řady stávající – výběr prvků na základě jejich indexů

## Spojování datových rámců s využitím append, concat, merge a join

## Použití metody groupby, naformátování a export tabulek pro tisk

## Práce se seskupenými záznamy, vytvoření multiindexů

## Odkazy na další informační zdroje

* Seriál: Knihovna Pandas 
  [https://www.root.cz/serialy/knihovna-pandas/](https://www.root.cz/serialy/knihovna-pandas/)
* Knihovna Pandas: základy práce s datovými rámci
  [https://www.root.cz/clanky/knihovna-pandas-zaklady-prace-s-datovymi-ramci/](https://www.root.cz/clanky/knihovna-pandas-zaklady-prace-s-datovymi-ramci/)
* Knihovna Pandas: zobrazení obsahu datových rámců, vykreslení grafů a validace dat
  [https://www.root.cz/clanky/knihovna-pandas-zobrazeni-obsahu-datovych-ramcu-vykresleni-grafu-a-validace-dat/](https://www.root.cz/clanky/knihovna-pandas-zobrazeni-obsahu-datovych-ramcu-vykresleni-grafu-a-validace-dat/)
* Knihovna Pandas: práce s datovými řadami (series)
  [https://www.root.cz/clanky/knihovna-pandas-prace-s-datovymi-radami-series/](https://www.root.cz/clanky/knihovna-pandas-prace-s-datovymi-radami-series/)
* Knihovna Pandas: pokročilejší práce s datovými řadami (series)
  [https://www.root.cz/clanky/knihovna-pandas-pokrocilejsi-prace-s-datovymi-radami-series/](https://www.root.cz/clanky/knihovna-pandas-pokrocilejsi-prace-s-datovymi-radami-series/)
* Knihovna Pandas: spojování datových rámců s využitím append, concat, merge a join
  [https://www.root.cz/clanky/knihovna-pandas-spojovani-datovych-ramcu-s-vyuzitim-append-concat-merge-a-join/](https://www.root.cz/clanky/knihovna-pandas-spojovani-datovych-ramcu-s-vyuzitim-append-concat-merge-a-join/)
* Knihovna Pandas: použití metody groupby, naformátování a export tabulek pro tisk
  [https://www.root.cz/clanky/knihovna-pandas-pouziti-metody-groupby-naformatovani-a-export-tabulek-pro-tisk/](https://www.root.cz/clanky/knihovna-pandas-pouziti-metody-groupby-naformatovani-a-export-tabulek-pro-tisk/)
* Knihovna Pandas: práce se seskupenými záznamy, vytvoření multiindexů
  [https://www.root.cz/clanky/knihovna-pandas-prace-se-seskupenymi-zaznamy-vytvoreni-multiindexu/](https://www.root.cz/clanky/knihovna-pandas-prace-se-seskupenymi-zaznamy-vytvoreni-multiindexu/)
