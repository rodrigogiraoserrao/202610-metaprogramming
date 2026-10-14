class Person:
    def __init__(self, first, last):
        # The leading underscore means “this attribute is ‘private’”
        # “private” is just a convention
        self._first = first
        self._last = last

john = Person("John", "Doe")
john._first = "Steve"
