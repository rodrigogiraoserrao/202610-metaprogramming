class Colour:
    def __init__(self, r, g, b):
        self._r = r

    @property
    def r(self):
        return self._r

red = Colour(255, 0, 0)
print(red.r)  # 255

red.r = 300
red.r = -30
red.r = "bananas"