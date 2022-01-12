#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zápis objektů do databáze."""

import shelve


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        self._poznamka = 124

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "name: {name} {surname}   Salary: {salary}".format(
            name=self._first_name, surname=self._surname, salary=self._salary
        )

    def __eq__(self, other):
        if other is None:
            return False
        return (
            self._first_name == other._first_name
            and self._surname == other._surname
            and self._salary == other._salary
        )


# vytvoření tří instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Eda", "Wasserfall", 10000)
employee3 = Employee("Přemysl", "Hájek", 25001)


with shelve.open("test") as db:
    db["employee1"] = employee1
    db["employee2"] = employee2
    db["employee3"] = employee3
