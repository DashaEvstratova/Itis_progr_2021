q = []
n = int(input())
while n != 0:
    q.append(n)
    n = int(input())
max2 = 0
max1 = 0
minrast = 10000
for i in range(1, len(q) - 2):
    if q[i] > q[i+1] and q[i] > q[i-1]:
        max2 = max1
        max1 =  i
        if (max1 > 0) and (max2 > 0) and (max1 - max2 < minrast):
            minrast = max1 - max2 - 1
if minrast == 10000: 
    minrast = 0
print(minrast)