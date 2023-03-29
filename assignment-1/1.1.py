while 1:
    x = int(input('Podaj nieparzysta liczbe: '))
    if x/2 == int(x/2):
        print('Podano liczbe parzysta')
    else:
        print(x * '*')
        y = 1
        while y < x/2 - 1:
            print(y * ' ' + '*' + (x - 2 * y - 2) * ' ' + '*' + y * ' ')
            y+=1
        print(y * ' ' + '*')
        quit()