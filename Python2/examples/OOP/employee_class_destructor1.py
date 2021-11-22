#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Ukázka jednoduché třídy reprezentující zaměstnance."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        print("Konstruktor:", first_name, surname)
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def __del__(self):
        """Destruktor objektu."""
        print("Destruktor:", self._first_name, self._surname)


def test_destructor():
    # vytvoření dvou instancí třídy
    employee1 = Employee("Eda", "Wasserfall", 10000)
    employee2 = Employee("Přemysl", "Hájek", 25001)


test_destructor()
