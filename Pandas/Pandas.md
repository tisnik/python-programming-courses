# Knihovna Pandas

![pandas_logo.png](pandas_logo.png)

### Autor Pavel Tišnovský
### Email kurzy.python@centrum.cz



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

### Pro starší Python (<3.8)

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

* Datovou řadu je možné vytvořit z řady již existující
  - výběrem indexů těch prvků, které mají být přidány do nové řady
* Podobně je možné změnit (mutovat) stávající datovou řadu
* Pro oba účely se používá metoda nazvaná `pandas.Series.reindex`
  - té se předá seznam, popř. pole indexů vybíraných prvků.

```python
import pandas
 
s = pandas.Series(range(1, 7), ('a', 'b', 'c', 'd', 'e', 'f'))
 
print("Series:")
print(s)
print()
 
print("Index:")
print(s.index)
print()
 
print("Values:")
print(s.values)
print()
 
s = s.reindex(['d', 'a', 'b', 'c', 'd', 'a', 'a', 'a'])
 
print("Reindexed:")
print()
 
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

### Základní statistické informace o prvcích uložených v datové řadě

```python
import pandas
 
s = pandas.Series(range(1, 7), ('a', 'b', 'c', 'd', 'e', 'f'))
 
print("sum", s.sum(), sep="\t")
print("prod", s.prod(), sep="\t")
print("min", s.min(), sep="\t")
print("max", s.max(), sep="\t")
print("median", s.median(), sep="\t")
print("std", s.std(), sep="\t")
print("var", s.var(), sep="\t")
print("quantile", s.quantile(0.01), sep="\t")
```

### Přeskočení chybějících hodnot při výpočtu statistických informací

```python
import pandas
 
s = pandas.Series((1, 2, None, 4, 5, 6), ('a', 'b', 'c', 'd', 'e', 'f'))
 
print("sum", s.sum(), sep="\t")
print("prod", s.prod(), sep="\t")
print("min", s.min(), sep="\t")
print("max", s.max(), sep="\t")
print("median", s.median(), sep="\t")
print("std", s.std(), sep="\t")
print("var", s.var(), sep="\t")
print("quantile", s.quantile(0.01), sep="\t")
```

### Vektorové operace nad všemi prvky datové řady

```python
import numpy as np
import pandas
 
s1 = pandas.Series(range(1, 7), ('a', 'b', 'c', 'd', 'e', 'f'))
 
print(s1 + 10)
print(s1 - 10)
print(s1 * 10)
print(s1 / 10)
 
print(s1 % 2)
```

### Relační operátory

* Výsledkem je nová datová řada s hodnotami `True` a `False`

```python
import numpy as np
import pandas
 
s1 = pandas.Series(range(1, 7), ('a', 'b', 'c', 'd', 'e', 'f'))
 
print(s1 > 3)
print(s1 < 3)
print(s1 % 2 == 0)
```

#### Hodnoty None a NA, které se vyhodnotí na False

```python
import numpy as np
import pandas
 
s1 = pandas.Series((1, 2, None, 4, 5, 6), ('a', 'b', 'c', 'd', 'e', 'f'))
 
print(s1 > 3)
print(s1 < 3)
print(s1 % 2 == 0)
```

### Výběr prvků z datové řady na základě podmínky

* Knihovna Pandas umožňuje výběr prvků z datové řady na základě vyhodnocení podmínky pro každý prvek
* V tomto případě je nutné podmínku zapsat do hranatých (indexových) závorek
* Pokud se podmínka vyhodnotí na `True`, bude prvek použit ve výsledku, v opačném případě bude zahozen
* Vybírat tedy můžeme prvky menší nebo větší než nějaká hodnota, prvky dělitelné dvěma atd.

```python
import numpy as np
import pandas
 
s1 = pandas.Series(range(1, 7))
s2 = pandas.Series(range(50))
 
print(s1[s1<3])
print(s1[s1>3])
 
print(s2[s2 % 2 == 0])
print(s2[s2 % 2 != 0])
 
print(s2[s2 % 3 == 0])
```

* Nic nám ovšem nebrání provádět výběr na základě logické operace aplikované na odlišnou datovou řadu

```python
import numpy as np
import pandas
 
