class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

john = Person("John", "Doe")

def get_name(person):
    return f"{person.first} {person.last}"
Person.get_name = get_name

print(john.get_name())  # John Doe