class ColourComponent:  # Descriptor
    def __init__(self, start, end):
        self.start, self.end = start, end

    #                `obj` is the object that contains the descriptor
    #                     `cls` the class (or the type) of the object that contains
    #                     the descriptor
    def __get__(self, obj, cls):
        return int(obj.hex[self.start:self.end], 16)

    # __set__ accepts the object that is having one of its attributes
    # set to, and the value that's being used in the assignment.
    def __set__(self, obj, value):

class HexColour:
    r = ColourComponent(1, 3)
    g = ColourComponent(3, 5)
    b = ColourComponent(5, 7)

    def __init__(self, hex_str):
        self.hex = hex_str


# Getting components and their values:
colour = HexColour("#ff0000")  # red
print(colour.r)  # 255
print(colour.g)  # 0

# ---
# Setting components:

colour.r = 0
colour.g = 255
print(colour.hex)  # '#00ff00'