s1 = pandas.Series(range(1, 7))
s2 = pandas.Series(range(-3, 3))
 
print(s1[s2 >= 0])
print(s1[s2 < 0])
print(s1[s2 != 0])
```

### Konverze mezi různými datovými typy datové řady

```python
import pandas
 
s = pandas.Series((100, 200, 300, 400, 500, 600))
print(s.dtypes)
print(s)
print()
 
s = s.astype('int32')
print(s.dtypes)
print(s)
print()
 
s =s.astype('int8')
print(s.dtypes)
print(s)
```

* Taktéž je možné využít automatickou konverzi na ten nejlepší datový typ

```python
import pandas
 
s = pandas.Series((100, 200, 300, 400, 500, 600), dtype="float32")
print(s.dtypes)
print(s)
print()
 
s = s.convert_dtypes()
print(s.dtypes)
print(s)
print()
```

### Vykreslení hodnot prvků z datové řady formou grafu

* Založeno na knihovně Matplotlib

```
#    Metoda                       Stručný popis
1    pandas.Series.plot           graf vybraný parametrem kind
2    pandas.Series.plot.area      oblast pod průběhem je vyplněna barvou (pro kladné hodnoty)
3    pandas.Series.plot.bar       sloupcový graf s vertikálně orientovanými sloupci
4    pandas.Series.plot.barh      sloupcový graf s horizontálně orientovanými sloupci
5    pandas.Series.plot.box       krabicový diagram
6    pandas.Series.plot.density   diagram založený na KDE
7    pandas.Series.plot.hist      histogram
8    pandas.Series.plot.kde       diagram založený na KDE
9    pandas.Series.plot.line      stejné jako pandas.Series.plot
10   pandas.Series.plot.pie       koláčový diagram
11   pandas.Series.hist           histogram
```

### Liniový (spojnicový) graf

```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
 
# hodnoty na x-ové ose
r = np.linspace(0, 2*np.pi, 100)
 
# konstrukce struktury Series - datové řady
s = pandas.Series(data=np.sin(r), index=r)
 
# tisk obsahu Series
print(s)
 
# vytvoření grafu
s.plot()
 
# uložení grafu
plt.savefig("series_plot_01.png")
 
# vykreslení grafu
plt.show()
```

### Vyplnění plochy pod funkcí/hodnotami

```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
 
# hodnoty na x-ové ose
r = np.linspace(0, 2*np.pi, 100)
 
# konstrukce struktury Series - datové řady
s = pandas.Series(data=np.sin(r), index=r)
 
# tisk obsahu Series
print(s)
 
# vytvoření grafu
s.plot.area(stacked=False)
 
# uložení grafu
plt.savefig("series_plot_02.png")
 
# vykreslení grafu
plt.show()
```

### Vertikální i horizontální sloupcové grafy

* Vertikální sloupce

```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
 
# hodnoty na x-ové ose
r = np.linspace(0, 2*np.pi, 20)
 
# konstrukce struktury Series - datové řady
s = pandas.Series(data=np.sin(r), index=r)
 
# tisk obsahu Series
print(s)
 
# vytvoření grafu
s.plot.bar(grid=True)
 
# uložení grafu
plt.savefig("series_plot_03.png")
 
# vykreslení grafu
plt.show()
```

* Horizontální sloupce

```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
 
# hodnoty na x-ové ose
r = np.linspace(0, 2*np.pi, 20)
 
# konstrukce struktury Series - datové řady
s = pandas.Series(data=np.sin(r), index=r)
 
# tisk obsahu Series
print(s)
 
# vytvoření grafu
s.plot.barh(grid=True)
 
# uložení grafu
plt.savefig("series_plot_04.png")
 
# vykreslení grafu
plt.show()
```


### Graf s KDE (Kernel density estimation)

* Narozdíl od histogramu umožňuje KDE lépe popsat skutečné chování dat, kterých se předpokládá, že tvoří spojitou funkc

```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
 
# hodnoty na x-ové ose
r = np.linspace(0, 2*np.pi, 100)
 
# konstrukce struktury Series - datové řady
s = pandas.Series(data=np.sin(r), index=r)
 
# tisk obsahu Series
print(s)
 
# vytvoření grafu
s.plot.kde(grid=True)
 
