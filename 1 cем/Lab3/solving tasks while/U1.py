n = int(input())
c = 1
s = 1
while n != 0:
    n1 = int(input())
    if n == n1:
        c += 1
    else:
        if c > s:
            s = c
        c = 1
    n = n1
print(s)