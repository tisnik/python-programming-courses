#!/usr/bin/env python3
# vim: set fileencoding=utf-8


class Employee:
    """Třída reprezentující zaměstnance."""

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    def display_employee(self):
        """Metoda pro výpis hodnoty objektu."""
        print("Full name: ", self._first_name, self._surname, "   Salary: ", self._salary)


# vytvoření dvou instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
employee2 = Employee("Přemysl", "Hájek", 25001)

# výpis hodnot objektů
employee1.display_employee()
employee2.display_employee()
