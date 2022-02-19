A = int(input())
B = int(input())
for i in range(A, B+1):
	c = i // 100
	#swap the last two digits
	d = int(str((i % 100) % 10) + str((i % 100) // 10))
	if c == d:
		print(i)