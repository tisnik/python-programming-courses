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
            name=self._first_name, surname=self._surname
        )


class Student(Person):
    pass


# vytvoření dvou instancí třídy
p1 = Person("Eda", "Wasserfall")
p2 = Person("Přemysl", "Hájek")

print(p1)
print(p2)

s1 = Student("John", "Doe")

print(s1)
