class Person:
    def __init__(self, first):
        # The leading underscore means “this attribute is ‘private’”
        # “private” is just a convention
        self._first = first

    @property
    def first(self):
        return self._first

john = Person("John")
print(john.first)

john.first = "Steve"