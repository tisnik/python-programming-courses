# Jazyk Python

## Časté problémy

```python
# Třídní atributy jsou de facto uloženy ve slovníku
# Ve skutečnosti B a C nemají vlastní hodnoty atributů
# pouze reference do A

class A(object):
    attribute = "foo"


class B(A):
    pass


class C(A):
    pass


print(A.attribute, B.attribute, C.attribute)

A.attribute = "baz"

print(A.attribute, B.attribute, C.attribute)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/pitfalls/classes.py)

```python
# výchozí hodnota funkce je vyhodnocena pouze jedenkrát
# a to ve chvíli definici funkce

def foo(bar=[]):
    bar.append("baz")
    return bar

print(foo())

print(foo())

print(foo())
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/pitfalls/default_argument_1.py)

```python
# výchozí hodnota funkce je vyhodnocena pouze jedenkrát
# a to ve chvíli definici funkce

def foo(bar=None):
    if bar is None:
        bar = []
    bar.append("baz")
    return bar

print(foo())

print(foo())

print(foo())
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/pitfalls/default_argument_2.py)

```python
x = 1

def foo():
    x += 1
    print(x)

foo()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/pitfalls/scoping1.py)

```python
x = 1

def foo():
    global x
    x += 1
    print(x)

foo()
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/pitfalls/scoping2.py)

```python
seznam = []

def foo(x):
    seznam.append(x)

print(seznam)
foo(1)
print(seznam)
foo(2)
print(seznam)

def bar(x):
    seznam += [x]

print(seznam)
bar(3)
print(seznam)
bar(4)
print(seznam)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/pitfalls/scoping3.py)

```python
seznam = []

def foo(x):
    seznam.append(x)

print(seznam)
foo(1)
print(seznam)
foo(2)
print(seznam)

def bar(x):
    global seznam
    seznam += [x]

print(seznam)
bar(3)
print(seznam)
bar(4)
print(seznam)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/pitfalls/scoping4.py)

```python
y = 10

def adder(x):
    return y + x

print(adder(1))

y = 20

print(adder(1))
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/pitfalls/closures.py)

```python
# Python 2 vs Python 3

x = 0.2

x += 0.1

print(x)

print(repr(x))

print(str(x))
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/pitfalls/floats.py)

```python
numbers = [n for n in range(10)]

print(numbers)

for i in range(len(numbers)):
    print(i)
    if numbers[i] % 2 == 0:
        del numbers[i]

print(numbers)
```

[Zdrojový kód](https://github.com/tisnik/python-programming-courses/blob/master/Python2/examples/pitfalls/mutating_list.py)
