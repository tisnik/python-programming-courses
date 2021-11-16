#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Statická metoda."""


class Employee:
    """Třída reprezentující zaměstnance."""

    counter = 0

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        Employee.inc_counter()
        Employee.dec_counter()

    def display_employee(self):
        """Metoda pro výpis hodnoty objektu."""
        print("Full name: {name} {surname}   Salary: {salary}".format(
            name=self._first_name,
            surname=self._surname,
            salary=self._salary))

    @classmethod
    def inc_counter(cls):
        cls.counter += 1

    @staticmethod
    def dec_counter():
        # !!!
        cls.counter += 1

    @classmethod
    def num_employees(cls):
        return cls.counter



# vytvoření dvou instancí třídy
employee1 = Employee("Eda", "Wasserfall", 10000)
print("Now we have", Employee.num_employees(), "employees")

employee2 = Employee("Přemysl", "Hájek", 25001)
print("Now we have", Employee.num_employees(), "employees")


# výpis hodnot objektů
employee1.display_employee()
employee2.display_employee()
