x = int(input('Podaj liczbe: '))
ruler = x * '|....' + '|\n0'
for n in range (1, x + 1):
    ruler += str(n).rjust(5)
print(ruler)