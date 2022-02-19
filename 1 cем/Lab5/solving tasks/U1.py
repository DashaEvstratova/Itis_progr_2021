from fractions import Fraction
n = Fraction(input())
p = n.numerator
q = n.denominator
k = 1
while p != 1:
	k =int(q/p) + 1
	if p * k - q >= 0:
		p = p * k - q
		q = q * k
		print(Fraction(1, k), end=' ')
print(Fraction(1, q))