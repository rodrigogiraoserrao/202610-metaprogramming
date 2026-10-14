class ReadOnlyAttr:
    def __set_name__(self, owner, name):
        print("Inside __set_name__")
        print(owner, name)

    def __get__(self, obj, _):
        return None

class Person:
    first = ReadOnlyAttr()
    last = ReadOnlyAttr()

    def __init__(self, first, last):
        # The leading underscore means “this attribute is ‘private’”
        # “private” is just a convention
        self._first = first
        self._last = last
