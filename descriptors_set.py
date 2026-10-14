class ColourComponent:
    ...

class HexColour:
    r = ...
    g = ...
    b = ...

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