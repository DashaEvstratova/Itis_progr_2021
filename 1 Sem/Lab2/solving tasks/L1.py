x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if y1 < y2:
	if x1 - x2 == y1 - y2 or x2 - x1 == y1 - y2:
		print('YES')
	else:
		print('NO')
else:
	print('NO')