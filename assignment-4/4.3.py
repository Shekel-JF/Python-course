# podpunkt A) 
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo, 
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo(self, x):
        print(f'wykonanie foo({self}, {x})')
   
    @classmethod
    def class_foo(cls, x):
        print(f'class_foo({cls}, {x})')

    @staticmethod
    def static_foo(x):
        print(f'wykonanie static_foo({x})')

a = A()
a.foo(123) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a,123) # ditto
a.class_foo(123) # class_foo(<class '__main__.A'>, 123)
A.class_foo(123) # ditto
a.static_foo(123) # wykonanie static_foo(123)
A.static_foo(123) # ditto

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod
import math

class Block(ABC):
    @abstractmethod
    def volume(self):
        pass

class Cuboid(Block):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x*self.y*self.z

class Cylinder(Block):
    def __init__(self, y, r):
        self.y = y
        self.r = r

    def volume(self):
        return self.y * math.pi*self.r*self.r


A = Cuboid(4, 5, 6)
print(A.volume())

B = Cylinder(5, 2)
print(B.volume())


# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez 
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu

print("\n\n\n")

class GasStation:
    def __init__(self):
        print("Stacja otwarta!")
        self._fuel = 600

    @property
    def fuel(self):
        print("Pozostalo " + str(self._fuel) + " litrow paliwa\n")
        return self._fuel
    
    @fuel.setter
    def fuel(self, fuel):
        if(fuel < self._fuel and self.fuel != 0):
            print("Zatankowano " + str(fuel) + " litrow!")
            self._fuel -= fuel
        else:
            fuel = self.fuel
            print("Zatankowano " + str(fuel) + " litrow i skonczylo sie paliwo!")
            print("Zapraszamy jutro!")
            self._fuel = 0

bmw = GasStation()
bmw.fuel = 50
bmw.fuel = 30
bmw.fuel = 100
#print(bmw.fuel)
bmw.fuel = 200
bmw.fuel = 180
bmw.fuel = 40
