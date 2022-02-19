a = 0
b = 0
c = 0
n = int(input())
q = []
while n != 0:
    q.append(n)
    n = int(input())
for i in range(0, len(q)-1):
    if q[i] > q[i+1]:
        c += 1
    else:
        a = max(a, c)
        c = 0
a = max(a, c)
c = 0
for i in range(0, len(q)-1):
    if q[i] < q[i+1]:
        c += 1
    else:
        b = max(a, c)
        c = 0
b = max(a, c)
 
print(max(a, b))