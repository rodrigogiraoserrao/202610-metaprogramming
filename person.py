class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def get_name(self):
        return f"{self.first} {self.last}"

john = Person("John", "Doe")
print(john.get_name())
john.first = "Steve"
print(john.get_name())