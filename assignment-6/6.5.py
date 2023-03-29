from itertools import product

K, M = map(int, input().split())

arr = []

for n in range (K):
    x = list(map(int, input().split()))
    arr.append(x[1:])
    
arr = list(product(*arr))

values = []
for n in arr:
    values.append(sum(map(lambda x: x*x, n))%M)
    
res = max(values)
print(res)