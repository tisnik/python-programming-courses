#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Gettery a settery."""


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        self._poznamka = 124
        self._age = None

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "name: {name} {surname}   Salary: {salary}   Age: {age}".format(
            name=self._first_name,
            surname=self._surname,
            salary=self._salary,
            age=self._age,
        )

    def set_age(self, age):
        if age <= 0:
            raise ValueError("The age must be positive")
        self._age = age

    def get_age(self):
        return self._age


# vytvoření tří instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Eda", "Wasserfall", 10000)

employee1.set_age(30)
employee2.set_age(40)

# výpis hodnot objektů
print(employee1)
print(employee2)