# vykreslení grafu
plt.show()
```

### Koláčový diagram

* Vstupní data

```
Sep 2020  Sep 2019  Change    Language           Ratings   Changep
1         2         change    C                  15.95     +0.74
2         1         change    Java               13.48     -3.18
3         3                   Python             10.47     +0.59
4         4                   C++                7.11      +1.48
5         5                   C#                 4.58      +1.18
6         6                   Visual Basic       4.12      +0.83
7         7                   JavaScript         2.54      +0.41
8         9         change    PHP                2.49      +0.62
9         19        change    R                  2.37      +1.33
10        8         change    SQL                1.76      -0.19
11        14        change    Go                 1.46      +0.24
12        16        change    Swift              1.38      +0.28
13        20        change    Perl               1.30      +0.26
14        12        change    Assembly language  1.30      -0.08
15        15                  Ruby               1.24      +0.03
16        18        change    MATLAB             1.10      +0.04
17        11        change    Groovy             0.99      -0.52
18        33        change    Rust               0.92      +0.55
19        10        change    Objective-C        0.85      -0.99
20        24        change    Dart               0.77      +0.13
```

```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# pro jistotu si datový rámec zobrazíme
print(df)
 
# konstrukce struktury Series - datové řady z datového rámce
s = pandas.Series(df["Ratings"])
 
# tisk obsahu Series
print(s)
 
# vytvoření grafu
s.plot.pie()
 
# vykreslení grafu
plt.show()
```

### Data obsahující šum

* Simulace šumu

```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
 
# hodnoty na x-ové ose
r = np.linspace(0, 2*np.pi, 100)
 
# konstrukce datové struktury Series
s = pandas.Series(data=np.sin(r), index=r)
 
# šum
s2 = np.random.rand(100)/2
 
# přidání šumu k původní řadě
s3 = s + s2
 
# tisk obsahu Series
print(s3)
 
# vytvoření grafu
s3.plot(grid=True)
 
# vykreslení grafu
plt.show()
```

### Vyhlazení průběhu na grafu

```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
 
# hodnoty na x-ové ose
r = np.linspace(0, 2*np.pi, 100)
 
# konstrukce struktury Series - datové řady
s = pandas.Series(data=np.sin(r), index=r)
 
# přidání šumu
s2 = s.map(lambda x: x+np.random.rand()/2)
 
# vyhlazení (moving average)
s3 = s2.rolling(2).mean()
 
# tisk obsahu Series
print(s3)
 
# vytvoření grafu
s3.plot(grid=True)
 
# vykreslení grafu
plt.show()
```

* Širší vyhlazovaná oblast

```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
 
# hodnoty na x-ové ose
r = np.linspace(0, 2*np.pi, 100)
 
# konstrukce struktury Series - datové řady
s = pandas.Series(data=np.sin(r), index=r)
 
# přidání šumu
s2 = s.map(lambda x: x+np.random.rand()/2)
 
# vyhlazení (moving average)
s3 = s2.rolling(20).mean()
 
# tisk obsahu Series
print(s3)
 
# vytvoření grafu
s3.plot(grid=True)
 
# vykreslení grafu
plt.show()
```

* Váhování vzorků Gaussovou křivkou

```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
 
# hodnoty na x-ové ose
r = np.linspace(0, 2*np.pi, 100)
 
# konstrukce struktury Series - datové řady
s = pandas.Series(data=np.sin(r), index=r)
 
s2 = s.map(lambda x: x+np.random.rand()/2)
 
s3 = s2.rolling(10, win_type="gaussian").sum(std=3)
 
# tisk obsahu Series
print(s3)
 
# vytvoření grafu
s3.plot(grid=True)
 
# vykreslení grafu
plt.show()
```

### Graf s několika průběhy získanými z datové řady, použití podgrafů

* Budeme muset zkombinovat možnosti knihoven Pandas i Matplotlib

```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
 
# hodnoty na x-ové ose
r = np.linspace(0, 2*np.pi, 100)
 
# konstrukce struktury Series - datové řady
s = pandas.Series(data=np.sin(r), index=r)
 
s2 = s.map(lambda x: x+np.random.rand()/2)
 
s3 = s2 - s
 
