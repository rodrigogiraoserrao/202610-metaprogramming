class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # an attribute access becomes a method call
    def _name(self):
        return f"{self.first} {self.last}"

john = Person("John", "Doe")
print(john._name)
john.first = "Steve"
print(john._name)