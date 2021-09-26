x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if y1 == y2 and (x1 + 1 == x2 or x1 - 1 == x2):
	print('YES')
elif x1 == x2 and (y1 + 1 == y2 or y1 - 1 == y2):
	print('YES')
elif y1 + 1 == y2 and x1 + 1 == x2:
	print('YES')
elif y1 - 1 == y2 and x1 + 1 == x2:
	print('YES')
elif y1 + 1 == y2 and x1 - 1 == x2:
	print('YES')
elif y1 - 1 == y2 and x1 - 1 == x2:
	print('YES')
else:
	print('NO')