# vytvoření grafu
plt.plot(s, "--", s2, "-", s3, "-")
 
# uložení grafu
plt.savefig("series_plot_11.png")
 
# vykreslení grafu
plt.show()
```

### Podgrafy

```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
 
# hodnoty na x-ové ose
r = np.linspace(0, 2*np.pi, 100)
 
# konstrukce struktury Series - datové řady
s = pandas.Series(data=np.sin(r), index=r)
 
s2 = s.map(lambda x: x+np.random.rand()/2)
 
s3 = s2 - s
 
# vytvoření grafu
plt.subplot(221)
plt.plot(s)
 
plt.subplot(222)
plt.plot(s2)
 
plt.subplot(223)
plt.plot(s3)
 
# uložení grafu
plt.savefig("series_plot_12.png")
 
# vykreslení grafu
plt.show()
```

### Iterace přes všechny prvky datové řady

* V každé iteraci se vrací tuple (n-tice)

```python
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# pro jistotu si datový rámec zobrazíme
print(df)
 
# konstrukce datové struktury Series z datového rámce
s = pandas.Series(df["Ratings"])
 
# tisk obsahu Series
print(s)
 
# iterace nad prvky rady
for index, value in s.items():
    print("Index: {:20}  Value: {:5.3}".format(index, value))
```

#### Alternativní způsob s metodou `iteritems`

```python
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# pro jistotu si datový rámec zobrazíme
print(df)
 
# konstrukce datové struktury Series z datového rámce
s = pandas.Series(df["Ratings"])
 
# tisk obsahu Series
print(s)
 
# iterace nad prvky rady
for index, value in s.iteritems():
    print("Index: {:20}  Value: {:5.3}".format(index, value))
```

### Aplikace vybrané funkce na všechny prvky datové řady

```python
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# pro jistotu si datový rámec zobrazíme
print(df)
 
# konstrukce datové struktury Series (datové řady) z datového rámce
s = pandas.Series(df["Ratings"])
 
# tisk obsahu původní datové řady
print("In percents")
print(s)
print()
 
# převod na skutečný poměr <0, 1>
s2 = s.map(lambda x: x/100.0)
 
# tisk obsahu nové datové řady
print("As ratios")
print(s2)
```

#### Naformátování hodnot v datové řadě

```python
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# pro jistotu si datový rámec zobrazíme
print(df)
 
# konstrukce datové struktury Series (datové řady) z datového rámce
s = pandas.Series(df["Ratings"])
 
# tisk obsahu původní datové řady
print("In percents")
print(s)
print()
 
# formát hodnot v datové řadě
s2 = s.map("Rating is {:4.1f} %".format)
 
# tisk obsahu nové datové řady
print("As ratings")
print(s2)
```

#### Transformace dat

```python
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# pro jistotu si datový rámec zobrazíme
print(df)
 
# konstrukce datové struktury Series (datové řady) z datového rámce
s = pandas.Series(df["Ratings"])
 
# tisk obsahu původní datové řady
print("In percents")
print(s)
print()
 
# převod na skutečný poměr <0, 1>
s2 = s.transform(lambda x: x/100.0)
 
# tisk obsahu nové datové řady
print("As ratios")
print(s2)
```

#### Obecnější transformace

* Výsledkem bude nikoli jeden sloupec (tedy klasická datová řada), ale sloupce dva, které sdílí společný index

```python
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# pro jistotu si datový rámec zobrazíme
print(df)
 
# konstrukce datové struktury Series (datové řady) z datového rámce
s = pandas.Series(df["Ratings"])
 
# tisk obsahu původní datové řady
print("In percents")
print(s)
print()
 
# převod na skutečný poměr <0, 1>
s2 = s.transform([lambda x: x, lambda x: x/100.0])
 
# tisk obsahu nové datové řady
print("In percents and also as ratios")
print(s2)
```

### Agregace informací z datové řady

```
import pandas
import numpy as np
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# pro jistotu si datový rámec zobrazíme
print(df)
 
# konstrukce datové struktury Series (datové řady) z datového rámce
s = pandas.Series(df["Ratings"])
 
# tisk obsahu původní datové řady
print("In percents")
print(s)
print()
 
# agregace výsledků
results = s.aggregate([np.min, np.max, np.sum, np.mean])
 
