from fractions import Fraction
n = int(input())
q = []
s = []
q.append(Fraction(1, 0))
q.append(Fraction(1/1))
i = 1
while i != n:
    s.append(q[0])
    for j in range(0, len(q)-1):
        s.append(Fraction(q[j].numerator, q[j+1].denominator))
    s.append(q[-1])
    i += 1
    q = s
print(s)