A = int(input())
B = int(input())
if A <= B:
	print(*(i for i in range(A, B+1)))
else:
	for i in range(A, B-1, -1):
		print(i, end=' ')