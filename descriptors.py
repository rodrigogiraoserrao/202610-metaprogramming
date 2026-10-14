class GlorifiedAttribute:  # Descriptor: class WITH a method __get__
    def __get__(self, _1, _2):
        print("Inside __get__ in GlorifiedAttribute")
        return 42

class ClassWithASingleAttribute:
    bananas = GlorifiedAttribute()

print("1")
obj = ClassWithASingleAttribute()
print("2")
print(obj.bananas)
print("3")