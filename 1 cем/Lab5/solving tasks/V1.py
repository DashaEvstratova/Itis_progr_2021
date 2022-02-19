from fractions import Fraction
n = int(input())
q = []
s = []
q1 = []
s1 = []
i = 1
j = 0
while i - 1 != n:
    q1.append(0)
    s1.append(1)
    for j in range(0, len(s)-1):
        if s[j] + s[j + 1] <= i:
            q1.append(q[j] + q[j + 1])
            s1.append(s[j] + s[j + 1])
        q1.append(q[j + 1])
        s1.append(s[j + 1])
    if i == 1:
        q1.append(1)
        s1.append(1)
    q = q1
    s = s1
    q1 = []
    s1 = []
    i += 1
print('0/1', sep='', end=' ')
for i in range(1, len(s)-1):
    print(Fraction(q[i], s[i]), sep='', end=' ')
print('1/1', sep='')