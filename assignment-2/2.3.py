x = input('Wpisz lancuch znakowy: ')

digits = 0
letters = 0
stats = {}

for n in x:
    stats[n] = 0

for n in x:
    if n.isnumeric():
        digits+=1
    elif n.isalpha():
        letters+=1

    stats[n]+=1

print('Ilosc slow: ' + str(len(x.split())))
print('Ilosc liter: ' + str(letters))
print('Ilosc cyfr: ' + str(digits))
print("Czestosc wystepowania poszczegolnych znakow:\n" + str(stats))