def reverse(array, left, right):
    while left < right:
        temp = array[left]
        array[left] = array[right]
        array[right] = temp
        left += 1
        right -= 1
    return array

list = [-2 , 3, 4, -1, 2, 5, 7]
print("Lista przed odwróceniem: ")
print(list)
print("Lista po odwróceniu elementów o indeksach od 2 do 5: ")
print(reverse(list, 2, 5))
