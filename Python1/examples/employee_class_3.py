#!/usr/bin/env python3
# vim: set fileencoding=utf-8


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "Full name: {name} {surname}   Salary: {salary}".format(
                name=self._first_name,
                surname=self._surname,
                salary=self._salary)


# vytvoření dvou instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Přemysl", "Hájek", 25001)

# výpis hodnot objektů
print(employee1)
print(employee2)
