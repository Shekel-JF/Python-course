def Insert(L):
    if(any(isinstance(n, list) for n in L)):
        for n in L:
            if(isinstance(n, list)):
                n = Insert(n)
    else:
        return L.append(L[-1] + 1)

list1 = [1, 2, [3, 4, [5, 6], 5], 3, [4, 5]]
list2 = [1, [3], [2]] 

print('Lista 1 przed wywolaniem funkcji:')
print(list1)
Insert(list1)
print('\nLista 1 po wywołaniu funkcji')
print(list1)

print('\n\nLista 2 przed wywolaniem funkcji:')
print(list2)
Insert(list2)
print('\nLista 2 po wywołaniu funkcji')
print(list2)