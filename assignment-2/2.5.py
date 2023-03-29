def fun(N):
    x = bin(N)
    temp = 0
    length = 0
    for n in x:
        if n == '0':
            temp+=1
        elif temp > length:
            length = temp
            temp = 0

        
    return length


x = int(input('Podaj liczbe naturalna: '))
print('Dlugosc najdluzszej przerwy binarnej: ', fun(x))