# tisk výsledku
print("Results")
print(results)
```

### Kombinace údajů ze dvou datových řad, popř. datové řady a skalární hodnoty

* Zkombinujeme (postupně) hodnotu prvků z datové řady s hodnotou 2, resp. 10
* Přičemž kombinace bude provedena funkcemi `min` a `max`
* V prvním případě tedy nahradíme ty prvky z řady, které jsou větší než 10 hodnotou 10
* A následně ty prvky z řady, které jsou menší než 2 právě hodnotou 2

```python
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# pro jistotu si datový rámec zobrazíme
print(df)
 
# konstrukce datové struktury Series (datové řady) z datového rámce
s = pandas.Series(df["Ratings"])
 
# tisk obsahu původní datové řady
print(s)
print()
 
# omezení hodnot
results = s.combine(10, min)
 
# tisk výsledku
print("Bound (max)")
print(results)
 
# omezení hodnot
results = results.combine(2, max)
 
# tisk výsledku
print("Bound (min)")
print(results)
```

### Výběr hodnot na základě zadané podmínky metodou `Series.mask`

* Tato metoda vrátí novou datovou řadu
* Prvky odpovídající zadané podmínce maskovány hodnotou `NA` nebo `NaN`
  - kterou je možné později odstranit

```python
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# pro jistotu si datový rámec zobrazíme
print(df)
 
# konstrukce datové struktury Series (datové řady) z datového rámce
s = pandas.Series(df["Ratings"])
 
# tisk obsahu původní datové řady
print(s)
print()
 
# maskování hodnot
results = s.mask(s > 10)
 
# tisk výsledku
print("Masked (max)")
print(results)
 
# maskování hodnot
results = results.mask(s < 2)
 
# tisk výsledku
print("Masked (min)")
print(results)
```

### Výběr hodnot na základě zadané podmínky metodou `Series.where`

* Dokáže změnit vybrané prvky na určitou hodnotu
  -  je tedy přesným opakem metody `Series.mask`

```python
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# pro jistotu si datový rámec zobrazíme
print(df)
 
# konstrukce datové struktury Series (datové řady) z datového rámce
s = pandas.Series(df["Ratings"])
 
# tisk obsahu původní datové řady
print(s)
print()
 
# maskování hodnot
results = s.where(s < 10, "Dobře")
 
# tisk výsledku
print(results)
 
# maskování hodnot
results = results.where(s > 2, "Nic moc")
 
# tisk výsledku
print(results)
```

### Skutečná filtrace dat kombinující `Series.where` a `Series.dropna`

* V předchozích příkladech jsme „pouze“ nahrazovali prvky na základě splnění či nesplnění podmínky za hodnoty NaN, popř. NA
* Tyto hodnoty je možné snadno z datové řady odstranit, a to s využitím metody `Series.dropna`:

```python
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# pro jistotu si datový rámec zobrazíme
print(df)
 
# konstrukce datové struktury Series (datové řady) z datového rámce
s = pandas.Series(df["Ratings"])
 
# tisk obsahu původní datové řady
print(s)
print()
 
# maskování hodnot
results = s.where(s < 10)
 
# tisk výsledku
print(results)
 
results = results.dropna()
 
# tisk nového výsledku
print(results)
```

### Výběr prvků metodou `Series.filter`

```python
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# pro jistotu si datový rámec zobrazíme
print(df)
print()
 
# konstrukce datové struktury Series (datové řady) z datového rámce
s = pandas.Series(df["Ratings"])
 
# tisk obsahu původní datové řady
print(s)
print()
 
# maskování hodnot
results = s.filter(regex="C.*")
 
# tisk výsledku
print(results)
```

## Další často používané operace s rámci

### Přidání nového datového sloupce odvozeného z existujícího sloupce

```python
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# převod na skutečný poměr <0, 1>
df["Ratings as ratio"] = df["Ratings"].map(lambda x: x/100.0)
 
# datový rámec zobrazíme
print(df)
print()
 
# podrobnější informace o datovém rámci
print(df.dtypes)
print()
 
