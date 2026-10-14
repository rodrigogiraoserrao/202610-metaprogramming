class GlorifiedAttribute:
    def __get__(self, _, _):
        return 42

class ClassWithASingleAttribute:
    bananas = GlorifiedAttribute()

obj = ClassWithASingleAttribute()
print(obj.bananas)