class Person:
    def __init__(self, first, last):
        # The leading underscore means “this attribute is ‘private’”
        # “private” is just a convention
        self._first = first
        self._last = last

    @property
    def first(self):
        return self._first

    @property
    def last(self):
        return self._last

john = Person("John")
print(john.first)

john.first = "Steve"
