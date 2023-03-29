while 1:
    x = int(input('Podaj szerokosc prostokata: '))
    y = int(input('Podaj wysokosc prostokata: '))
    if(x < 1 or y < 1):
        print('\nPodaj liczby naturalne!\n')
    else:
        break

square = '+' + x * '---+' + '\n'
for n in range (y):
    square+= '|' + x * '   |' + '\n'
    square+= '+' + x * '---+' + '\n'
print(square)
