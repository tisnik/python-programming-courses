#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Přečtení objektů z databáze."""

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


with shelve.open("test") as db:
    print(db["employee1"])
    print(db["employee2"])
    print(db["employee3"])
