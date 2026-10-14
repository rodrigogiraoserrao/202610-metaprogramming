class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

john = Person("John", "Doe")

def get_name(person):
    return f"{person.first} {person.last}"
Person.get_name = get_name

print(john.get_name())  # John Doe

# ---

class Method:
    def __init__(self, lambda_func):
        self.lambda_func = lambda_func

    def __get__(self, obj, _):
        return lambda: self.lambda_func(obj)

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    get_name = Method(lambda self: f"{self.first} {self.last}")

john = Person("John", "Doe")
print(john.get_name ())














