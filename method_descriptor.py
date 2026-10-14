class Method:
    def __init__(self, lambda_func):
        self.lambda_func = lambda_func

    def __get__(self, obj, _):
        def bound_method(*args, **kwargs):
            return self.lambda_func(obj, *args, **kwargs)
        return bound_method

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    get_name = Method(lambda self: f"{self.first} {self.last}")

john = Person("John", "Doe")
print(john.get_name)
print(john.get_name ())