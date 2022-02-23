n = int(input())
c = 1
max1 = 0
while n != 0:
	if n > max1:
		max1 = n
		c = 1
	else:
		if n == max1:
			c += 1
	n = int(input())
print(c)