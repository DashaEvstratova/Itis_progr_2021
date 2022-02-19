k = int(input())
c = 0
i = 1
while i != k:
    a = str(i)
    if a == a[::-1]:
        c += 1
    i += 1
print(c)