class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def name(self):
        return f"{self.first} {self.last}"

john = Person("John", "Doe")
print(john.name())
john.first = "Steve"
print(john.name())