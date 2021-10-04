n = int(input())
c = 0
while n != 0:
	a = int(input())
	if a > n:
		c += 1
	n = a
print(c)