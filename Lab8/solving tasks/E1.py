def ReduceFraction(n, m):
	i = min(n, m)
	while i != 1:
		if m % i == 0 and n % i == 0:
			m = m//i
			n = n//i
		else:
			i -=1
	print(n, m)

ReduceFraction(12, 16)
ReduceFraction(7, 9)
ReduceFraction(10, 100)