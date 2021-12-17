class Person:
    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        print("Person.__init__")
        self._first_name = first_name
        self._surname = surname

    def get_name(self):
        return "Person:  {} {}".format(self._first_name, self._surname)

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Person** Full name: {name} {surname}".format(
            name=self._first_name, surname=self._surname
        )


class Student(Person):
    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        print("Student.__init__")
        super().__init__(first_name, surname)

    def get_name(self):
        return "Student: {} {}".format(self._first_name, self._surname)

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Student** Full name: {name} {surname}".format(
            name=self._first_name, surname=self._surname
        )


class Employee(Person):
    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        print("Employee.__init__")
        super().__init__(first_name, surname)
        self._salary = salary

    def calc_bonus(self):
        return self._salary * 0.5

    def get_name(self):
        return "Employee: {} {}".format(self._first_name, self._surname)

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Employee** Full name: {name} {surname}   Salary: {salary}".format(
            name=self._first_name, surname=self._surname, salary=self._salary
        )


class Manager(Employee):
    def __init__(self, first_name, surname, salary):
        """Konstruktor objektu."""
        print("Manager.__init__")
        super().__init__(first_name, surname, salary)

    def calc_bonus(self):
        return self._salary * 0.75


e1 = Employee("Eric", "Iverson", 10000)
m1 = Manager("aaa", "bbb", 10000)

print(e1.calc_bonus())
print(m1.calc_bonus())
