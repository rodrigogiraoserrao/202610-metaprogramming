"""
Finish implementing the class `Colour` so that it supports
three properties: r, g, and b.
All three properties must have the “basic” getter (like `r`)
and all three properties must have the setter that performs validation:
 - the new value is in the range [0, 255] (inclusive)
 - the new value is an integer
"""

class Colour:
    def __init__(self, r, g, b):
        self._r = r

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, new_r):
        """Validate the new value of R."""
        if not 0 <= new_r <= 255:
            raise ValueError("Red must be between 0 and 255")

        self._r = new_r

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, new_g):
        """Validate the new value of G."""
        if not 0 <= new_g <= 255:
            raise ValueError("Green must be between 0 and 255")

        self._g = new_g

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, new_b):
        """Validate the new value of B."""
        if not 0 <= new_b <= 255:
            raise ValueError("Blue must be between 0 and 255")

        self._b = new_b

red = Colour(255, 0, 0)
print(red.r)  # 255

red.r = 300
red.r = -30
red.r = "bananas"