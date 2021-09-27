a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = -b // a
if (c * x) + d == 0:
	print('NO')
elif a == 0 and b == 0:
	print('INF')
else:
	print(x)
