class ReadOnlyAttr:
    def __set_name__(self, owner, name):
        print("Inside __set_name__")
        print(owner, name)
        self.attribute_name = f"_{name}"

    def __get__(self, obj, _):
        return getattr(obj, self.attribute_name)

class Person:
    first = ReadOnlyAttr()
    last = ReadOnlyAttr()

    def __init__(self, first, last):
        # The leading underscore means “this attribute is ‘private’”
        # “private” is just a convention
        self._first = first
        self._last = last

john = Person("John", "Doe")
print(john.first)
print(john.last)