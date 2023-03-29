while(1):
    print('Podaj 4 liczby naturalne: ')

    x = int (input ("x = "))
    y = int (input ("y = "))
    z = int (input ("z = "))
    n = int (input ("n = "))
    if(x < 0 or y < 0 or z < 0 or n < 0):
        print('Nie podano liczb naturalnych\n')
    else:
        break


coords = []
for a in range (x + 1):
    for b in range (y + 1):
        for c in range (z + 1):
            if(a + b + c != n):
                coords.append([a, b, c])

print('Lista mozliwych wspolrzednych:')
print(coords)