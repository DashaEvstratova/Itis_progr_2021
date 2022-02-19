def power(a, n):
	b = a
	for i in range(1, n):
		a = a*b
	return(a)
print(power(2, 1))
print(power(2, 2))
print(power(2, 3))