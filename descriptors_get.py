class GlorifiedAttribute:  # Descriptor: class WITH a method __get__
    def __init__(self, value):
        self.value = value

    def __get__(self, _, __):
        print("Inside __get__ in GlorifiedAttribute")
        return self.value

class ClassWithASingleAttribute:
    bananas = GlorifiedAttribute(42)
    apples = GlorifiedAttribute(23)

obj = ClassWithASingleAttribute()
print(obj.bananas)
print(obj.apples)
