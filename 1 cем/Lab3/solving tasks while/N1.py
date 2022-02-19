n = int(input())
c = 0
max1 = 0
max2 = 0
while n != 0:
	if n > max1:
		max2 = max1
		max1 = n
	else:
		if n > max2:
			max2 = n
	n = int(input())
print(max2)