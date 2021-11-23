class Person:

    def __init__(self, first_name, surname):
        """Konstruktor objektu."""
        self._first_name = first_name
        self._surname = surname

    def get_name(self):
        return "{} {}".format(self._first_name, self._surname)

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Person** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


class Student(Person):

    def __str__(self):
        """Speciální metoda pro převod objektu na řetězec."""
        return "**Student** Full name: {name} {surname}".format(
                name=self._first_name,
                surname=self._surname)


# vytvoření dvou instancí třídy
p1 = Person("Eda", "Wasserfall")
p2 = Person("Přemysl", "Hájek")

print(p1.get_name())
print(p2.get_name())

s1 = Student("John", "Doe")

print(s1.get_name())

print(type(p1))
print(type(s1))
