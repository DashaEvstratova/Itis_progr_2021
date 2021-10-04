n = int(input())
c1 = 1
c2 = 1
s2 = 1
s1 = 1
while n != 0:
    n1 = int(input())
    if n > n1:
        c1 += 1
        if c2 > s2:
            s2 = c2
        c2 = 1
    elif n < n1:
        if c1 > s1:
            s1 = c1
        c2 += 1
        c1 = 1
    else:
        if c2 > s2:
            s2 = c2
        c2 = 1
        if c1 > s1:
            s1 = c1
        c2 += 1
        c1 = 1
    n = n1
if c1 > s1:
    s1 = c1
if c2 > s2:
    s2 = c2
if s1 > s2:
    print(s1)
else:
    print(s2)