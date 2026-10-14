# 1. Define a class `Number` that accepts a single integer as an argument.
# Define two subclasses of `Number` called `OddNumber` and `EvenNumber`.
# When you create an instance of `Number(x)`, check the parity of the integer `x`
# and create an instance of the correct subclass.

# Example: Number(3)  -> OddNumber(3)
# Example: Number(20) -> EvenNumber(20)

# When you finish, please paste your code in the chat.

# 2. Improve `OddNumber` and `EvenNumber` so that if they’re instantiated
# directly with the wrong integers, there’s a runtime error.

class Number:
    def __new__(cls, value):
        if cls is Number:
            cls = OddNumber if value % 2 else EvenNumber
        return super().__new__(cls)

class OddNumber(Number):
    def __new__(cls, value):
        if value % 2 == 0:
            raise ValueError(f"{value} isn't odd!")

class EvenNumber(Number):
    ...

print(OddNumber(42))
