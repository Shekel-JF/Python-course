S = list(input())

lower = []
upper = []
even = []
odd = []

for n in S:
    if n.isalpha():
        if n.isupper():
            upper.append(n)
        else:
            lower.append(n)
    else:
        if int(n) % 2 != 0:
            odd.append(n)
        else:
            even.append(n)
lower.sort()
upper.sort()
odd.sort()
even.sort()

for m in lower:
    print(m, end = "")
for m in upper:
    print(m, end = "")
for m in odd:
    print(m, end = "")
for m in even:
    print(m, end = "")
