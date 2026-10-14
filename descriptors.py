class GlorifiedAttribute:
    def __get__(self, obj, _):
        return 42

class ClassWithASingleAttribute:
    bananas = ...