# více podrobnějších informací o datovém rámci
print(df.info())
print()
```

### Přepis původního sloupce „Ratings“ zkonvertovanými hodnotami:

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8
 
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# převod na skutečný poměr <0, 1>
df["Ratings"] = df["Ratings"].map(lambda x: x/100.0)
 
# datový rámec zobrazíme
print(df)
print()
 
# podrobnější informace o datovém rámci
print(df.dtypes)
print()
 
# více podrobnějších informací o datovém rámci
print(df.info())
print()
```

### Přímá aplikace funkce format bez nutnosti použití lambda výrazu:

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8
 
import pandas
 
# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)
 
# formát hodnot ve sloupci
df["Ratings"] = df["Ratings"].map("Rating is {:4.1f}%".format)
 
# datový rámec zobrazíme
print(df)
print()
 
# podrobnější informace o datovém rámci
print(df.dtypes)
print()
 
# více podrobnějších informací o datovém rámci
print(df.info())
print()
```

## Spojování datových rámců s využitím append, concat, merge a join

Různé způsoby spojení rámců:

* pod sebou
    - co s neexistujícími sloupci?
* vedle sebe
    - co s neexistujícími řádky?

### Spojení datových rámců metodou `append`

```python
import pandas
 
# přečtení zdrojových dat
df1 = pandas.read_csv("tiobeC.tsv", sep="\t")
df2 = pandas.read_csv("tiobeD.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df1.set_index("Language", inplace=True)
df2.set_index("Language", inplace=True)
 
# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()
 
# spojení obou datových rámců
concatenated = df1.append(df2)
 
# výpis výsledku
print(concatenated)
```

### Spojení rámců po sloupcích nebo po řádcích funkcí `concat`

* Alternativní možnost spojení dvou datových rámců nabízí funkce nazvaná `concat`
* Je aplikovatelná pro libovolný počet instancí třídy `DataFrame`
* Tato funkce dokáže datové rámce spojit buď po sloupcích nebo po řádcích
  - a to v závislosti na hodnotě parametru `axis`, který by měl obsahovat hodnotu 0 nebo 1 (popř. nebýt vůbec uveden)

#### Spojení rámců po sloupcích

```python
import pandas
 
# přečtení zdrojových dat
df1 = pandas.read_csv("tiobeE.tsv", sep="\t")
df2 = pandas.read_csv("tiobeF.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df1.set_index("Language", inplace=True)
df2.set_index("Language", inplace=True)
 
# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()
 
# spojení obou datových rámců
concatenated = pandas.concat([df1, df2], axis=1)
 
# výpis výsledku
print(concatenated)
```

#### Spojení rámců po řádcích

```python
import pandas
 
# přečtení zdrojových dat
df1 = pandas.read_csv("tiobeC.tsv", sep="\t")
df2 = pandas.read_csv("tiobeD.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df1.set_index("Language", inplace=True)
df2.set_index("Language", inplace=True)
 
# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()
 
# spojení obou datových rámců
concatenated = pandas.concat([df1, df2])
 
# výpis výsledku
print(concatenated)
```

### Funkce `merge`

* Velmi často se setkáme s nutností spojit dvě tabulky, které sice obsahují
  shodné sloupce, ovšem ne všechny řádky (resp. záznamy) nalezneme v obou
  spojovaných tabulkách
* Taková operace je zcela běžná v oblasti relačních databází (přesněji řečeno v
  SQL databázích), kde pro ni existuje i klauzule JOIN.
* Podle toho, jakým způsobem jsou do výsledku zařazeny ty záznamy, které nejsou
  nalezeny v obou spojovaných tabulkách, rozlišujeme:
   - vnitřní spojení (inner join)
   - vnější spojení (outer join)
* Vnější spojení je dále děleno na:
   - úplně vnější spojení (outer join)
   - vnější spojení zleva (left join)
   - vnější spojení zprava (right join)

#### Inner join (vnitřní spojení) založený na funkci `merge`

* Operace vnitřního spojení neboli inner join dokáže automaticky spojit ty
  řádky tabulek, které mají totožný obsah
* Současně jsou i identifikovány sloupce se shodným názvem a typem (pokud
  neurčíme jinak).

```python
import pandas
 
# přečtení zdrojových dat
df1 = pandas.read_csv("tiobeA.tsv", sep="\t")
df2 = pandas.read_csv("tiobeB.tsv", sep="\t")
 
# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()
 
# spojení obou datových rámců
merged = pandas.merge(df1, df2)
 
# výpis výsledku
print(merged)
```

* Spojení dvou datových rámců s explicitně nastavenými indexy získanými ze sloupce „Language“:

```python
import pandas
 
# přečtení zdrojových dat
df1 = pandas.read_csv("tiobeA.tsv", sep="\t")
df2 = pandas.read_csv("tiobeB.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df1.set_index("Language", inplace=True)
df2.set_index("Language", inplace=True)
 
# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()
 
# spojení obou datových rámců
merged = pandas.merge(df1, df2)
 
# výpis výsledku
print(merged)
```

* Předchozí demonstrační příklad lze rozšířit specifikací těch sloupců, které
  se skutečně mají spojit. To zařizuje nepovinný parametr on (což opět
  připomíná SQL konstrukci JOIN xxx ON):

```python
import pandas
 
# přečtení zdrojových dat
df1 = pandas.read_csv("tiobeA.tsv", sep="\t")
df2 = pandas.read_csv("tiobeB.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df1.set_index("Language", inplace=True)
df2.set_index("Language", inplace=True)
 
# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()
 
# spojení obou datových rámců
merged = pandas.merge(df1, df2, left_index=True, right_index=True,
                      on=["Change", "Ratings", "Changep"])

# výpis výsledku
print(merged)
```

#### Left join (vnější spojení „zleva“) založený na funkci `merge`

* Toto spojení je specifikováno parametrem how nastaveným na hodnotu „left“
  (jedná se o řetězec)
* Ve výsledném datovém rámci budou za všech okolností všechny řádky z levého
  rámce, a to i ve chvíli, kdy k nim nebyly nalezeny odpovídající řádky v
  pravém rámci

```python
import pandas
 
# přečtení zdrojových dat
df1 = pandas.read_csv("tiobeA.tsv", sep="\t")
df2 = pandas.read_csv("tiobeB.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df1.set_index("Language", inplace=True)
df2.set_index("Language", inplace=True)
 
# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()
 
# spojení obou datových rámců
merged = pandas.merge(df1, df2, left_index=True, right_index=True,
                      how="left",
                      on=["Change", "Ratings", "Changep"])
 
# výpis výsledku
print(merged)
```

#### Right join (vnější spojení „zprava“) založený na funkci `merge`

* Toto spojení je specifikováno parametrem how nastaveným na hodnotu „right“
  (opět se jedná o řetězec)
* Ve výsledném datovém rámci budou za všech okolností všechny řádky z pravého
  rámce, a to i ve chvíli, kdy k nim nebyly nalezeny odpovídající řádky v levém
  rámci

```python
import pandas
 
# přečtení zdrojových dat
df1 = pandas.read_csv("tiobeA.tsv", sep="\t")
df2 = pandas.read_csv("tiobeB.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df1.set_index("Language", inplace=True)
df2.set_index("Language", inplace=True)
 
# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()
 
# spojení obou datových rámců
merged = pandas.merge(df1, df2, left_index=True, right_index=True,
                      how="right",
                      on=["Change", "Ratings", "Changep"])
 
# výpis výsledku
print(merged)
```

#### Outer join (vnější spojení) založený na funkci `merge`

```python
import pandas
 
# přečtení zdrojových dat
df1 = pandas.read_csv("tiobeA.tsv", sep="\t")
df2 = pandas.read_csv("tiobeB.tsv", sep="\t")
 
# specifikace indexu - má se získat ze sloupce Language
df1.set_index("Language", inplace=True)
df2.set_index("Language", inplace=True)
 
# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()
 
# spojení obou datových rámců
merged = pandas.merge(df1, df2, left_index=True, right_index=True,
                      how="outer",
                      on=["Change", "Ratings", "Changep"])
 
# výpis výsledku
print(merged)
```

## Použití metody `groupby`, naformátování a export tabulek pro tisk

### Metoda `groupby`

* Jedná se o metodu, která umožňuje údaje z datových rámců rozdělit do
* Údaje z každé skupiny nějakým způsobem agregují
  - například se zjistí jejich počet, součet hodnot ve vybraném sloupci atd.


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
