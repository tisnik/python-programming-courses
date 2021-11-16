#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vylepšení metody pro výpis hodnoty objektu."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def display_employee(self):
        """Metoda pro výpis hodnoty objektu."""
        print("Full name: {name} {surname}   Salary: {salary}".format(
            name=self._first_name,
            surname=self._surname,
            salary=self._salary))


# vytvoření dvou instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Přemysl", "Hájek", 25001)

# výpis hodnot objektů
employee1.display_employee()
employee2.display_employee()
