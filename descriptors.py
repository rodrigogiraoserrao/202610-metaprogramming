class GlorifiedAttribute:  # Descriptor: class WITH a method __get__
    def __get__(self, _1, _2):
        return 42

class ClassWithASingleAttribute:
    bananas = GlorifiedAttribute()

obj = ClassWithASingleAttribute()
print(obj.bananas)