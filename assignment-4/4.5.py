from multipledispatch import dispatch

class Figura(object):
    def __init__(self):
        print("Figura init")

class Prostokat(Figura):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Kwadrat(Prostokat):
    def __init__(self, x):
        super().__init__(x, x)

@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0

@dispatch(Prostokat)
def pole(self):
    return self.x * self.y

@dispatch(Prostokat, int, int)
def pole(self, x, y):
    self.x = x
    self.y = y
    return x * y

@dispatch(Kwadrat)
def pole(self):
    return self.x**2

@dispatch(Kwadrat, int)
def pole(self, x):
    self.x = x
    return x * x

a, b, c = Figura(), Prostokat(2,4), Kwadrat(2)

bb = pole(b, 5, 6)
print(bb)
cc = pole(c, 7)
print(cc)


def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(pole(i))

polaPowierzchni([a,b,c])