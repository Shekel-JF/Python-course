from math import hypot, atan, sin, cos, sqrt

class Zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def conjugate(self):
        return self.__class__(self.r, -self.i)

    def argz(self):
        return atan(self.i / self.r)

        
    def __abs__(self):
        return Zespolona(sqrt(self.r**2 - self.i**2), 0)

    def __repr__(self):
        return f'Zespolona({self.r}, {self.i})'

    def __str__(self):
        if self.i < 0:
            return f'({self.r}{self.i}j)'
        else:
            return f'({self.r}+{self.i}j)'

    def __add__(self, other):
        if isinstance(other, (float, int)):
            return Zespolona(self.r + other, self.i)
        else:
            return Zespolona(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        if isinstance(other, (float, int)):
            return Zespolona(self.r - other, self.i)
        else:
            return Zespolona(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Zespolona(self.r * other, self.i*other)
        else:
            return Zespolona(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rsub__(self, other):
        other = Zespolona(other, 0)
        return other.__sub__(self)

    def __eq__(self, other):
        if self.i == other.i and self.r == other.r:
            return 1
        else:
            return 0

    def __ne__(self, other):
        if self.i == other.i and self.r == other.r:
            return 0
        else:
            return 1

    def __pow__(self, other):
        result = self
        while other > 1:
            result *= self
            other-=1
        return result


def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a == b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a ** 2)
    print(b ** 4)


if __name__ == "__main__":
    main()