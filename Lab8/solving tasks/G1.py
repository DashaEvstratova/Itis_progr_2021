def degree(a, n):
	if n % 2 == 0:
		return degree(a**2, n/2)
	elif n == 1:
		return a
	else:
		return a * degree(a, n-1)

print(degree(2, 1))
print(degree(2, 2))
print(degree(2, 3))