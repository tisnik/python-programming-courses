class Employee:
    """Třída reprezentující zaměstnance."""

    __counter = 0

    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        Employee.inc_counter()

    def display_employee(self):
        """Metoda pro výpis hodnoty objektu."""
        print("Full name: {name} {surname}   Salary: {salary}".format(
            name=self._first_name,
            surname=self._surname,
            salary=self._salary))

    @classmethod
    def inc_counter(cls):
        cls.__counter += 1

    @classmethod
    def num_employees(cls):
        return cls.__counter


def test():
    # vytvoření dvou instancí třídy
    employee1 = Employee("Eda", "Wasserfall", 10000)
    print("Now we have", Employee.num_employees(), "employees")

    employee2 = Employee("Přemysl", "Hájek", 25001)
    print("Now we have", Employee.num_employees(), "employees")


test()
print("Now we have", Employee.num_employees(), "employees")
