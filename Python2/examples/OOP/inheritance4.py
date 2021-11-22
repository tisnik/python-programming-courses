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
