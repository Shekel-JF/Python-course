def contains(str, set):
    for c in str:
        if c in set:
            continue
        else:
            print("Podano zly zapis!")
            quit()

def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    contains(s, roman)
    result = 0
    for i in range(len(s)):
        if i > 0 and roman[s[i]] > roman[s[i - 1]]:
            result += roman[s[i]] - 2 * roman[s[i - 1]]
        else:
            result += roman[s[i]]
    return result

def int_to_roman(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV","I"]
    result = ''
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            result += rom[i]
            n -= val[i]
        i += 1
    return result

x = input("Wprowadz liczbe w zapisie rzymskim lub arabskim: ")
if x.isdigit():
    print(int_to_roman(int(x)))
else:
    print(roman_to_int(x))