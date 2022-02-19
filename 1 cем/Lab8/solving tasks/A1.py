def pr(n):
	i = int(n**(0.5))
	while n != 0:
		if n >= i**2:
			n -= i**2
			print(i, end=' ')
		else:
			i -= 1
pr(1)
print()
pr(2)
print()
pr(3)
print()
pr(4)