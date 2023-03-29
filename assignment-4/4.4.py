from functools import singledispatch, singledispatchmethod
from math import ceil

class Mean:
	@singledispatchmethod
	def calculate(self, arg):
		return "Unknown overload"

	@calculate.register (list)
	def _(self, arg):
		result = 0
		for i in range (0, len(arg)):
			result += arg[i]
		return result / len(arg)

	@calculate.register (set)
	def _(self, arg):
		result = 0
		for i in arg:
			result += i
		return result / len(arg)

	@calculate.register (tuple)
	def _(self, arg):
		result = 0
		for i in range (0, len(arg)):
			result += int(arg[i])
		return result / len(arg)

	@calculate.register (dict)
	def _(self, arg):
		result = {}
		for i in arg:
			result[i] = (i + arg[i]) / 2
		return result


mean = Mean()

print (mean.calculate ("tekst"))
print (mean.calculate ([700, 15, 1604, 124, 420]))
print (mean.calculate ({1, 2, 3, 4}))
print (mean.calculate (("200", "300", "400"))) 
print (mean.calculate ({17: 21, 67: 1728}))

print("\n\n")

@singledispatch
def volume(arg):
	return "Unknown overload"

@volume.register
def _(a:int, b:int, c:int):
	return a * b * c

@volume.register
def _(a:float, b:float, c:float):
	return ceil(a) * ceil(b) * ceil(c)

@volume.register
def _(a:tuple):
	return int(a[0]) *int (a[1])* int(a[2])

print(volume("carbonara"))
print(volume(7, 2, 3))
print(volume(7.3, 2.5, 13))
print(volume(("4", "7", "9")))