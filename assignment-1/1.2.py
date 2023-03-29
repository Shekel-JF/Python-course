import sys
argv = sys.argv
for i in range(1,len(argv)):
    number = int(argv[i])
    print( str( number) + ' = ', end = '')
    distr = ''
    k = 2

    while number > 1:
        power = 0
        while number % k == 0:
            power += 1
            number/= k

        if power > 1:
            distr += str(k) + '^' + str(power) + '*'
            
        elif power == 1:
            distr += str(k) + '*'
        k+=1

    print(distr[:-1])
    