class ReadOnlyAttr:
    def __get__(self, obj, _):
        return obj.???

class Person:
    first = ReadOnlyAttr()
    last = ReadOnlyAttr()

    def __init__(self, first, last):
        # The leading underscore means “this attribute is ‘private’”
        # “private” is just a convention
        self._first = first
        self._last = last
