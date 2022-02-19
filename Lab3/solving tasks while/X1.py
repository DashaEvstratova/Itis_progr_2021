n = int(input())
s = 0
c = 0
q = []
while n != 0:
    s = s + n
    c = c + 1
    q.append(n)
    n = int(input())
s = s / c
i = 0
res = 0
while i != len(q):
    res = res + (q[i] - s)**2
    i = i + 1
print((res/(c-1))**0.5)