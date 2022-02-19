n = int(input())
maxim = 0
while n != 0:
	if n > maxim:
		maxim = n
	n = int(input())
print(maxim)