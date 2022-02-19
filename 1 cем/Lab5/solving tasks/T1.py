a = input()
s = ''
for i in range(0, len(a)):
    if i % 3 != 0:
        s += a[i]
print(s)
    