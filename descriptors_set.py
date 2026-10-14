class ColourComponent:
    ...

class HexColour:
    r = ...
    g = ...
    b = ...


colour = HexColour("#ff0000")  # red
print(colour.r)  # 255
print(colour.g)  # 0
colour.r = 0
colour.g = 255
print(colour.hex)  # '#00ff00'