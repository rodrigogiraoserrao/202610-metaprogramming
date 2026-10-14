class Colour:
    def __init__(self, r, g, b):
        self.r = r

    @property
    def r(self):
        return self.r

red = Colour(255, 0, 0)
print(red.r)

red.r = 300
red.r = -30
red.r = "bananas"